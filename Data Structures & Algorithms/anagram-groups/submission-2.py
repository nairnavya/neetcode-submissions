class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        seen_map = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in seen_map:
                seen_map[key].append(s)
            else:
                seen_map[key] = [s]

        for sorted_list in seen_map:
            output.append(seen_map[sorted_list])

        return output


