class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word))) # Append length of the word
            res.append("#")             # Append separator
            res.append(word)            # Append the word itself
        return "".join(res) 


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0  # Pointer to the current position in the encoded string

        while i < len(s):
            # 1. Read the length
            length_str = ""
            # Find the '#' delimiter
            j = i
            while j < len(s) and s[j].isdigit():
                length_str += s[j]
                j += 1
            length = int(length_str)

            # 2. Advance pointer past the length and the '#'
            # j is currently at '#'
            i = j + 1 # Move past '#' to the start of the word

            # 3. Extract the word
            word = s[i : i + length]
            decoded_strs.append(word)

            # 4. Advance pointer past the extracted word
            i += length

        return decoded_strs
            

