class Solution:
    def isMatch(self, message: str, decoder_key: str) -> bool:
        def match_helper(msg_idx, pat_idx):
            if msg_idx == len(message) and pat_idx == len(decoder_key):
                return True
            if pat_idx < len(decoder_key) and decoder_key[pat_idx] == '*':
                return (match_helper(msg_idx, pat_idx + 1) or
                        (msg_idx < len(message) and match_helper(msg_idx + 1, pat_idx)))
            if msg_idx < len(message) and pat_idx < len(decoder_key) and \
               (decoder_key[pat_idx] == '?' or decoder_key[pat_idx] == message[msg_idx]):
                return match_helper(msg_idx + 1, pat_idx + 1)
            return False

        return match_helper(0, 0)

if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aa", "a"))        
    print(solution.isMatch("aa", "*"))        
    print(solution.isMatch("cb", "?a"))       
    print(solution.isMatch("abc", "a*?"))     
