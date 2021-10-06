* 분할정복
* 백트래킹
* 트리



# Divide and Conquer: 분할 정복

## Problem: 가짜 동전 찾기

n개의 동전들 중의 가짜 동전 1개를 찾기



## 분할 정복 기법

Divide, Conquer, Combine: 분할, 정복, 통합

크기 N인 문제를 N/k인 부분 문제 k개로 나누어 풀고 통합하기



## 거듭 제곱 예시

C^n = C * C * C * ... * C

```
Recursive_Power(x, n):
	if n == 1: return x
	if n is even:
		y = Recursive_Power(x, n/2)
		return y * y
	else:
		y = Recursive_Power(x, (n-1)/2)
		return y * y * x
```

O(n^2)이었던 문제가 O(logn)으로!



## Merge Sort: 병합 정렬

여러개의 정렬된 자료의 집합을 병합하여, 한 개의 정렬된 집합으로 만드는 정렬



### Example

1. [69, 10, 30, 2, 16, 8, 31, 22]가 주어짐

2. 최소 크기의 부분집합이 될 때까지 분할
   * [69, 10] [30, 2] [16, 8] [31, 22]
3. 정렬하며 하나의 집합으로 병합
   * [10, 69] [2, 30] [8, 16] [22, 31]
   * [10, 69, 2, 30] [8, 16, 22, 31]
   * [2, 10, 30, 69] [8, 16, 22, 31]
   * [2, 8, 10, 16, 22, 30, 31, 69]

(실제 구현 차원에서는 메모리를 절약하기 위해 실제 자료를 나눠 저장하기보단 인덱스를 활용)



```
merge_sort(LIST_m):
	if length(m) == 1: return m
	
	list left, right
	middle = length(m) / 2
	
	for x in m before middle
		add x to left
	for x in m after or equal middle
		add x to right
		
	left = merge_sort(left)
	right = merge_sort(right)
	
	return merge(left, right)
```

```
merge(list left, list right):
	list result
	
	while length(left) > 0 or length(right) > 0:
		if length(left) > 0 and length(right) > 0:
			if first(left) <= first(right):
				append popfirst(left) to result
			else:
				append popfirst(right) to result
		elif:
		elif:
		
	return result
		
```



## Quick Sort

배열 이분할 후 각각 정렬, but...

1. 절반이 아니라 pivot item을 중심으로 작은 걸 왼쪽, 큰 걸 오른쪽으로
2. 각 부분 정렬 후에 별도의 병합과정이 필요없음

```
quickSort(A[], l, r):
	if l < r
		s = partition(a, l, r)		# 나눔
		quickSort(A[], l, s-1)		# 왼쪽 구간	
		quickSort(A[], s+1, r)		# 오른쪽 구간
	
```

Hoare-Partition 알고리즘

```
partition(A[], l, r):
	p = A[l]  # 피봇 값 (일단 맨 왼쪽을...)
	i = l
	j = r
	while i <= j:
		while i <= j and A[i] <= p: i++
		while i <= j and a[j] >= p: j--
		if i < j: swap(A[i], A[j])
		
	swap(A[l], A[j]) # 피봇을 j가 가리키는 값으로 바꿈
	return j
```



기본 아이디어

[P // P>i인 i들 // P<i인 i들]

[P>i인 i들 // P (쏙) // P<i인 i들]



### 피봇 선택

왼쪽 끝, 오른쪽 끝,

임의의 세 개 중 중간값 등 (재귀 깊이를 최대한 균등하게 하기 위함)



Lomuto partition 알고리즘

```
partition(A[], p, r):
	x = A[r]
	i = p - 1
	
	for j in p -> r-1:
		if A[j] <= x:
			i++
			swap(A[i], A[j])
			
	swap(A[i+1], A[r])
	return i + 1
```

피봇 x(A[r])보다 작은 경우, i와 j가 함께 움직임

큰 경우 j만 움직임



## Binary Search: 이진 검색

자료가 정렬된 상태여야 가능

가운데 키값과 비교하고 범위를 줄여나가는 방식



반복구조

```
binarySearch(n, S[], k):
	low = 0
	high = n-1
	
	while low <= high:
		mid = low + (high - low) / 2
		
		if S[mid] == key:
			return mid
		elif S[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
			
	return -1
```



## 정리

병합 정렬: 외부 정렬의 기본 알고리즘, Multi-core CPU 등 정렬 알고리즘 병렬화를 위해 활용

퀵 정렬: 매우 큰 입력 데이터에서 좋은 성능을 보임



# Backtracking: 백트래킹

## Example: N-Queen Problem

N by N 체스판에서 n개의 Queen을 서로 위협하지 않도록 배치하는 문제

1. 여러 선택지 중 한 가지를 먼저 선택
2. 선택에 의해 새로운 선택지 집합이 형성
3. 



Backtracking: 

## Backtracking v. DFS

Prunning

경우의 수가 너무 많은 경우...

DFS는 N!

Backtracking는 최악의 경우 Exponential Time이므로 역시 힘들지만, 그래도 가능한 경우 있음



## 8-Queens Problem

8 Queens in 8 by 8 board?

후보 해의 개수: 64C8 = 약 44억 개

실제 해의 개수: 92개

이걸 어떻게 찾지...?

냅다 놓고 가로 세로 ... 이러면 절대 못 풀 문제



4-Queen으로 축소해서 생각해보자

1. 굳이 같은 행에 놓을 필요가 없다는 건 자명
   * 그럼 4 * 4 * 4 * 4 = 256경우



DFS: 155 노드 탐색

백트래킹: 27 노드 탐색



상태공간트리의 구축 (일반적 형태의 백트래킹)

```
bool backtrack(선택집합, 선택한 수, 모든 선택 수):
	if (선택한 수 == 모든 선택 수):
		솔루션 체크
		return 결과
	
	else:
		후보 선택들 생성
		선택 집합에 1개의 후보 선택을 추가 (해 보기)
		선택한 수 = 선택한 수 + 1
		결과 = backtrack 호출
		
		if 결과 == 성공
			return 성공
			
		return 실패
```

```
backtrack(a[], k, input):
	c[maxcdndidates]
	ncands
	
	if k == input:
		process_solution(a[], k)
	else:
		k++
		make_candidates(a[], k, input, c[], ncands)
		for i in 0 -> ncands - 1:
			a[k] = c[i]
			backtrack(a, k, input)

make_candidates(a[], k, n, c[], ncands):
	c[0] = True
	c[1] = False
	ncands = 2

process_solution(a[], k):
	for i in 1 -> k:
		if a[i] == True:
			print(i)

main():
	a[MAX]						# powerset을 저장할 배열
	backtrack(a[], 0, 3)		# 3개의 원소를 가지는 powerset
	

```





백트래킹을 이용해 순열 구하기

```
make_cand(a[], k, n, c[], ncands):
	in_perm[NMAX] = False
	
	for i in 1 -> k-1:
		in_perm[a[i]] = True
	ncand = 0
	for i in 1 -> n:
		if in_perm[i] == False:
			c[ncands] = i
			ncands ++
process_solution(a[], k):
	for i in 1 -> k:
		print(i)
```





----





# Tree: 트리 활용



## Tree Revisited

* 트리는 Cycle이 없는 무향 연결 그래프이다
  * 두 노드 사이에는 유일한 경로가 존재
  * 각 노드는 최대 하나의 부모 노드가 존재
  * 각 노드는 자식 노드가 없거나, 하나 이상이 존재할 수 있음
* 비선형 구조
  * 원소들 간 1:n 관계 구조
  * 원소들 간 계층관계를 가짐



* 1개 이상의 노드로 이루어진 유한집합이며,
* 노드 중 부모가 없는 노드를 Root라고 한다.
* 나머지 노드들은 n개의 분리 집합 T1, T2, ... TN으로 분리될 수 있다.
* 이들은 각각 하나의 트리가 되며(재귀적 정의)
  루트의 Subtree라 한다.

Leaf Node, Terminal Node, ...



* Node 노드: Elements of Tree, =Vertex
* Edge 간선: Lines linking nodes
* Root Node
* Sibling Node: 같은 부모 노드의 자식 노드들
* 조상 노드: edge를 따라 root node까지 이르는 경로에 있는 모든 node
* subtree: 부모 node와 연결된 edge를 끊었을 때 생성되는 tree
* 자손 노드: subtree에 있는 하위 level의 node들



* Degree 차수
  * Degree of Node: 노드에 연결된 자식 노드의 수
  * Degree of Tree: 트리에 있는 노드의 차수 중에서 가장 큰 값
  * Leaf Node: 0 degree Node
* Level 높이
  * Level of Node: 루트에서 노드에 이르는 간선의 수
  * Level of Tree: 트리에 있는 노드의 높이 중 가장 큰 값
    Maximum level of nodes



## Binary Tree: 이진 트리

모든 노드들이 최대 2개의 subtree를 갖는 특수한 형태의 tree

left child node

right child node



### 특성

Level i에서 node의 최대 개수는 2^i개

높이가 h인 binary tree가 가질 수 있는 노드의 최소 개수는 h+1개가 되며, 최대 개수는 2^(h+1)-1개가 된다.



### 종류

* Full Binary Tree: 포화 이진 트리
  * 모든 Level의 노드가 채워져 있음
  * 높이 h인 binary tree가 2^(h+1)-1의 노드를 모두 갖고 있는 형태
  * root를 1번으로 하여 2(h+1)-1까지 *정해진 위치*에 대한 노드 번호를 가짐
* Complete Binary Tree: 완전 이진 트리
  * 높이가 h이고 노드 수가 n개 일 때, 포화 이진 트리의 노드 번호 1번부터 n번까지의 빈 자리가 없는 이진 트리
* Skewed Binary Tree: 편향 이진 트리
  * 높이 h에 대한 최소 개수 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리



### Traversal: 순회

트리의 노드들을 체계적으로 방문하는 것

​                     V (Root)

L(Left Subtree)     R(Right Subtree)

* Preorder Traversal 전위 순회: VLR
* Inorder Traversal 중위 순회 LVR
* Postorder Traversal 후위 순회 LRV



#### 전위 순회

```
preorder_traverse (Tree T)
	if T is not null
		visit(T)						# 방문해서 수행할 작업
		preorder_traverse (T.left)		# L child
		preorder_traverse (T.right)		# R child
```



#### 중위 순회

```
preorder_traverse (Tree T)
	if T is not null
		preorder_traverse (T.left)
		visit(T)
		preorder_traverse (T.right)
```



#### 후위 순회

```
preorder_traverse (Tree T)
	if T is not null
		preorder_traverse (T.left)
		preorder_traverse (T.right)
		visit(T)
```



### 노드 번호의 성질

노드 번호가 i인 노드의 부모 노드 번호 i // 2

왼쪽 자식 2*i

오르쪽 자식 2*i + 1

레벨 n의 노드 시작 번호 2^n



참고: 레드 블랙 트리

---



배열을 이용한 이진 트리 표현의 단점

* 편향 이진 트리의 경우 사용하지 않는 배열 원소에 대한 메모리 낭비



트리의 표현: 연결 리스트

[]



### 이진 탐색 트리

* 탐색 작업을 효율적으로 하기 위한 자료구조
* 모든 원소는 서로 다른 유일한 키를 가짐
* Key(왼쪽 서브트리) < Key(루트 노드) < Key(오른쪽 서브트리)
* 양 서브트리 또한 이진 탐색 트리가 된다
* 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다



탐색 연산

삽입 연산

삭제 연산

* 리프라면 간단히 삭제
* 차수가 있는 경우: 그림을 그려 확인해보자
  * 왼쪽 서브트리의 마지막 값으로 치환하기



#### 이진 탐색 트리의 성능

탐색, 삽입, 삭제 연산의 경우 트리의 높이만큼 시간이 걸린다.

O(h)

평균: 이진 트리가 균형적으로 생성된 경우

O(logn)

최악: 편향 이진 트리

O(n) == 순차탐색의 시간복잡도



## Heap

Complete Binary Tree에 있는 노드 중 키값이 가장 큰 코드나, 키값이 가장 작은 노드를 찾기 위해 만든 자료구조

* Max Heap:
  * 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  * 부모 노드의 키값 > 자식 노드의 키값
  * 루트 노드: 최대값
* Min Heap
  * 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  * 부모 노드의 키값 < 자식 노드의 키값
  * 루트 노드: 최소값

주로 우선순위 큐를 구현하는 데 사용됨



힙을 활용하는 대표적인 두가지 예: 특별한 큐의 구현과 정렬

* 추가, 삭제 시간복잡도 O(logN)
* 최대, 최소값을 O(1)에 구함
* 관리에 소모되는 자원 적음



### Heap의 활용

배열을 통해 트리 형태를 쉽게 구현할 수 있음

부모나 자식 노드를 O(1) 연산으로 쉽게 찾을 수 있음



#### Heap Sort

1. 하나의 값을 힙에 삽입한다
2. 힙에서 순차적으로 값을 하나씩 제거한다

전체 정렬에 소요되는 시간 복잡도 O(NlogN)



