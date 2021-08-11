# Array

* 2차원 배열
* 부분집합 생성
* Binary Search
* Selection Algorithm
* Selection sort



# 2차원 배열

1차원 Array를 묶어놓은 Array

다차원 Array > 차원에 따라 Index를 선언

Python의 2차원 List:

```python
arr = [[0, 1, 2, 3],
       [4, 5, 6, 7]]
# row: 2, column: 4
```

2행 4열의 2차원 List



```python
N, M = map(int, input().split())
# N: row M: column
arr = [list(map(int, input().split())) for _ in range(N)]
# list... 구문은 한 행, comprehension 구문은 필요 행만큼 반복
```

```python
arr2 = [[0] * M for _ in range(N)]

# cf. the code below is not working properly (it will use shallow copy)
arr2 = [[0] * M] * N
```



## 배열 순회 (Access)

```python
for i in range(len(Array)):
    # i행
    for j in range(len(Array[i])):
        # j열
        Array[i][j] ~~~~
        # i행 j열의 data
        
for i in range(N):
    for j in range(M):
        print(Array[i][j])
```



### 열 우선 순회

```python
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j]
```



### 지그재그 순회

```python
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j) * (i % 2)]
        
        # M-1-j // j
        # i % 2: 홀짝판정
```



### Search Array w/ Delta

어떻게 4방향의 인접 배열 요소를 탐색할까?

(i-1 i+1 j-1 j+1)



```
dx[] <- [0, 0, -1, 1]
dy[] <- [-1, 1, 0, 0] # 좌우상하

for x in range (len(ary)):
	for y in range(len(ary[x])):
		for I in range(4):
			testX <- x + dx[mode]
			testY <- y + dy[mode]
			test(ary[testX][testY])
```



```python
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            # 가장자리면 어떡해?
            if 0 <= ni < N and 0 <= nj < M:
                print(arr[ni][nj])           
```

```python
for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [1-, 0]]:
            ni = i + di
            nj = j + dj
            
            if 0 <= ni < N and 0 <= nj < M:
                arr[ni][nj]
```



### 전치 행렬

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            # 반쪽...!
            # 만일 이 과정을 생략한다면...? 도로 제자리로 돌겠지
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



## 부분집합의 합 (Subset Sum)

cf. [-7, -3, -2, 5, 8]에서, 합이 0이 되는 부분집합이 있을까? 있다면 몇 개일까?



* 완전검색 기법: 어떻게 부분집합을 만들까
* n elements: 2^n개의 부분집합이 생긴다
  * 해당 element가 있는 경우 없는 경우 두 가지 & n개

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

```python
arr = [1, 2, 3, 4]
#### bit ####
	for p in range(4):
		if bit[p]:
       		print(arr[p], end= ' ')
    print()
```

### Bit Operator (비트 연산자)

`&` `|` `<<` `>>` 비트 단위의 AND, OR, 좌/우 이동

뭐하러 [0, 0, 0, 0]...? 비트 단위로 저장해보자

```python
1 << n : 2^n, 원소가 n개일 때의 모든 부분집합의 수
# bit 1을 n번 밀어

# ex
1 << 3 # 1이 8(2^3)로
```



비트 사이에 AND와 OR 연산은 같은 비트 자리끼리만 수행됨

ex. AND

0 1 1 0 0 1

1 0 1 1 0 0

: 0 0 1 0 0 0

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        # n만큼 bit를 비교할 것임
        if i & (1<<j):
            # i의 j번째 비트가 1이라면 arr[j] 출력
            print(arr[j], end = ", ")
	print()
print()
```

비트 연산자n의 갯수가 바뀔 때 부분집합 문제를 유연하게 풀 수 있음



# Search: 검색

"저장된 자료 중에서 원하는 항목을 찾는 작업"

= 목적하는 탐색 키를 가진 항목을 찾는 것

* 순차검색
* 이진검색
* 해시



## Sequential Search 순차검색

일렬로 되어 있는 자료를 순서대로 검색하는 방법

가장 간단, 직관적

배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용

구현이 쉽지만, 검색 대상의 수가 많다면 수행시간이 급격히 증가하여 비효율적

* 대상이 정렬되지 않은 경우
* 대상이 정렬된 경우



### 정렬되어 있지 않은 경우

대상 key값 == 원소 key값 찾아 앞에서부터....

```python
def search(A, N, key):
    for i in range(N):
        if A[i] == key:
            return i
        	# return True
    return -1
	# return False
```

찾고자 하는 원소의 순서에 따라 비교회수가 결정됨

시간 복잡도: O(n)

주의사항: and 문으로 인덱스 유효성 / 키값검사를 동시에 한다면, and 문의 앞부분을 유효성 검사로 해야 할 것 (먼저 검사하니까...!)



### 정렬된 경우

찾는 값보다 큰 값이 등장: 아 없구나: 종료

시간 복잡도: O(n) (여전히...)

하지만 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다.



```
def seqSearch(a n, key):
    i <- 0
    while 1 < n and a[i] < key:
    	# 다음으로
    	i <- i+1
  	
  	if i < n and a[i] = key:
    		# 맞는 키를 찾아 나온 경우: 성공
    		return i
    else:
    	# 지나가거나, 마지막 인덱스까지 다 뒤졌거나...
    	return -1
```



## Binary Search: 이진 검색

자료 **가운데에 있는 항목의 키 값**과 비교

반드시 정렬된 상태여야.

cf. 만일 자료에 추가삭제가 이뤄진다면 난감...

과정

* 중앙 원소 고르기
* 값 비교
* 작으면 왼쪽 반에서 다시, 크면 오른쪽 반에서 다시
* 찾을 때까지 1~3 반복

새 구간을 형성할 수 없다면 실패



* 검색범위의 시작점과 종료점을 이용하기
* 자료에 삽입이나 삭제가 발생했을 때 배열을 항상 정렬상태로 유지하는 작업이 필요

```
def binSearch(a, key)
	start <- 0
	end <- length(a) - 1
	while start <= end:
	# '=': 둘이 같더라도, 그 값이 찾는 값인가 한 번 확인은 해야 하니까
		middle = (start + end) // 2
		if a[middle] == key:
			return True
			# return middle
		elif a[middle] > key:
			end = middle - 1
		else:
			start = middle + 1
	return False
```







----

별첨

python에서의 a <= b <= c 비교

다른 언어에서는 a <= b True False 값을 <=와 비교하는 사태가 발생하기도 함



