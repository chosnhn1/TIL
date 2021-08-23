* 계산기
* 백트래킹
* (참고) 부분집합 / 순열
* 분할정복



# 계산기

문자열로 된 계산식을 스택을 이용해 계산하기

1. 중위 표기볍을 후위표기법으로 변경
   * A+B >> AB+
2. 후위 표기법을 스택이용해 계산
   * A, B, +: A+B!

두 단계 계산



* 중위표기식에서 후위표기식으로 변환 방법 1
  * 괄호를 사용해 다시 표현
  * 연산자를 괄호 뒤로 이동
  * 괄호 제거
* Example: A*B/C-D
* 중위표기식에서 후위표기식으로 변환 방법 2: Stack!
  * 입력받은 중위표기식에서 Token을 읽는다
  * if token == operand: 토큰 출력
  * if token == operator:
    * top의 연산자보다 우선순위 높으면 push
    * 아니라면, top의 연

```
icp(incoming priority)
isp(in-stack priority)
if (icp > isp) push() else pop()
```

(6+5*(2-8)/2) >> [?]

1. 토큰 하나 가져오기
2. 토큰이 연산자라면 스택 top과 비교: 스택 top의 isp가 토큰의 icp보다 높으면, 여는괄호면, 비어있으면 push
3. 토큰이 피연산자라면 그대로 출력(다른 곳에 저장)
4. not push 상태가 되면! (ex. 닫는 괄호)
5. 여는 괄호를 만날 때까지 전부 pop() (연산자를 피연산자들 뒤에 저장)
6. 닫는 괄호는 버림
7. top 변경



* 후위 표기법의 수식을 스택을 이용해 계산
  1. 피연산자를 만나면 push
  2. 연산자를 만나면 필요한 만큼의 피연산자를 pop해서 연산
  3. 연산 결과를 다시 스택에 push
  4. 수식이 끝나면 마지막으로 스택을 pop하여 출력



# Backtracking

* 백트래킹: 해를 찾는 도중에 막히면 되돌아가 다시 해를 찾아가는 기법
* Optimization (최적화), Decision(결정) 문제 해결
* 결정 문제: 조건을 만족하는 해가 존재하는지 검증하는 문제 (입력크기가 크면 계산량이 상당한 문제들)
  * 미로 찾기
  * n-Queen
  * Map Coloring
  * Subset Sum 문제



## Maze

입구에서 출구까지 4방향으로 움직이며 경로 찾기

```
int mazeArray[8][8] = {
	{0, 0, 1, 1, 1, 1, 1, 1},
	{1, 0, 0, 0, 0, 0, 0, 1},
	{1, 1, 1, 0, 1, 1, 1, 1},
	{1, 1, 1, 0, 1, 1, 1, 1},
	{1, 0, 0, 0, 0, 0, 0, 1},
	{1, 0, 1, 1, 1, 1, 1, 1},
	{1, 0, 0, 0, 0, 0, 0, 0},
	{1, 1, 1, 1, 1, 1, 1, 0}
}
```

스택에 지나간 경로 저장하기 / 갈 수 있는 곳의 목록 저장하기 (DFS)



[현재 칸, 새 칸 찾아 움직임] > stack에 push

[[0, 1, 오른쪽], [1, 1, 오른쪽], [2, 1, 오른쪽], ...]

더 이상 진행 불가하다면 진행할 수 있는 상태로 되돌아가야. (탐색)

+1한 방향을 탐색



## Backtracking vs. DPS

* 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않다면, 더이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 (Pruning, 가지치기)
* 깊이 우선 탐색이 모든 경로를 추적하는데 비해, 백트래킹은 불필요한 경로를 조기에 차단
* 깊이 우선 탐색을 수행하기에는 경우의 수가 너무 많은 경우 > 백트래킹을 적용하면 일반적으로 경우의 수가 줄어들지만, 이 역시 최악의 경우 여전히 Exponential Time을 요함 (처리불가)

* Backtracking은 모든 후보를 검사하지 않는다. > 어떻게?
  * 어떤 노드가 Promising한지(유망한지) 판단하고, 그렇지 않다면 그 노드의 부모로 되덜아가 다음 자식 노드로 감
  * 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없다면: not promising
  * 해답의 가능성이 있다면?: promising
  * Pruning(가지치기): 유망하지 않은 노드가 포함된 경로는 고려 대상에서 제외



백트래킹

1. 상태 공간 트리의 DPS를 실시

2. 각 노드의 유망성 점검

3. 유망하지 않다면 부모 노드로 돌아가 다음 검색 수행

   

### Example: n-Queen Problem

cf. n-Queen Problem

```
def checknode (v) : # node
	if promising(v) :
		if there is a solution at v:
			write the solution
		else:
			for u in each child of v:
				checknode(u)
```



cf. 상태 공간 트리

Naive DPS: 155 vs. Backtracking: 27





## Powerset

어떤 집합의 공집합과 자기 자신을 포함하는 모든 부분집합: Powerset

n elements > 2^n 부분집합

powerset 구하기



cf. by loop

```
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



cf. Powerset을 구하는 Backtracking Algorithm

```
def backtrack(a, k, input):
	global MAXCANDIDATES
	c = [0] * MAXCANDIDATES
	
	if k == input:
		process_solution(a, k)
		# 답이라면 원하는 작업
	else:
		k += 1
		ncandidates = construct_candidates(a, k, input, c)
		# 유망한 후보 고르기
		for i in range(ncandidates):
			a[k] = c[i]
			backtrack(a, k, input)
			
def construct_candidates(a, k, input, c):
	c[0] = True
	c[1] = False
	return 
```



### Permutation: 순열

동일한 숫자가 포함되지 않았을 때(순열)의 loop 순열

```
for i1 in range(1, 4):
	for i3 in range(1, 4):
		
```

백트래킹 순열

```
def construct_candidates(a, k, input, c):
	in_perm = [False] * NMAX
	
	for i in range(1, k):
		in_perm[a[i]] = True
	
	ncandidates
```





#### Practice

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소 합이 10인 부분집합을 구하시오.

i 고려 대상인 부분집합 원소를 가리키는 인덱스

A 부분집합 원소 정보

그렇다면...

* Element i의 포함 여부가 결정되면, i까지의 합 Si가 결정되고
* Si-1이 찾고자 하는 부분집합의 합보다 크다면, 남은 원소를 고려할 필요가 없다



```
f(i, N, s, t)   # i-1까지의 합 s가 주어진다면,
				# if s>t return 백트래킹이 일어날 수 있도록
```

```
f(i, N, s, t):
		if s == t		# i-1 원소까지의 합이 찾는 값인 경우
		elif i == N		# 모든 원소에 대한 고려가 끝난 경우
		elif s > t		# 남은 원소를 고려할 필요가 없는 경우
		else			# 남은 원소가 있고, s < t인 경우
		
			subset[i] = 1
			f(i+1, N, s + A[i], t)	# element i 포함
			subset[i] = 0
			f(i+1, N, s, t)			# element i 미포함
			## 두 개의 재귀호출
```



##### 추가 고려사항

남은 구간의 합 RS: 남은 원소의 합을 다 더해도 T 미만이라면 중단

고려 구간의 합 S. S > T라면 중단 (넘어버렸네?) ][ 남은 구간의 합 RS. S+RS < T라면 중단 (다 더해도 안 닿겠네?)



##### cf. Permutation Construction

*순열, 조합을 재귀로 만드는 방법 알아야.*

A[1, 2, 3]: 123, 132, 213, 231, 312, 321

1. P[0] 결정
2. P[1] 결정
3. P[2] 결정
4. 완성

```
f(i, N):
	if i == N:  # 순열 완성
	
	else:
				# 가능한 모든 원소에 대해 P[i] 결정
		
		for j: i -> N-1		# j와 바꾸기 (처음엔 자기 자신과 바꾸기)
			P[i] <-> P[j]
			f(i+1, N)		# P[i] 복구
			P[i] <-> P[j]
```



```python
def f(i, N, ##r):
    if i == N ##r:  # 완성~
        print(P#[0:r])

    else:		# i번 원소의 값 결정
        for j in range(1, N-1):  # 자기부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N, ##r)
            P[i], P[j] = P[j], P[i]
            
P = [1, 2, 3]
f(0, len(P))
##nPr만 출력하기
```



# Divide-and-Conquer Algorithm



## Example: Exponentiation

```
def Power(Base, Exponent):
	if Exponent == 0 or Base == 0:
		return 1
	
	if Exponent % 2 == 0:
		NewBase = Power()
```

O(log2n)으로 줄이기



----

Quick Sort

