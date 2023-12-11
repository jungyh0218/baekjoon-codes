N = int(input())

def is_palindrome(sentence, mismatch):
    left_idx = 0
    right_idx = len(sentence) - 1
    while(left_idx < right_idx):
        if sentence[left_idx] == sentence[right_idx]:
            left_idx += 1
            right_idx -= 1
        else:
            if mismatch == True:
                return 2 # Non-palindrome
            else:
                mismatch = True
                case1 = is_palindrome(sentence[left_idx+1:right_idx+1], mismatch)
                case2 = is_palindrome(sentence[left_idx:right_idx], mismatch)
                if case1 == 0 or case2 == 0:
                    return 1
    return 0
            

for _ in range(N):
    print(is_palindrome(input(), False))
    