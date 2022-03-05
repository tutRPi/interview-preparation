class Solution:
    def wordBreak(self, s: str, wordDict: list):
        memo = [None] * len(s)
        for i in reversed(range(len(s))):
            self.find_sentences(s, i, memo, wordDict)

        print([" ".join(s) for s in memo[0]])
        return [" ".join(s) for s in memo[0]]

    def find_sentences(self, s, index, memo, wordDict):
        memo[index] = []
        for word_length in range(1, len(s) - index + 1):
            word = s[index:index + word_length]
            if word in wordDict:
                if index + word_length < len(s):
                    other_sentences = memo[index + word_length]

                    for other_sentence in other_sentences:
                        sentences = [word]
                        sentences.extend(other_sentence)
                        memo[index].append(sentences)
                else:
                    memo[index].append([word])


if __name__ == "__main__":
    assert sorted(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(["cat and dog", "cats sand dog"])
    assert sorted(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    assert sorted(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) == []
