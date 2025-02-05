class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_idx, second_idx, num_diffs = 0, 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    first_idx = i
                else:
                    second_idx = i
        return(
            s1[first_idx] == s2[second_idx] and s1[second_idx] == s2[first_idx]
        )
