class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for s in strs:
            output[tuple(sorted(s))].append(s)
        return output.values()
        