class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for start in range(len(s)):
            hashset = set()
            for i in range(start, len(s)):
                if s[i] not in hashset:
                    hashset.add(s[i])
                    longest = max(longest, len(hashset))
                else:
                    break

        return longest

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
