"""Independent predicates and source checks for finite classification audit."""
import math
import unittest
from itertools import product
from classification_audit import (source_games, automorphisms, classify, diagram_audit,
                                   equality_patterns, specialize)
from matching_audit import bijections, multiply


def independent_preserves(g,game):
    p,fs=g; n=len(p)
    inv=tuple(p.index(j) for j in range(n))
    for s,u in game.items():
        image=tuple(fs[inv[j]][s[inv[j]]] for j in range(n))
        if tuple(game[image][p[i]] for i in range(n)) != u: return False
    return True


class ClassificationAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.games,cls.records=source_games()

    def test_source_extraction(self):
        self.assertEqual(self.games['2.1'][(1,1,0)],(5,5,4))
        self.assertEqual(self.games['5.13'][(0,0,1)],('beta','gamma','delta'))
        self.assertEqual(self.games['5.16'][(1,1,1,1,1,1)],(29,30,29,30,29,30))
        self.assertEqual(len(self.records['5.14']['tables']),8)
        for game in self.games.values():
            n=len(next(iter(game)))
            self.assertEqual(set(game),set(product(range(2),repeat=n)))
            self.assertTrue(all(len(u)==n for u in game.values()))

    def test_independent_automorphism_predicate(self):
        for ident in ['4.1','5.13','5.14a','5.14b','5.15','5.16']:
            game=self.games[ident]; n=len(next(iter(game)))
            expected={g for g in bijections((2,)*n) if independent_preserves(g,game)}
            actual=set(automorphisms(game))
            self.assertEqual(expected,actual,ident)
            self.assertTrue(all(multiply(g,h) in actual for g in actual for h in actual),ident)

    def test_generic_classification(self):
        expected={'5.13':(6,6,True,False),'5.14a':(8,4,False,False),
                  '5.14b':(16,4,False,False),'5.15':(48,24,False,False),'5.16':(12,12,False,False)}
        for ident,want in expected.items():
            got=classify(self.games[ident]); self.assertEqual(tuple(got[k] for k in ['automorphism_order','player_image_order','standard','fully']),want)
            if ident!='5.16': self.assertEqual(got['pure_equilibria'],None)
        self.assertEqual(classify(self.games['4.1'])['pure_equilibria'],[])

    def test_parameter_boundaries(self):
        game=self.games['5.13']; names=sorted(set(sum((list(v) for v in game.values()),[])))
        for pat in equality_patterns(4):
            got=classify(specialize(game,pat)); d=dict(zip(names,pat))
            self.assertEqual(got['fully'],d['beta']==d['gamma'])
            # Exact NE characterization for every weak order represented here.
            for s in product(range(2),repeat=3):
                expected=(d['alpha']>=d['delta']) if len(set(s))==1 else (d['delta']>=d['alpha'])
                self.assertEqual(s in got['pure_equilibria'],expected)
        for ident in ['5.12','5.13','5.14a','5.14b','5.15']:
            game=self.games[ident]; k=len({v for row in game.values() for v in row})
            got=classify(specialize(game,[0]*k)); n=got['n']
            self.assertEqual(got['automorphism_order'],math.factorial(n)*2**n)
            self.assertTrue(got['fully'])

    def test_diagram_completeness_and_edges(self):
        for n,count in [(2,4),(3,7)]:
            got=diagram_audit(n)
            self.assertEqual(got['family_count'],count)
            self.assertTrue(got['source_all_nodes_match'])
            self.assertTrue(got['source_edges_match'])
            self.assertTrue(all(got['generator_tables_match'].values()))

    def test_printed_generators_generate_actual_generic_aut(self):
        from classification_audit import source_generators, generated_by
        for ident,gs in source_generators().items():
            self.assertEqual(generated_by(gs),set(automorphisms(self.games[ident])))

    def test_all_eight_parameter_coincidences(self):
        import json
        from parameter_audit import OUTPUT, verify
        self.assertEqual(verify(json.loads(OUTPUT.read_text())),4140)

if __name__=='__main__':unittest.main()
