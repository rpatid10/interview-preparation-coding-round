from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs) :
        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)

        return list(anagrams.values())


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))