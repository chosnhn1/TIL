# Index

Recursion

Combinatorial Problems

Greedy Algorithms



# Iteration and Recursion



## Iteration

* Initialize: 초기화
* Check Control Expression: 조건검사
  * 반복을 수행하게 되는 조건을 검사
* Action: 명령문의 실행
* Loop Update: 업데이트
  * 무한루프가 되지 않도록 조건이 False가 되게 설정



* Pre-test loop
* Post-test loop



### Selection Sort w/ Iteration 

```python
def SelectionSort(A):
    n = len(A)
    
    for i in range(0, n-1):
        minI = i
        for j in range(i + 1, n):			# n-1까지
            if A[j] < A[minI]:
                minI = j
        A[minI], A[i] = A[i], A[minI]
```



## Recursion

Recursive Algorithm

Parts of Recursion

* Basis case
* Inductive Case



### Recursive Function

함수 내부에서 직/간접적으로 자신을 호출하는 함수

일반적으로 재귀적 정의를 이용해 구현

기본 부분과 유도 부분으로 구성

반복구조에 비해 간결, 이해하기 쉬움

함수 호출은 프로그램 메모리 구조에서 스택을 사용

반복적 스택 사용, 따라서 메모리 사용량 및 성능에서 불리



### Example: Factorial

* Basis Rule: if N <= 1, n = 1

* Inductive Rule: if N > 1, n! = n * (n-1)!

* n!에 대한 재귀함수

  * ```
    def fect(n):
        if n <= 1:					// Basis Part
            return 1
        else:
            return n * fact(n-1)	// Inductive Part
    ```



참고:

좀 더 일반적인 재귀 함수의 형태는 종료 시점 k를 주는 것

(factorial은 종료 시점이 고정된 형태이기 때문에)

```
def f(n, k):
	if n == k:
		return
	else:
		return f(n+1, k)
```



## Which one: Iteration or Recursion?

재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스러움

반면 재귀적 알고리즘은 반복 알고리즘보다 더 많은 메모리와 연산이 필요

입력되는 값 n이 커질수록, 재귀 알고리즘은 반복에 비해 비효율적





#### 

|                    | Recursion      | Iteration |
| ------------------ | -------------- | --------- |
| 종료               | Base Case      | Condition |
| 수행시간           | Slow           | Fast      |
| Memory Space Usage | Big            | Small     |
| Code Length        | Short,         | Long      |
| Code Structure     | if ... else    | for while |
| Infinite Loop      | Stack Overflow | CPU 100%  |

```
// Recursion
def power_of_2(k):
	if k == 0:
		return 1
	else
		return 2 * power_of_2(k-1)
```

```
// Iteration
def power_of_2(k):
	i = 0
	power = 1
	while i < k:
		power = power * 2
		i = i + 1
	return power
```







# 완전 검색 기법

## Example: Baby-gin Game

Brute-force

* 대부분 문제에 적용 가능
* 상대적으로 빠른 시간에 알고리즘 설계가 가능
* 문제에 포함된 자료의 크기가 작다면 유용
* 학술, 교육적 목적에서 알고리즘의 효율성 판단 척도로 사용



* Brute-force in Sequential Search

* 키 값을 찾기 위해 첫번째 자료부터 비교

* ```
  def SeqSearch(A[0 .. n], k):
  	A[n] = k
  	i = 0
  	while A[i] != k:
  		i ++
  	if i < n:
  		return i		# search success
  	else:
  		return -1		# search fail
  ```

* 



완전 검색 as good starting point:

* 모든 경우의 수를 생성하고 테스트
* 느린 수행 속도, but 해답을 찾을 확률 높음
* 이를 기반으로 Greedy Algorithm, DP를 이용해 효율적 알고리즘을 찾을 수 있다
* 주어진 문제를 풀 때, 우선 완전 검색으로 접근하고 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 좋다



## Example 2: Tour





# Combinatorial Problems

## Permutation

순서화된 요소들의 집합에서 최선의 방법을 찾는 문제들

i.e. Traveling Salesman Problem (TSP)

N개의 요소들에 대해 n!개의 순열들이 존재

12! = 479,001,600

n > 12인 경우 경우의 수가 너무 많음



단순하게 순열을 생성하는 예

```
for i1 in 1 -> 3:
	for i2 in 1 -> 3:
		if i2 != i1:
			for i3 in 1 -> 3:
				if i3 != i1 and i3 != i2:
					print(i1, i2, i3)
```



재귀 호출을 통한 순열 생성

```
def perm(n, k):
	if k == n:
		print array
	else:
		for i in k -> n-1:
			p[k] <-> p[i]
			perm(n, k+1)
			p[k] <-> p[i]
```



참고... 사전 순으로 만들기

a [1, 2, 3]

u [0, 0, 0]: 사용된 숫자들을 저장할 배열

왼쪽부터 사용하지 않은 숫자를 찾아 표시하고, 숫자를 복사

k = 0

p [1, ]

a [1, 0, 0]

k = 1

p[1, 2, ]

a [1, 1, 0]

k = 2

p[1, 2, 3]

a[1, 1, 1]

k = 3:

return



```
def perm(n, k):
	if (k == n): print_arr()
	else:
		for i : 0 -> n-1:
```



sample code

```python
def f(n, m, k):
	if n == k:
		print(p)
    else:
        for i in range(m):
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                f(n, m, k+1)
                u[i] = 0

p = [0, 0, 0]
arr = [1, 2, 3, 4, 5]
u = [0, 0, 0, 0, 0]
f(3, 3, 0)			# mPn, k번째를 결정
```



## 부분집합

집합에 포함된 원소 선택

원소들의 그룹에서 최적의 부분집합 찾기: 자주 사용되는 알고리즘 구조

knapsack problem 등...



N개의 원소를 포함한 집합:

자기 자신과 공집합까지 포함된, 모든 부분집합의 개수는 2^n

원소의 수가 증가하면, 부분집합의 개수는 지수적으로 증가



단순한 부분집합 생성

```
for i1 in 0 -> 1:
	bit[0] <- i1
	for i2 in 0 -> 1:
		bit[1] <- i2
		for i3 in 0 -> 1:
			bit[2] <- i3
			...
			print_array()
```



### Binary Counting: 바이너리 카운팅을 통한 사전적 순서



## Combination: 조합

서로 다른 원소 중 r개를 순서 없이 골라낸 것

조합의 수식: nCr = n! / ((n-r)! * r!) (n >= r)

nCr = n-1Cr-1 + n-1Cr (조합의 재귀적 표현)

nC0 = 1



----



10개의 원소 중 3개를 고르는 조합: 10C3

```
a = []0~9

for i in 0 -> 7:
	for j in i+1 -> 8:
		for k in j+1 -> 9:
			f(a[i], a[j], a[k])
```

```python
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]에서 3개 고르는 조합                                                 
for i in range(8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            print(i, j, k)
    
```



재귀를 통해... n개에서 r개를 고르는 고합

```python
def nCr(n, r, s, k):			# n개에서 r개를 고르는데,
    							# 현재 k개를 골랐으며, s부터 고를 수 있다
    if k == r:
        # action
        print(*comb)
    else:
        for i in range(s, n-r+k + 1):
            comb[k] = i
            nCr(n, r, i+1, k+1)
            
N = 10
R = 3
comb = [0] * R
nCr(N, R, 0, 0)
```







# Greedy Approach: 탐욕 알고리즘

Sample Problem: Change

거스름돈을 지불하는 문제: 지폐와 동전의 갯수를 최소한으로 줄이는 법



최적해를 사용하는 데 사용되는 근시안적 방법

* 일반적으로 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 곧 greedy approach
* 여러 경우 중 하나를 선택할 때마다, 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적 해답에 도달
* 지역적 최적의 모음이 반드시 최적해일 수는 없음



탐욕 기법의 동작과정

1. 해 선택
   * 부분문제의 최적해를 구해 부분해집합에 추가
2. 실행 가능성 검사
   * 새 부분해집합이 실행가능한지 검사 (제약 조건)
3. 해 검사
   * 새 부분해집합이 문제의 해가 되는지 검사



Applied to Sample Problem

1. 고를 수 있는 가장 큰 단위 동전 제시
2. 액수를 초과하는지 검사
3. 액수가 맞는지: 모자라면 1로 돌아가기, 맞으면 답이므로 종료



최적해를 반드시 구한다는 보장이 없다!

cf. 물건값 1200원, 받은 돈 2000원, 거스름돈: 800

case 1: 500, 100, 50, 10

case 2: 500, 400, 100, 50, 10

case 2의 경우, 800원을 거슬러 줄 때 400 400이 아니라 500 100 100 100을 고르게 됨 (greedy approach의 실패)

: DP, 재귀, 부분집합 등을 이용한 풀이



## Example: Knapsack

배낭에 들어가는 물건들의 가치가 최대가 되도록 담는 방법

### Knapsack Problem의 정형적 정의

S = {item1, item2, ..., itemn}

wi = itemi의 무게, Pi = itemi의 가치

W: 배낭의 수용가능무게

Σitemi wi <= W이면서, ΣitemiPi가 최대가 되도록 하는



* 0 - 1 Knapsack: item 넣거나 말거나
* Fractional Knapsack: item 쪼개 넣을 수 있는 경우



### 0-1 Knapsack

부분집합: item n이 커질수록 연산량 너무 많아진다

Greedy 1: 비싼 물건부터 채우기 - 실패

Greedy 2: 가벼운 것부터 채우기 - 실패

Greedy 3: 무게당 가치가 높은 물건부터 채우기 - 역시 실패



### Fractional Knapsack

Greedy: 무게당 가치 - 성공!





----

모든 물건을 담은 경우 or 담은 물건의 무게 > W인 경우: return



## Activity-selection Problem: 활동 선택 문제

회의실 문제:

가능한 많은 회의를 여는 방법?

1 4 / 1 6 / 6 10 / 5 7 / 3 8 / 5 9 / 3 5 / 8 11 / 2 13 / 12 14 



시작시간과 종료시간이 있는 n개의 활동들의 집합 A = {A1, A2, ..., An}, 1 <= i <= n에서 non-overlapping 최대갯수 활동 집합 S를 구하는 문제



* 종료 시간 순으로 활동을 정렬



Greedy Approach

1. 하위문제 Si, j에서 종료시간이 가장 빠른 활동 am을 선택
2. Si,m은 공집합이므로, am을 선택하면 공집합이 아닌 하위 문제 Sm,j가 남는다
3. 1, 2과정을 반복한다

