from anagrams import anagramms


assert anagramms("abcba", "abc") == [0, 2]
assert anagramms("aaa", "a") == [0, 1, 2]
assert anagramms("abc cba xabcd", "abc") == [0, 4, 9]
