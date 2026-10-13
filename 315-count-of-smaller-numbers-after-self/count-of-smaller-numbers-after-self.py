
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid

            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    counts[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i < mid:
                counts[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1

            arr[left:right] = temp

        merge_sort(0, n)
        return counts

        