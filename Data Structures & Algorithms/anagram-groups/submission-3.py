class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for string in strs:
            if ("".join(sorted(string)) in anagram_map):
                anagram_map["".join(sorted(string))].append(string)
            else:
                anagram_map["".join(sorted(string))] = [string]
        

        output = []
        for anagram in anagram_map:
            output.append(anagram_map[anagram])

        return output
        
        
