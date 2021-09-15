13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

Tree 연습문제 input



# Tree

트리의 개념
비선형 구조,
원소들 간 1:n 관계를 가지는 자료구조
원소들 간에 계층관계를 가지는 계층형 자료
상위 원소에서 하위 원소로 내려가면서 확장되는 트리 구조

한 개 이상의 노드로 이루어진 유한집합
다음 조건을 만족
1. 노드 중 최상위 노드를 루트라고 한다
2. 나머지 노드들은 n개의 분리 집합 T1, T2, ..., TN으로 분리될 수 있다.
- 이들 분리집합들은 각각 하나의 트리가 됨 (재귀적 정의): 부트리(subtree)라 불림

* 정점 (node, vertex) 트리의 원소
* 단말노드, 잎노드 (terminal node, leaf node)

* 간선 (edge) 노드를 연결하는 선
* 루트 노드(root node): 트리의 시작 노드

부모 노드 / 자식 노드
형제 노드
조상 노드
서브트리
자손 노드

* Degree: 차수
  * 노드의 연결된 자식 노드의 수
* Level: 높이
  * 노드의 높이: 루트에서 노드에 이르는 간선의 수
  * *주의: 레벨 0부터 시작 / 레벨 1부터 시작*
  * 트리의 높이: 노드의 높이 최댓값



# Binary Tree: 이진 트리

모든 노드들이 (최대) 2개의 서브트리를 갖는 특수한 트리

* 자식이 없는 노드
* 왼쪽 자식 노드
* 오른쪽 자식 노드
* 자식이 둘 있는 노드

## 이진 트리의 특성

* 레벨 i에서의 노드의 최대 개수는 2**i개
* 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 h+1
* 최대 갯수는 2**(h+1) - 1

## 이진 트리의 종류

### Full Binary Tree: 포화 이진 트리

모든 레벨에서 노드가 포화상태로 차 있는 이진 트리

높이가 h일 때, 2^(h+1)-1개의 노드를 가지고 있음

루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가짐

**포화 이진 트리에서는 1번을 루트로 사용하는 것이 보편적**

### Complete Binary Tree: 완전 이진 트리

높이가 h이고, 노드 수가 n개일 때 (h+1 <= n < 2^(h+1)-1) 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리



### Skewed Binary Tree: 편향 이진 트리

* 높이 h에 대한 최소 개수의 노드를 가지면서
* 한쪽 방향의 자식 노드만을 가진 이진 트리
* ~~ 선형 자료구조처럼 형성됨 (트리의 장점 없음...)



## 이진 트리의 활용

## Traversal: 순회

Traversal: 트리의 각 노드를 중복되지 않게 체계적으로 전부 방문하는 것

비선형구조이므로, 선형구조에서와 같이 *선후 연결관계를 알 수 없기* 때문에, 특별한 방법이 필요하다.

#### 3가지 기본 순회 방법

* Preorder Traversal: 전위순회 VLR
  * 부모노드를 방문한 다음, 자식노드를 좌-우 순서로 방문
* Inorder Traversal: 중위순회 LVR
  * 왼쪽 자식, 부모, 오른쪽 자식 순으로 방문
* Postorder Traversal: 후위순회 LRV
  * 자식노드를 좌-우 순서로 먼저 방문한 후 부모노드 방문



#### Preorder Traversal

1. 현재 노드 N을 방문, 처리: V
2. 현재 노드 N의 왼쪽 서브트리로 이동: L
3. 현재 노드 N의 오른쪽 서브트리로 이동: R

* 전위 순회 알고리즘

```
def preorder_traverse(T):
	if T:
		visit(T)
		preorder_traverse(T.left)
		preorder_traverse(T.right)
```

```
# 예시
#    A			A: T0
#   /  \		B: T1
#  B   C		C: T2
# / \ / \
# D E F  G		E: T3
#  / \
#  H  I

# 순서1: T0 > T1 > T2
# 순서2: A > B D (T3) > C F G
# 전체 순서:
# A B D E H I C F G
```



#### Inorder traversal

1. 현재 노드 n의 왼쪽 서브트리로 이동: L
2. V
3. R

```
def inorder_traverse(T):
	if T:
		inorder_traverse(T.left)
		visit(T)
		inorder_traverse(T.rigth)
```

```
# 순서1: T1 > T0 > T2
# 순서2: D B (T3) > A > F C G
# 전체 순서:
# D B H E I A F C G
```



#### Postorder traversal

1. L
2. R
3. V

```
def postorder_traverse(T):
	if T:
		postorder_traverse(T.left)
		postorder_traverse(T.right)
		visit(T)
```

```
# 순서1: T1 > T2 > T0
# 순서2: 
# 전체 순서:
# D H I E B F G C A
```



#### 연습문제

VLR:

ABDHIEJCFKGLM

LVR:

HDIBJEAFKCLGM

LRV:

HIDJEBKFLMGCA



## 이진 트리의 표현

### 배열을 이용한 이진 트리의 표현

*포화/완전 이진 트리의 저장방법*

* 이진 트리의 각 노드 번호를...
  * 루트 번호: 1
  * n에 있는 노드에 대해 왼쪽부터 오른쪽으로 2^n부터 2^(n+1)-1까지
* 이 경우 노드 번호의 성질
  * i번의 부모: i//2 (floor)
  * i의 왼쪽 자식: 2*i
  * i의 오른쪽 자식: 2*i+1
  * lvl n의 첫번째 노드: 2^n

*그밖의 경우...?*

굳이 없는 공간에 0(빎)을 저장시켜야 할까?

마지막 정점 번호를 알고 있으니... 그보다 넘어가면 중단

높이가 h인 이진 트리를 위한 배열의 크기는?

2^(h+1)-1



단점:

편향 이진 트리의 경우: 사용하지 않는 공간 너무 많음

트리 중간에 새로운 노드 삽입 / 기존 노드 삭제 시 비효율적



### 연결 리스트를 이용한 트리의 표현







----

참조: Segment Tree

----



# Expression Binary Tree: 수식 트리

수식을 표현하는 이진 트리

연산자는 루트, 가지 노드

피연산자는 모두 잎 노드



# 이진 탐색 트리

cf. 이진 탐색

* 탐색작업을 효율적으로 하기 위한 자료구조
* 모든 원소는 서로 다른 유일한 key를 갖는다
* key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
* 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리
* 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다!

```
			루트
			/	\
<왼쪽 서브트리>	<오른쪽 서브트리>
루트보다 작은 값	루트보다 큰 값
```



탐색 연산

* 루트에서 시작
* 목표 키값을 루트 노드의 키값과 비교
  * ==: 성공
  * 목표 < 루트: 왼쪽 서브트리에 대해 탐색연산 수행
  * 목표 > 루트: 오른쪽 서브트리에 대해 탐색연산 수행



삽입 연산

1. 탐색 연산을 수행
   * 삽입할 원소와 같은 원소가 트리에 있으면 안 됨
   * 탐색 실패가 결정되는 위치가 곧 삽입 위치
2. 탐색 실패한 위치에 원소를 삽입



삭제 연산

1. 탐색 연산을 수행
2.  탐색 성공, 해당 노드 삭제
   1. 자식을 노드의 부모에 연결
   2. 루트 노드인 경우(두 개의 자식... 트리가 둘로 분리?!)
      1. 왼쪽 서브트리의 가장 오른쪽 leaf, 





## 이진 탐색 트리의 성능

* 탐색, 삽입, 삭제는 트리의 높이만큼 시간이 걸린다
* 평균: 이진트리가 균형적으로 생성되어 있는 경우
* 최악: 한쪽으로 치우쳐진 경사 이진트리의 경우
  * O(n)
  * 순차탐색과 같은 시간복잡도



검색 알고리즘의 비교

* 배열에서의 순차 검색: O(N)
* 정렬된 배열에서의 순차 검색: O(N)
* 정렬된 배열에서의 이진탐색: O(logN)
  * 단, 고정 배열 크기
  * 삽입, 삭제 시 추가 연산 필요
* 이진 탐색트리에서의 평균: O(logN)
  * 최악의 경우: O(N)
  * 완전 이진 트리, 또는 균형 트리로 바꿀 수 있다면 최악의 경우를 없앨 수 있다.
    * 새로운 원소를 삽입할 때 삽입 시간을 줄인다
    * 평균과 최악의 시간이 같다.
* 해시 검색: O(1)
  * But 추가 저장 공간이 필요



# Heap

완전 이진 트리에 있는 노드 중에서, 키값이 가장 큰 노드/키값이 가장 작은 노드를 찾기 위해 만든 자료구조

* Max Heap
  * 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  * (부모 노드의 키값 > 자식 노드의 키값)
  * 루트 노드: 키값이 가장 큰 노드
* Min Heap
  * 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  * (부모 노드의 키값 < 자식 노드의 키값)
  * 루트 노드: 키값이 가장 작은 노드

cf. 우선순위 큐

 

참고: 힙 연산 - 삽입

20 - 15 19 - 4 13 11 삽입 전의 힙 << 17 삽입

- 자리 늘려서 삽입
- 끝...?
- 부모와 키값 비교 (vs. 19)
- 그대로

20 - 15 19 - 4 13 11 삽입 전의 힙 << 23 삽입

* 자리 늘려서 삽입
* 부모와 키값 비교 (vs. 19)
* 더 크다: 서로 치환 (부모가 없거나, 부모의 키값이 더 클 때까지)
* 다시 부모와 키값 비교 (vs. 20)
* 더 크다: 서로 치환
* 끝



```
enQ(n)
	last += 1
	h[last] = n
	c = last
	p = c//2
	while p > 0 and h[p] < h[c]:
		h[c] <-> h[p]
		c <- p
		
```



힙 연산 - 삭제

* 루트 노드의 원소만을 삭제할 수 있다

예시:

1. 루트 원소 출력
2. last를 루트 자리에 놓고 마지막 노드 삭제(last -= 1)
3. 자리 바꾸기 (자식보다 크거나 leaf에 다다를 때까지-자식이 last보다 크면)



힙은 주로 우선순위 큐를 구현하는 데에 쓰임


