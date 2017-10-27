from collections import Counter


input()
inp_list = [int(x) for x in input().split()]
count = Counter(inp_list)
num = int(input())

out_list = [key for key, val in count.items() if val == num]
print(min(out_list))
