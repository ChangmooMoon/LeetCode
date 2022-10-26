nums - integer arr
k - integer
연속된 subarray의 사이즈가 2이상. 조건 - 그 합이 k의 배수이면 true/ otherwise false
​
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
​
O(N^2) 미만으로 풀어야함.
Hashmap으로 O(N) 카운트하면서 나머지값 체크
​
​