import itertools

input()
nums = [_ for _ in list(map(int,input().split()))]
nums_combs = itertools.permutations(nums)
# sum_list=[]
# for ncs in nums_combs:
#     abs_list=[abs(ncs[i] - ncs[i+1]) for i in range(len(ncs)-1)]
#     sum_list.append(sum(abs_list))
sum_list = [sum([abs(ncs[i] - ncs[i+1]) for i in range(len(ncs)-1)]) for ncs in nums_combs]
print(max(sum_list))
