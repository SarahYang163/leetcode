# def calculate_tp99(data: list):
#     sorted_data = sorted(data)
#     l = len(sorted_data)
#     out_data = int(l * 0.01)
#     res_data = sorted_data[:out_data]
#     tp99 = max(res_data)
#     a=dict()
#     return tp99
#
#
# def climb_stair(n: int) -> int:
#     if n <= 2:
#         return n
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]
#
#
# print(climb_stair(5))

import sys

print('Hello,World!');
arr = [3, 5, 2, 1, 5, 6, 5, 4, 3]
arr_tmp = []
for a in arr:
    if a not in arr_tmp:
        arr_tmp.append(a)
print(arr_tmp)


def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pre = arr[0]
    left = [x for x in arr if x < pre]
    middle = [x for x in arr if x == pre]
    right = [x for x in arr if x > pre]

    return quicksort(left) + middle + quicksort(right)


print(quicksort(arr_tmp))
