class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(size, root):
            while True:
                largest = root
                left = 2 * root + 1
                right = 2 * root + 2

                if left < size and nums[left] > nums[largest]:
                    largest = left

                if right < size and nums[right] > nums[largest]:
                    largest = right

                if largest == root:
                    break

                nums[root], nums[largest] = nums[largest], nums[root]
                root = largest

        # Build a max heap.
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Move the maximum to the end, then restore the heap.
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)

        return nums
        