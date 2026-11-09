class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_char_to_number = {}
        t_char_to_number = {}

        for c in s:
            if c in s_char_to_number.keys():
                s_char_to_number[c] += 1
            else:
                s_char_to_number[c] = 1
        
        for c in t:
            if c in t_char_to_number.keys():
                t_char_to_number[c] += 1
            else:
                t_char_to_number[c] = 1
        
        for c in s_char_to_number.keys():
            if c in t_char_to_number.keys() and (t_char_to_number[c] == s_char_to_number[c]):
                continue
            else:
                return False
        
        return True

            