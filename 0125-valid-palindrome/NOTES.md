0. 대소문자, non-alphanumeric characters 전처리
- lower()
- isalnum()
- re.sub('[^[a-zA-Z0-9]', '', s)
(https://wikidocs.net/4308 - 정규표현식 참고)
​
- 나의 풀이 - start, end 투 포인터를 한칸씩 이동하면서 서로 비교
​
1. 리스트로 변환해서 푸는 방식
```
strs = []
for ch in s:
if ch.isalnum():
strs.append(ch.lower())
while len(strs) > 1:
if strs.pop(0) != strs.pop():
return False
return True
```
​
2. 덱으로 최적화하는 방식
```
strs: Deque = collections.deque()
for ch in s:
if ch.isalnum():
strs.append(ch.lower())
while len(strs) > 1:
if strs.popleft() != strs.pop():
return False
```
3. 슬라이싱
```
s = s.lower()
s = resub('[^a-z0-9]', '', s)
return s == s[::-1] # 문자열 뒤집기
```
​