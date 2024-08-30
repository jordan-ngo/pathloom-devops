import unittest
from permutations import permutation_func
class TestPermutations(unittest.TestCase):

    # Test three elements
    def test_three_elements(self):
        expected = [('apple', 'banana', 'orange'), 
                    ('apple', 'orange', 'banana'), 
                    ('banana', 'apple', 'orange'), 
                    ('banana', 'orange', 'apple'), 
                    ('orange', 'apple', 'banana'), 
                    ('orange', 'banana', 'apple')]

        actual = permutation_func(['apple', 'banana', 'orange'])
        self.assertEqual(sorted(actual), sorted(expected))

# Debugging Purposes:
#
#        print("Actual permutations:")
#        for perm in actual:
#            print(perm)
#
#        print("\nExpected permutations:")
#        for perm in expected:
#            print(perm)

    # Test two elements
    def test_two_elements(self):
        
        expected = [('apple', 'banana'),
                    ('banana', 'apple')]

        actual = permutation_func(['apple', 'banana'])
        self.assertEqual(sorted(actual), sorted(expected))

    # Test with a list of strings
    def test_one_element(self):
        
        expected = [('apple',)]

        actual = permutation_func(['apple'])
        self.assertEqual(sorted(actual), sorted(expected))

    # Test with an empty list
    def test_empty(self):
       
        expected = [()] 

        actual = permutation_func([])
        self.assertEqual(sorted(actual), sorted(expected))

    # Test duplicate elements
    def test_duplicate_elements(self):
    
        expected = [('apple', 'apple')]

        actual = permutation_func(['apple', 'apple'])
        self.assertEqual(sorted(actual), sorted(expected))

    # Test two duplicate elements
    def test_two_duplicates(self):
        
        expected = [('apple', 'apple', 'banana'),
                    ('apple', 'banana', 'apple'),
                    ('banana', 'apple', 'apple')]

        actual = permutation_func(['apple', 'apple', 'banana'])
        self.assertEqual(sorted(actual), sorted(expected))

# TO DO BELOW:

    # Test multiple elements and duplicates
    def test_large_list(self):
        expected = [('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),
                    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'i'),
                    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'h', 'j'),
                    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'h'),
                    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'h', 'i')]

        actual = permutation_func(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], limit=5)
        self.assertEqual(sorted(actual), sorted(expected))

    # Test multiple elements and duplicates
    def test_large_list_duplicates(self):
        expected = [('a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'),
                    ('a', 'a', 'b', 'b', 'c', 'd', 'c', 'd'),
                    ('a', 'a', 'b', 'b', 'c', 'd', 'd', 'c'),
                    ('a', 'a', 'b', 'b', 'd', 'c', 'c', 'd'),
                    ('a', 'a', 'b', 'b', 'd', 'c', 'd', 'c'),
                    ('a', 'a', 'b', 'b', 'd', 'd', 'c', 'c'),
                    ('a', 'a', 'b', 'c', 'b', 'c', 'd', 'd'),
                    ('a', 'a', 'b', 'c', 'b', 'd', 'c', 'd'),
                    ('a', 'a', 'b', 'c', 'b', 'd', 'd', 'c'),
                    ('a', 'a', 'b', 'c', 'c', 'b', 'd', 'd')]

        actual = permutation_func(['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], limit=31)
        self.assertEqual(sorted(actual), sorted(expected))

    # Test multiple elements and duplicates
    def test_mixed_elements(self):
        # converted to set due to sort() function complexities
        # and used a set instead to solve permutations ordering
        # differing and throwing errors when comparing actual and expected
        actual = set(permutation_func(['apple', 2, 3.563, 1j]))
        expected = set([(2, 1j, 'apple', 3.563),
                        ('apple', 2, 3.563, 1j),
                        (2, 'apple', 1j, 3.563),
                        (1j, 3.563, 2, 'apple'),
                        (1j, 'apple', 3.563, 2),
                        ('apple', 3.563, 2, 1j),
                        ('apple', 3.563, 1j, 2),
                        (3.563, 2, 1j, 'apple'),
                        (3.563, 1j, 2, 'apple'),
                        (3.563, 2, 'apple', 1j),
                        (1j, 2, 'apple', 3.563),
                        (3.563, 1j, 'apple', 2),
                        (2, 3.563, 1j, 'apple'),
                        ('apple', 1j, 3.563, 2),
                        (3.563, 'apple', 2, 1j),
                        (1j, 3.563, 'apple', 2),
                        (2, 3.563, 'apple', 1j),
                        (2, 1j, 3.563, 'apple'),
                        (1j, 2, 3.563, 'apple'),
                        (1j, 'apple', 2, 3.563),
                        ('apple', 2, 1j, 3.563),
                        (2, 'apple', 3.563, 1j),
                        (3.563, 'apple', 1j, 2),
                        ('apple', 1j, 2, 3.563)])

        self.assertEqual(actual, expected)

    # Test mixed elements and duplicates
    def test_large_mixed_duplicates_list(self):
        actual = set(permutation_func([3.563, 1j, 1j, 'apple', 2]))

        expected = set(([(3.563, 'apple', 1j, 1j, 2),
                         (1j, 1j, 3.563, 'apple', 2),
                         (1j, 2, 3.563, 'apple', 1j),
                         (1j, 'apple', 3.563, 2, 1j),
                         (1j, 2, 'apple', 1j, 3.563),
                         (3.563, 1j, 2, 'apple', 1j),
                         (1j, 3.563, 1j, 2, 'apple'),
                         (3.563, 1j, 2, 1j, 'apple'),
                         (3.563, 1j, 1j, 2, 'apple'),
                         (1j, 3.563, 1j, 'apple', 2),
                         (1j, 'apple', 1j, 2, 3.563),
                         (1j, 'apple', 2, 1j, 3.563),
                         ('apple', 1j, 3.563, 2, 1j),
                         ('apple', 1j, 2, 1j, 3.563),
                         (1j, 2, 3.563, 1j, 'apple'),
                         (1j, 2, 1j, 3.563, 'apple'),
                         (1j, 'apple', 3.563, 1j, 2),
                         (3.563, 'apple', 2, 1j, 1j),
                         ('apple', 1j, 3.563, 1j, 2),
                         (2, 3.563, 1j, 1j, 'apple'),
                         (3.563, 2, 'apple', 1j, 1j),
                         (3.563, 1j, 1j, 'apple', 2),
                         ('apple', 1j, 1j, 3.563, 2),
                         (2, 3.563, 1j, 'apple', 1j),
                         (3.563, 1j, 'apple', 2, 1j),
                         (1j, 1j, 2, 3.563, 'apple'),
                         ('apple', 3.563, 1j, 2, 1j),
                         (1j, 3.563, 'apple', 2, 1j),
                         ('apple', 2, 1j, 3.563, 1j),
                         (1j, 1j, 'apple', 3.563, 2),
                         (1j, 2, 1j, 'apple', 3.563),
                         ('apple', 1j, 1j, 2, 3.563),
                         (1j, 2, 'apple', 3.563, 1j),
                         (1j, 'apple', 2, 3.563, 1j),
                         ('apple', 3.563, 1j, 1j, 2),
                         (1j, 3.563, 'apple', 1j, 2),
                         ('apple', 3.563, 2, 1j, 1j),
                         ('apple', 2, 3.563, 1j, 1j),
                         (1j, 3.563, 2, 1j, 'apple'),
                         ('apple', 1j, 2, 3.563, 1j),
                         ('apple', 2, 1j, 1j, 3.563),
                         (3.563, 'apple', 1j, 2, 1j),
                         (3.563, 2, 1j, 'apple', 1j),
                         (1j, 1j, 'apple', 2, 3.563),
                         (3.563, 1j, 'apple', 1j, 2),
                         (1j, 1j, 3.563, 2, 'apple'),
                         (3.563, 2, 1j, 1j, 'apple'),
                         (1j, 1j, 2, 'apple', 3.563),
                         (1j, 'apple', 1j, 3.563, 2),
                         (1j, 3.563, 2, 'apple', 1j)]))

        print("Actual permutations:")
        for perm in actual:
            print(perm)

        print("\nExpected permutations:")
        for perm in expected:
            print(perm)

        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()

