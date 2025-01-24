class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars, left, longest = set(), 0, 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
