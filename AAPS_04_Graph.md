# Graph & Backtracking

* 그래프 기본
* 탐색
* 서로소 집합
* 최소 비용 신장 트리 MST
* 최단 경로



# 그래프 기본

그래프는 item들과 그 연결 관계를 표현

Vertex의 집합과 이들을 연결하는 Edge들의 집합으로 구성된 자료구조

\|V| 정점 개수

\|E| 간선 개수

V개의 정점을 가지는 그래프는 최대 V (V-1) / 2 간선이 가능

N:N 관계를 가지는 자료를 표현하는 데 유용



## 그래프의 유형

* Undirected Graph무향 그래프
* Directed Graph 유향 그래프
* Weighted Graph 가중치 그래프
* Directed Acyclic Graph (DAG) 사이클 없는 방향 그래프
  * (자기 자신으로 돌아올 수 있는 그래프: Cyclic)



* 완전 그래프
  * 정점들에 대해 가능한 모든 간선을 가진 그래프
* 부분 그래프
  * 원본 그래프에서 일부 정점이나 간선을 제외한 그래프



## 인접 정점

* Adjacency: 인접
  * 두 개의 정점에 간선이 존재하면 서로 인접해있다고 한다
  * 완전 그래프에 속한 임의의 두 정점은 모두 인접해 있다.



## 그래프의 경로

* Path: 경로
  * 간선들을 순서대로 나열한 것
* 단순 경로
  * 한 정점을 최대한 한 번만 지나는 경로
* Cycle: 사이클
  * 시작한 정점에서 끝나는 경우



## 그래프의 표현

간선의 정보를 저장하는 방식

메모리, 성능 등을 고려하여 결정

* 인접 행렬
  * 
* 인접 리스트



### Adjacent Matrix

방향이 없다면 대칭형의 행렬이

만일 방향이 있다면 행 번호가 출발, 열 번호가 도착으로 보통 쓰인다

차수: 한 정점에서 간선의 합

* 진출차수
  * 행의 합
  * "이 V에서 나가는 E는 몇 개?"
* 진입차수
  * 열의 합
  * "이 V로 들어오는 E는 몇 개?"



* 작성, 사용이 편하다
* 큰 용량이 필요하다

V가 1000개 정도여도 Adj Matrix를 만드는 것이 가능은 하다 (느림)



### Adjacent List

각 V에 대한 인접 V들을 순차적으로 표현

한 V에 대한 인접 V를 각각 노드로 하는 연결 리스트로 저장

V가 1000개가 넘어가면 Adjacent List가 좋을 것




### 저장 예시

```python
'''
6 8
0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4
마지막 정점 번호 / 간선 수
간선 정보
'''

V, E = map(int, input().splilt())
edge = list(map(int, input().split()))

adjM = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1 	# 무향 그래프인 경우
    
# 0번~ V번까지



# Python에서는 길이가 다른 리스트들의 리스트를 작성할 수 있으므로
'''
[[1, 2, 5, 6],		# 0번 정점에 연결된 정점들의 번호
 [0],				# 1번 정점에 연결된 정점들의 번호
 [0],				# 2번 정점...
 [0, 4, 5],
 ...]
 
 단, 따로 정렬을 하지 않는 한 입력 순서대로 나올 것임
'''
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)	# 무향 그래프인 경우

```



# 그래프 탐색

(순회라고도 하지만, 주로 탐색이라는 표현을 쓴다)



그래프 탐색은 비선형구조인 그래프로 표현된 모든 자료(=V)를 빠짐없이 탐색하는 것을 의미한다.

* Depth First Search (DFS):깊이 우선 탐색
* Breadth First Search (BFS): 너비 우선 탐색



## DFS

시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색하기

더 이상 갈 곳이 없게 되면, 마지막 갈림길 간선이 있는 정점으로 되돌아와 다른 방향의 정점으로 탐색을 계속 반복하여 모든 정점을 방문하는 순회방법

일반적으로 후입선출 구조의 스택을 사용

재귀 함수로 구현했다면, 각 호출이 방문 상태를 저장하고 있으므로 Return만으로 활용 가능

반복 구조로 구현했다면 스택을 사용해야 함



cf. "스택을 쓰면 DFS, 큐를 쓰면 BFS"라는 말은 맞을까?



### 스택

LIFO 선형구조: 물건을 쌓아올린 형태

* 배열과 top
* push, pop, isEmpty, peek과 같은 연산이 필요



python list의 append pop으로 구현하기

vs

최대크기 배열과 idx(top)으로 구현하기



#### 스택 구현

```
push(S, x):
	top = top + 1;
	if top >= STACK_SIZE:
		error overflow;
	else:
		S[top] = x;
		
pop(S):
	if top < 0:
		error underflow;
	else:
		top = top - 1;
		return S[top + 1];

```





### DFS by Recursion

```
DFS_Rec(G, v):
	visited[v] = True						# v에 대해 방문 표시
	
	for each all w in adjacency(G, v):		# 인접한 모든 정점 w에 대해...
		if visited[w] != True:
			DFS_Recursive(G, w)				# w에서 방문 실시
			
	visited[v] = False						# 만약에 경로의 갯수를 센다던가 하는 이유로
											# 필요한 경우
```



### DFS by Iteration

```
STACK s
visited []
DFS(v):
	push(s, v)
	while not isEmpty(s):
		v = pop(s)
		if not visited[v]:
			visit(v)
			for each w in adjacency(v):
				if not visited[w]:
					push(s, w)
					
					
					
STACK s
visited []
DFS(v):
	push(s, v)
	visited[v] = True			# push와 visited를 같이 묶어서 하는 경우
	while not isEmpty(s):
		v = pop(s)
		if not visited[v]:
			visit(v)
			for each w in adjacency(v):
				if not visited[w]:
					push(s, w)
					visited[v] = True
					
# 갈림길을 기억하는 방식
# 중복검사할 필요도 없고,
# 스택 크기도 최대 정점 개수만큼만 필요하기 때문에 스택 크기로 고민할 필요가 없음
# 다만 경로 상 모든 정점에 대한 작업이 필요하다면 먼저 방식을 쓰는 것이 좋을 것
```



## BFS

탐색 시작점의 정점들을 먼저 모두 차례로 방문

방문했던 정점을 시작점으로 하여 다시 인접 정점을 차례로 방문

인접 정점들에 대해 탐색을 하고, 차례로 다시 너비우선탐색을 진행해야 하므로 보통 FIFO 형태의 자료구조인 큐를 활용





### Queue

스택과 같이 삽입과 삭제의 위치가 제한적

큐의 앞에서 삭제, 뒤에서 삽입: 선입선출구조 (FIFO)

Queue[] Front, Rear로 구성

enQueue, deQueue 구현



```
enQueue(Q, x):
	if isFull():		// rear == queue_size
		error Queue_full
	else:
		rear = rear + 1
		Q[rear] = x
		
deQueue(Q):
	if isEmpty():
		Queue_empty:
	else:
		
...
```



### BFS Algorithm

````
BFS(G, v):		# 그래프 G, 방문시작점 v
	큐 생성
	v를 큐에 삽입
	v에 방문 표시
	while 큐가 비어있지 않음
		t = 큐의 첫번째 원소 반환
		< 해당 정점에 대한 작업 >		# 작업은 꺼낸 다음에
		for t와 연결된 모든 선에 대해
			u = t의 이웃점
			if u 미방문:
				enQueue u
				u 방문 표시
````



# Disjoint-sets:서로소 집합

서로소 집합(= 상호배타 집합) 서로 중복 포함된 원소가 없는 집합, 즉 상호간 교집합이 없는 집합

집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분하고, 이를 representative(대표자)라 함



* 표현 방법
  * 연결 리스트
  * 트리
* 연산
  * make-set(x)
  * find-set(x)
  * union(x, y)



make-set(x): x를 대표로 하는 독립집합 만들기

...

Union(x, y): x가 속한 집합, y가 속한 집합을 합침, 최종 대표 원소를 결정

find-set(y): y가 속한 집합의 대표 원소를 반환



## Represent Disjoint-set by Tree

하나의 집합을 하나의 트리로 표현하기

자식 노드가 부모 노드를 가리키며, 루트 노드가 대표자가 된다

cf. a / b / c < d, c < e, e < f

[첨자: 0 1 2 3 4 5]

[정점: a b c d e f]

[부모: 0 1 2 2 2 4]



## 상호배타집합의 연산

* Make-Set(x): 유일한 요소 x를 포함하는 새로운 집합을 생성하는 연산

  * ```
    Make-Set(x):
    	p[x] = x
    ```

* Find_Set(x): x를 포함하는 집합을 찾는 연산

  * ```
    ## 재귀 형태
    Find-Set(x):
    	if x == p[x]:	return x
    	else:			return Find-Set(p[x])
    
    ```

  * ```
    ## 반복구조 형태
    Find-Set(x):
    	while x != p[x]:
    		x = p[x]
    	return x
    ```

* Union(x, y): x와 y를 포함하는 두 집합을 통합하는 연산

  * ```
    Union(x, y)
    	p[Find-Set(y)] = Find-Set(x)
    	# y의 대표원소가 자기 자신 대신 x의 대표원소를 가리키도록
    ```





### 상호배타집합의 연산 효율성 제고

* subtree의 높이를 rank로 저장,

  * ```
    Union(x, y):
    	Link(find_set(x), find_set(y))
    	
    Link(x, y):
    	if rank[x] > rank[y]
    ```

  * 

* Path Compression

  * Find-Set을 수행할 때 바로 root를 가리키도록

  * ```
    ```

    

  * 

* 



# Minimum Spanning Tree: 최소 신장 트리

* 신장 트리
  * n개의 정점으로 이루어진 무향 그래프에서, n개의 정점과 n-1개의 간선으로 이루어진 트리
* 최소 신장 트리
  * 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장 트리

그래프에서 최소 비용 문제를 해결하기 위해 사용



## MST의 표현

그래프

간선들의 배열

인접 리스트

...



## Prim Algorithm

하나의 정점에서 연결된 간선들 중 하나씩 택하면서 MST를 만들어감

1. 임의 정점을 1개 선택
2. 인접 정점 중 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될 때까지 1-2 반복

서로소인 2개의 집합 정보를 유지



"MST에 포함되지 않고 남은 정점이 있을 때:

MST에 속한 정점 v에 인접하고, 아직 MST에 속하지 않은 정점 w 중에서

비용(가중치)이 최소인 경로를 선택하기"



```
MST_PRIM(G, r):									# 그래프 G, 시작 정점 v
	for u in G.V
		# 초기화 부분
		u.key = infi							# u에 연결된 간선 중 최소 가중치 u.key
		n.pi = NULL								# 트리에서 u의 부모() u.pi
		
	r.key = 0		
	MST[r] = 1	# (우선순위 큐 대신) 기록 남기는 방식
	Q = G.V										# (우선순위) Q에 모든 정점을 넣는다
	while Q != 0:								# Q가 비어있지 않은 동안:
		u = Extract_Min(Q)						# key값이 가장 적은 정점 가져오기
		for v in G.Adj[u]:
			if v in Q and w(u, v) < v.key:
				v.pi = u
				v.key = w(u, v)
```



예제 코드

```python
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def prim(start, V):
    key = [INF] * (V+1)
    key[start] = 0			# 시작 정점의 비용은 0 취급
    MST = [0] * (V + 1)
    pi = [0] * (V + 1)
    
    for _ in range(V):
        # MST에 포함되지 않으면서(MST[u] == 0) key[u]가 최소인 u 찾기
        u = 0
        minV = INF
        for i in range(1, V+1):
            if MST[i] == 0:
                if key[i] < minV:
                    u = i
                    minV = key[i]
        # u 찾고 나면...
        # key[u]가 최소인 u를 MST를 추가
        MST[u] = 1
        
        # u를 통해서 인접한 정점들의 key값 갱신
        for v in range(V+1):
            if MST[v] == 0 and 
        
        

```



## Kruskal Algorithm

간선을 하나씩 선택해서 MST을 찾는 알고리즘

1. 모든 간선을 가중치에 따라 오름차순 정렬
2. 가중치가 가장 낮은 간선부터 선택하며 트리를 증가
   * 이 때, 사이클이 존재하게 되면 다음으로 가중치가 낮은 간선 선택
   * 사이클 여부를 검사하기 위해 find_set과 union을 활용
3. n-1개의 간선이 선택될 때까지 2를 반복



각각 find_set을 했을 때 값이 다르면: 선택 시 cycle이 형성되지 않을 것임을 알 수 있음

선택하고 union하기



```python
MST-Kruskal(G, w):
    A = {}										# 공집합
    for vertex v in G. V:						# G.V: 그래프 정점 집합
        Make_Set(v)								# G.E: 그래프 간선 집합
       
    G.E에 포함된 간선들을 w에 의해 정렬
    
    for 최소 가중치 (u, v) in G.E 선택 (n-1개):
        if find_set(u) != find_set(v):
            A = A and {(u, v)}
            Union(u, v);
            
    return A
```





# 최단 경로

간선의 가중치가 있는 그래프에서, 두 정점 사이의 경로들 중 간선의 가중치 합이 최소인 경로



* 하나의 시작 정점에서 끝 정점까지의 최단경로
  * Dijkstra
    * 음의 가중치를 허용하지 않는 경우
  * Bellman-Ford
    * 음의 가중치를 허용하는 경우
* 모든 정점들에 대한 최소비용
  * Floyd-Warshall



## Dijkstra Algorithm

시작 정점에서 거리가 최소인 정점을 선택해나가면서 최단 경로(최소 비용)를 구하는 방식



```
# s: 시작 정점, A: 인접행렬, D: 거리
# V: 정점 집합, U: 선택된 정점 집합

Dijkstra(s, A, D):
	U = {s};
	
	for all v:
		D[v] = A[s][v]
		
	while U != V:
		D[w]가 최소인 정점 w in V-U를 선택			# 아직 선택되지 않은 것들 중에...
		U = U and {w}							  # 선택하기
		
		for w에 인접한 모든 정점 v:
			D[v] = min(D[v], D[w] + A[w][v])
```



