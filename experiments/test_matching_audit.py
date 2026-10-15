import unittest
from itertools import permutations, product
from matching_audit import (action, audit, bijections, implies, matching_element,
                            matchings, multiply, partition, satisfies, subgroups,
                            strategy_trivial, relabel_game, weakly_anonymous)


class MatchingAuditTests(unittest.TestCase):
    def test_typed_composition(self):
        for sizes in [(2,2),(1,2),(2,2,2)]:
            gs=bijections(sizes)
            for g in gs:
                for h in gs:
                    for s in product(*(range(m) for m in sizes)):
                        self.assertEqual(action(multiply(g,h),s),action(g,action(h,s)))

    def test_subgroups_known_counts(self):
        self.assertEqual(len(subgroups(bijections((2,2)))),10)
        self.assertEqual(len(subgroups(bijections((2,2,2)))),98)

    def test_all_domains(self):
        for sizes in [(1,1),(2,2),(3,3),(1,1,1),(2,2,2),(1,2),(1,1,2)]:
            r=audit(sizes)
            for key in ['theorem423','cor424_repaired','cor51','cor52','cor53']:
                self.assertTrue(r[key],(sizes,key))
        self.assertEqual(audit((2,2))['original424_failures'],228)

    def test_matching_equals_explicit_relabeling(self):
        # Independent coordinate formula: relabel actions to common A_0 labels,
        # permute coordinates, then return to local labels.
        sizes=(2,2,2)
        for m in matchings(sizes):
            for p in permutations(range(3)):
                for s in product(range(2),repeat=3):
                    labels=tuple(m[i].index(s[i]) for i in range(3))
                    expected=[None]*3
                    for i in range(3): expected[p[i]]=m[p[i]][labels[i]]
                    self.assertEqual(action(matching_element(m,p),s),tuple(expected))

    def test_payoff_relabeling_weak_anonymity(self):
        sizes=(2,2,2)
        profiles=tuple(product(range(2),repeat=3))
        for m in matchings(sizes):
            group=tuple(matching_element(m,p) for p in permutations(range(3)))
            values=partition(sizes,group,True)
            game={s:tuple(values[3*k+i] for i in range(3)) for k,s in enumerate(profiles)}
            # Also exercise a nontrivial player permutation in the isomorphism.
            f=((1,2,0),tuple(tuple(component.index(a) for a in range(2)) for component in m))
            self.assertTrue(weakly_anonymous(relabel_game(game,f),sizes))

    def test_minimal_distinct_constants(self):
        # Singleton strategies already refute the printed Cor4.24.
        sizes=(1,1)
        g=bijections(sizes)
        self.assertTrue(satisfies((0,1),partition(sizes,g,True)))
        self.assertFalse(satisfies((0,1),partition(sizes,g)))

    def test_weak_need_not_be_standard(self):
        # n=3 opponent-anonymous own-action utilities with player constants.
        sizes=(2,2,2)
        values=tuple(10*i+s[i] for s in product(range(2),repeat=3) for i in range(3))
        gs=[tuple(matching_element(m,p) for p in permutations(range(3))) for m in matchings(sizes)]
        self.assertTrue(any(satisfies(values,partition(sizes,g,True)) for g in gs))
        # Every player's payoff range is disjoint, forbidding player-moving autos.
        self.assertTrue(all(not satisfies(values,partition(sizes,[g])) for g in bijections(sizes) if g[0] != (0,1,2)))

    def test_partition_implication_witness(self):
        p=(0,0,2)
        q=(0,1,1)
        self.assertFalse(implies(p,q))
        self.assertTrue(satisfies(p,p))
        self.assertFalse(satisfies(p,q))


if __name__ == '__main__': unittest.main()

class FailedStrengtheningTests(unittest.TestCase):
    def test_matching_pennies_has_transitive_but_no_strategy_trivial_subgroup(self):
        sizes=(2,2)
        values=tuple((1 if s[0]==s[1] else -1)*(-1 if i else 1)
                     for s in product(range(2),repeat=2) for i in range(2))
        autos=tuple(g for g in bijections(sizes) if satisfies(values,partition(sizes,[g])))
        self.assertEqual(len(autos),4)
        self.assertEqual({g[0][0] for g in autos},{0,1})
        self.assertFalse(any(strategy_trivial(h) and {g[0][0] for g in h}=={0,1} for h in subgroups(autos)))
