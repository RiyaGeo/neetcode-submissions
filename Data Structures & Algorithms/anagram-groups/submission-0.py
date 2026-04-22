class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)
        for s in strs:
            strings["".join(sorted(s))].append(s)
        return list(strings.values())

            


            
        