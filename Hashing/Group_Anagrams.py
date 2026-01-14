"""
LeetCode 49: Group Anagrams
Difficulty: Medium

Approach:
- Use a hashmap (defaultdict)
- Sort each string and convert it to a tuple to use as a key

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

from collections import defaultdict


def groupAnagrams(strs):
    result = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        result[key].append(s)
    return list(result.values())

