class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap -> grouping pattern
        
        anagram_map = {}
    
        for s in strs:
            sorted_str = ''.join(sorted(s))
        
            # Have to add original string to the group

            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            anagram_map[sorted_str].append(s)
    
        return list(anagram_map.values())
