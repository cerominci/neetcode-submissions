class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_s = len(s)
        len_t = len(t)

        # If t is longer than s, no valid window can exist
        if len_t > len_s:
            return ""

        # Frequency map for characters in t
        t_freq = collections.Counter(t)
        
        # Track the number of unique characters from t that are matched
        # This is a good alternative to `matched_chars == len_t`
        # and handles duplicate characters in t more robustly.
        # It counts how many distinct characters in t have their frequency requirement met.
        # We use `required_chars` to count how many unique characters from `t` (e.g., 'a', 'b', 'c')
        # we still need to match based on their frequencies.
        required_chars = len(t_freq) 
        
        # `formed_chars` counts how many unique characters in the current window
        # match the frequency requirement in `t_freq`.
        formed_chars = 0

        # Frequency map for characters in the current window
        window_freq = collections.defaultdict(int)

        # Variables to store the result
        min_length = float('inf')
        min_start_index = 0

        left = 0
        for right in range(len_s):
            char_right = s[right]
            window_freq[char_right] += 1

            # If the current character is one we need and its frequency in the window
            # now meets or exceeds the requirement in t_freq, increment formed_chars.
            if char_right in t_freq and window_freq[char_right] == t_freq[char_right]:
                formed_chars += 1

            # Shrink the window when all required characters are found
            while formed_chars == required_chars:
                # Update minimum window
                current_window_length = right - left + 1
                if current_window_length < min_length:
                    min_length = current_window_length
                    min_start_index = left

                char_left = s[left]
                window_freq[char_left] -= 1

                # If the character leaving the window was one that was required
                # and its frequency now drops below the requirement, decrement formed_chars.
                if char_left in t_freq and window_freq[char_left] < t_freq[char_left]:
                    formed_chars -= 1
                
                left += 1

        if min_length == float('inf'):
            return ""
        else:
            return s[min_start_index : min_start_index + min_length]    

        