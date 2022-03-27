class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_indices = {}
        for i, word in enumerate(strs):
            sorted_chars = sorted(list(word))
            sorted_word = "".join(sorted_chars)
            if sorted_word not in sorted_word_indices:
                sorted_word_indices[sorted_word] = [i]
            else:
                sorted_word_indices[sorted_word].append(i)

        results = []
        for v in sorted_word_indices.values():
            words = []
            for i in v:
                words.append(strs[i])
            results.append(words)
        return results