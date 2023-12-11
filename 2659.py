a, b, c, d = input().split()
clock_num = min(int(a+b+c+d), int(b+c+d+a), int(c+d+a+b), int(d+a+b+c))

clock_nums = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                nums = [
                    i*1000+j*100+k*10+l,
                    j*1000+k*100+l*10+i,
                    k*1000+l*100+i*10+j,
                    l*1000+i*100+j*10+k,
                ]
                clock_nums.append(min(nums))
clock_nums = list(set(clock_nums))
clock_nums.sort()
print(clock_nums.index(clock_num) + 1)
                
                