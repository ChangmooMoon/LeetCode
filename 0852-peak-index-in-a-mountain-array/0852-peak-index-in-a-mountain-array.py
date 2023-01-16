class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        L, R = 0, len(arr) - 1 # 0 ~ L,R ~ N-1
        
        while L <= R:
            mid = (L + R) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                L = mid + 1
            elif arr[mid - 1] > arr[mid]:
                R = mid - 1
        return -1
            
        
        
        
        
        
        
        
'''
1. 문제 읽기
2. 논리적 순서
3. 필요한 자료연산 리스트업
4. 자료형, 시간복잡도, 유리한 자료구조 선택
5. 구현
6. 엣지케이스

1. 산을 배열로 표현함. 꼭대기 지점 i가 있어서 a[0]~a[i] 까지는 올라가고, a[i]~a[n - 1]까지는 내려감
i를 리턴하면 됨. logN 시간이 걸려야함. 
2. 이분 탐색으로 찾아내면 될 것 같다. 
3. L, R 지점을 양끝으로 해서 이분탐색
'''