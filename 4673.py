def self_num(number):
    sum_val = number
    for n in str(number):
        sum_val += int(n)
    return sum_val

nums = list(range(1, 10001))
for i in range(1, 10001):
    if self_num(i) in nums:
        nums.remove(self_num(i))
        
for n in nums:
    print(n) 
    

    
