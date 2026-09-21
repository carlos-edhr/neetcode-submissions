from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            vector = [0] * 26
            for ch in word:
                vector[ord(ch) - ord("a")] += 1
            key = tuple(vector)
            groups[key].append(word)
        return list(groups.values())