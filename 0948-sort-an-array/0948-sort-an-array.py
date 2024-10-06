class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, l, mid, r):
            lc = mid - l + 1
            rc = r - mid

            L, R = [0] * lc, [0] * rc
            for i in range(lc):
                L[i] = a[l + i]
            for j in range(rc):
                R[j] = a[mid + 1 + j]
            
            i, j, k = 0, 0, l
            while i < lc and j < rc:
                if L[i] <= R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1
            
            while i < lc:
                a[k] = L[i]
                i += 1
                k += 1

            while j < rc:
                a[k] = R[j]
                j += 1
                k += 1

        
        def mergesort(a, l, r):
            if l < r:
                mid = l + (r - l) // 2
                mergesort(a, l, mid)
                mergesort(a, mid + 1, r)
                merge(a, l, mid, r)
        

        mergesort(nums, 0, len(nums) - 1)
        return nums
