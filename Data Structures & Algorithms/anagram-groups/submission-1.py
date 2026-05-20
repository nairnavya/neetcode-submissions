class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        output = []
        for string in strs:
            if ''.join(sorted(string)) not in words:
                words[''.join(sorted(string))] = [string]
            else:
                words[''.join(sorted(string))].append(string)
        
        for word in words:
            output.append(words[word])

        return output