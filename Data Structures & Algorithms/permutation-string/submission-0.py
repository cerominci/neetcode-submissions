class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        # Edge case: If s1 is longer than s2, a permutation cannot exist
        if len_s1 > len_s2:
            return False

        # Create frequency maps for s1 and the initial window of s2
        s1_freq = [0] * 26
        window_freq = [0] * 26

        # Populate s1_freq
        for char_code in s1:
            s1_freq[ord(char_code) - ord('a')] += 1

        # Populate window_freq for the initial window (first len_s1 characters of s2)
        for i in range(len_s1):
            window_freq[ord(s2[i]) - ord('a')] += 1

        # Check if the initial window is a permutation
        if s1_freq == window_freq:
            return True

        # Slide the window across s2
        for i in range(len_s1, len_s2):
            # Add the new character entering the window
            window_freq[ord(s2[i]) - ord('a')] += 1
            # Remove the character leaving the window
            window_freq[ord(s2[i - len_s1]) - ord('a')] -= 1

            # Check if the current window is a permutation
            if s1_freq == window_freq:
                return True

        return False



        
        