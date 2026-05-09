class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for el in strs:
            dict["".join(sorted(el))].append(el)
        return list(dict.values())


        