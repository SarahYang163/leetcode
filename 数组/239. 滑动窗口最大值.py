# https://leetcode.cn/problems/sliding-window-maximum/
import collections
from typing import List
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
#
# 解释过程中队列中都是具体的值，方便理解，具体见代码。
# 初始状态：L=R=0,队列:{}
# i=0,nums[0]=1。队列为空,直接加入。队列：{1}
# i=1,nums[1]=3。队尾值为1，3>1，弹出队尾值，加入3。队列：{3}
# i=2,nums[2]=-1。队尾值为3，-1<3，直接加入。队列：{3,-1}。此时窗口已经形成，L=0,R=2，result=[3]
# i=3,nums[3]=-3。队尾值为-1，-3<-1，直接加入。队列：{3,-1,-3}。队首3对应的下标为1，L=1,R=3，有效。result=[3,3]
# i=4,nums[4]=5。队尾值为-3，5>-3，依次弹出后加入。队列：{5}。此时L=2,R=4，有效。result=[3,3,5]
# i=5,nums[5]=3。队尾值为5，3<5，直接加入。队列：{5,3}。此时L=3,R=5，有效。result=[3,3,5,5]
# i=6,nums[6]=6。队尾值为3，6>3，依次弹出后加入。队列：{6}。此时L=4,R=6，有效。result=[3,3,5,5,6]
# i=7,nums[7]=7。队尾值为6，7>6，弹出队尾值后加入。队列：{7}。此时L=5,R=7，有效。result=[3,3,5,5,6,7]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if k > len(nums):
            return res
        dq = collections.deque()  # 放的是索引
        l, r = 0, 0
        while r < k - 1:#前k-1个数只用维护栈内元素，按照从左到右从大到小排列，当前元素大于最右边的元素，依次弹出栈，知道遇到比他大的然后当前元素入栈，不用维护res和l
            while len(dq) != 0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            r += 1
        while r < len(nums):#窗口开始形成，要开始维护res辣，并且l、r指针每次都要加1，当前元素判断入栈之后，要判断最左边的元素还在有效期没（通过l、r判断滴），过期就弹出去，然后res去最左边也就是最大的元素
            while len(dq) != 0 and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            while dq[0] < l or dq[0] > r:
                dq.popleft()
            res.append(nums[dq[0]])
            r += 1
            l += 1
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
