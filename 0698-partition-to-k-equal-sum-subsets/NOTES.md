1. 문제 읽기
2. 논리적 순서
3. 필요한 자료연산 리스트업
4. 자료형, 시간복잡도, 유리한 자료구조 선택
5. 구현
6. 엣지케이스
​
given nums is int list, k is int
When made of K subsets, the sum is same
​
target값 = total // k를 만들어야됨
K: 1~16, nums[i]: 10000
​
1. K개의 서브셋 중에 하나에 원소를 넣는다 -> O(K^n) -> 4^16 = 2^32 = 42억
2. 서브셋마다 될수있는 경우의 수를 백트래킹 O(2^(kn))
​