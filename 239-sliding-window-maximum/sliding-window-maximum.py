from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Record the maximum for the current window
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
        