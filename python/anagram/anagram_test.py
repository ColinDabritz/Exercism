try:
    from anagram import Anagram, cannonize
except ImportError:
    raise SystemExit('Could not find anagram.py. Does it exist?')

import unittest

class AnagramTests(unittest.TestCase):
    def test_no_matches(self):
        self.assertEqual(
            [],
            Anagram('diaper').match('hello world zombies pants'.split())
        )

    def test_detect_simple_anagram(self):
        self.assertEqual(
            ['tan'],
            Anagram('ant').match('tan stand at'.split())
        )

    def test_detect_multiple_anagrams(self):
        self.assertEqual(
            ['stream', 'maters'],
            Anagram('master').match('stream pigeon maters'.split())
        )

    def test_does_not_confuse_different_duplicates(self):
        self.assertEqual(
            [],
            Anagram('galea').match(['eagle'])
        )

    def test_eliminate_anagram_subsets(self):
        self.assertEqual(
            [],
            Anagram('good').match('dog goody'.split())
        )

    def test_detect_anagram(self):
        self.assertEqual(
            ['inlets'],
            Anagram('listen').match('enlists google inlets banana'.split())
        )

    def test_multiple_anagrams(self):
        self.assertEqual(
            'gallery regally largely'.split(),
            Anagram('allergy').match('gallery ballerina regally clergy largely leading'.split())
        )

    def test_anagrams_are_case_insensitive(self):
        self.assertEqual(
            ['Carthorse'],
            Anagram('Orchestra').match('cashregister Carthorse radishes'.split())
        )

    def test_same_word_isnt_anagram(self):
        self.assertEqual(
            [],
            Anagram('banana').match(['banana'])
        )

    # my tests
    def test_cannonize_matches_same_twice(self):
        self.assertEqual(
            cannonize("word"),
            cannonize("word"))

    def test_cannonize_handles_case(self):
        self.assertEqual(
            cannonize("wOrd"),
            cannonize("WoRd"))


    def test_cannonize_ignores_punctuation(self):
        self.assertEqual(
            cannonize("it's"),
            cannonize("its"))

        self.assertEqual(
            cannonize(")@(&#%)(@&#Compound-Word*@(#(&!)"),
            cannonize("'(@@@)'Compou'ndWord&&&&&&&&&$$@()@#"))

    def test_cannonize_repeated_letters(self):
        self.assertNotEqual(
            cannonize("aaaaab"),
            cannonize("aab"))

        self.assertEqual(
            cannonize("aaab"),
            cannonize("aaab"))

    def test_cannonize_whitespace(self):
        self.assertEqual(
            cannonize("anagram"),
            cannonize("nag a ram"))

        self.assertEqual(
            cannonize(" a   b   c     "),
            cannonize("abc"))

        self.assertEqual(
            cannonize("""a
            b
            c d   e   f     
            """),
            cannonize("abcdef"))


    def test_is_anagram_no_match_to_self(self):
        self.assertFalse(Anagram("word").is_anagram("word"))

    def test_is_anagram_matches_jumble(self):
        self.assertTrue(Anagram("word").is_anagram("rowd"))

    def test_is_anagram_matches_classic_phrase(self):
        self.assertTrue(Anagram("anagram").is_anagram("nag a ram"))

    def test_is_anagram_no_match(self):
        self.assertFalse(Anagram("one").is_anagram("two"))


if __name__ == '__main__':
    unittest.main()
