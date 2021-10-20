* Queue
* Types of Queue
  * Linear Queue: 선형큐
  * Circular Queue: 원형큐
  * Linked Queue: 연결큐
  * Priority Queue: 우선순위 큐
* Cases of Applied Queue: 큐의 활용
  * Buffer
  * Breadth First Search (BFS): 너비 우선 탐색

# Queue

Same as stack but FIFO

back of the queue: only push

front of the queue: only pop



## Structure of Queue

```

Queue [ 0 1 2 1 2 3 2 1 4 5 2 1 ... 2 3 5 6 - - - - - - - - ]

        F                                 R
```

Front/Rear, two index will be managed

* Front: 저장된 원소 중 첫번째 or 삭제된 위치
* Rear: 저장된 원소 중 마지막



## Queue의 주요 연산

* enQueue(item): rear 다음에 원소를 삽입하는 연산
* deQueue(): front에서 원소 삭제/반환 연산
* createQueue(): 공백 큐 생성 연산
* isEmpty(): 공백인지 확인
* isFull(): 포화인지 확인
* Qpeek(): front에서 원소를 삭제없이 반환하는 연산



## Queue의 연산 과정

1. createQueue();
   * Q [ _  _  _ ]: front = rear = -1

2. enQueue(A);

rear += 1; Q[rear] = A

3. enQueue(B);

rear += 1; Q[rear] = B // Q [ A  B  _ ]: front = -1, rear = 1

4. deQueue();
   * front += 1
   * data = Q[front]; return data
5. enQueue(C);
   * 
6. deQueue();
   * 
7. deQueue();
   * front == rear: 마지막 내용물까지 꺼냄(빎)



# Linear Queue

1차원 배열을 이용한 큐

* 속성
  * 큐의 크기 = 배열 크기
  * front: 저장된 첫번째 원소의 인덱스
  * rear: 저장된 마지막 원소의 인덱스

* 상태 표현
  * 초기 상태: front = rear = -1
  * 공백 상태: front = rear
  * 포화 상태: rear = n-1 (n: 배열 크기, n-1: 배열 마지막 인덱스)



## 큐의 구현

### 삽입

```
def enQueue(item):
	global rear
	if isFull(): print("Queue_Full")	# 디버깅용
	else:
		rear <- rear + 1;
		Q[rear] <- item;
```

### 삭제

```
def deQueue():
	if isEmpty() then Queue_Empty();	# debugging
	else:
		front <- front + 1;
		return Q[front];
```

### 상태 검사

```
def isEmpty():
	return front == rear
def Full():
	
```

### 검사

```
def Qpeek():
	if isEmpty(): print("Queue_Empty")
	else: return Q[front+1]
```



## Example 1

```python
Q = [0] * 10
front = -1
rear = -1

rear += 1
Q[rear] = 1		# enQueue(1)

rear += 1
Q[rear] = 2		# enQueue(2)

rear += 1
Q[rear] = 3		# enQueue(3)

while front != rear:
    front += 1
    print(Q[front], end = ' ')		#print(deQueue())
```

```python
# python append를 사용한 예 - 느림
listQ = []
listQ.append(1)
listQ.append(2)
listQ.append(3)
while listQ:
    print(listQ.pop(0), end = ' ')
```

```python
# 참고: collections 활용법
from collections import deque

# enqueue -> append
q = deque()
q.append(1)
q.append(2)
q.append(3)

# dequeue -> popleft
q.popleft()
```



## 선형 큐 이용 시의 문제점

### 잘못된 포화상태 인식

배열 앞부분에 활용할 수 있는 공간이 있음에도 rear = n-1: 포화상태로 삽입을 수행하지 않게 됨



#### Sol 1.

매 연산시마다 저장된 원소들을 배열 앞부분으로 이동

// 원소 이동에 많은 시간 소요, 큐의 효율성 극감



#### Sol 2.

1차원 배열을 사용하되, 논리적으로 원형 형태의 큐를 이룬다고 가정하고 사용 (끝에서 되돌아가기)



# 원형 큐

front = rear = 0



front와 rear가 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야

cf. mod 사용: (rear+1) % n



## 원형 큐의 구조

front: 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈 자리로 두기



| 큐      | 삽입 위치 | 삭제 위치 |
| ------- | --------- | --------- |
| 선형 큐 |           |           |
| 원형 큐 |           |           |



enQueue(B)



if (rear+1) % n == front: Full



## 원형 큐의 구현

### 확인

```
def isEmpty():
	return front == rear
def isFull():
	return (rear+1) % len(cQ) == front # rear 다음 칸이 front?
```



### 삽입

```
def enQueue(item):
	global rear
	if isFull():
		print("Queue_Full")			# debug
	else:
		rear = (rear + 1) % len(cQ)
		cQ[rear] = item
```



참고: 그래도 꽉차면? 1. 덮어쓰기 2. 들어온 걸 버리기



### 삭제

```
def deQueue():
	global front
	if isEmpty():
		print()
	else:
		front = (front + 1) % (lencQ)
		return cQ[front]
```

```
def delete():
	global front
	if isEmpty():
		print()
	else:
		front = (front + 1) % (lencQ)
```



# 참조: Linked Queue (연결 큐)

## 단순 연결 리스트를 이용한 큐

* 큐의 원소: 단순 연결 리스트의 노드
* 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있음
* front: 첫번째 노드를 가리키는 링크
* rear: 마지막 노드를 가리키는 링크

### 상태 표현

* 초기 상태: front = rear = null
* 공백 상태: front = rear = null



```python
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n
        
def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode
```



# Priority Queue (우선순위 큐)

* 우선순위를 가진 항목들을 저장하는 큐
* FIFO 순서 대신 우선순위가 높은 순서대로 먼저 나가게 됨

Used in...

* 시뮬레이션 시스템
* 네트워크 트래픽 제어
* 운영체제의 태스크 스케쥴링



배열을 이용한 우선순위 큐 구현



# Applying Queue: Buffer

## Buffer

데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 데이터를 보관하는 메모리 영역

Buffering: 버퍼 채우는 동작



버퍼는 순서대로 입출력, 전달되어야 하므로 FIFO인 Queue가 쓰인다. 



### Example: Keyboard Buffer

User Input >> Keyboard Input Buffer > stdin > Process



### Example 2: Distribution Simulator

1번이 줄을 선다

1번이 1개를 받는다

1번이 다시 줄을 선다

2번이 새로 줄을 선다

1번이 2개를 받는다

1번이 다시 줄을 선다

3번이 새로 줄을 선다

2번이 1개를 받는다

...

20개 중 마지막 것은 누가 가져가는가?



# Breadth First Search (BFS)

그래프 탐색의 두 가지 방법, DFS(깊이 우선 탐색)와 BFS(너비 우선 탐색)



BFS는 탐색 시작점의 인접 정점들을 먼저 모두 차례로 방문,

방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

인접한 정점들에 대해 탐색을 한 후, "차례로" 다시 BFS를 진행해야 하므로 Queue를 사용



cf. Queue[1 | 1인접: 2 3 | 2 인접: 4 5 | 3 인접: 5 | ...] (이미 먼저 줄 서 있나?: )



A-B/C/D, B-E/F, D-G/H/I 일 때....

BFS: A, B, C, D, E, F, G, H, I 순 탐색

DFS: A, B, E, F, C, D, G, H, I 순 탐색



## 예시 입력 파라미터

```
def BFS(G, v):						# 그래프 G, 탐색 시작점 v
	#### 초기화 부분
	visited = [0] * (n+1)			# n: 정점(node) 개수  (1번부터 n번까지 써야지)
	queue = []						# 큐 생성
	queue.append(v)					# 시작점 v를 큐에 삽입
	
	#### 순회 방문
	while queue:					# 큐가 비어있지 않다면
		t = queue.pop(0)				# 큐의 첫번째 원소 반환
		### 중복이 발생할 수 있으므로 Queue의 길이을 결정하는 데 애먹을 수 있는 형태
	
		if not visited[t]:					# 그곳이 방문했던 곳이 아니라면
			visited[t] = True					# 방문한 곳으로 처리
			visit(t)							# 방문해서 해야 할 일 처리
			## indentation 주의
			for i in G[t]:						# t와 연결된 모든 node에 대해...
				if not visited[i]:					# 그 node가 방문한 곳이 아니라면
					queue.append(i)						# 큐에 삽입
```

```
A로 시작:
	Visited[T 0 0 0 0 0 0 0 0]				# A 방문 표시
	Q[B C D]								# A의 인접점 enQueue
탐색 진행:
											# deQueue B
	Visited[T T 0 0 0 0 0 0 0]				# B 방문 표시
	Q[C D E F]								# B 인접점 enQueue
	
	Visited[T T T F F F F F F]
	Q[D E F]
	
	Visited[T T T T F F F F F]
	Q[E F G H I]
	
	Visited[T T T T T F F F F]
	Q[F G H I]
	
	Visited[T T T T T T F F F]				#
	Q[G H I]								#
	
	...
	
	Visited[T T T T T T T T T]
	Q[]
	
Q가 비어있으므로 탐색 종료

'''
While Q:
	deQueue
	visited True
	v 인접 enQueue
'''
```

*해당 구조에 익숙해질 것! (말로 설명할 수 있을 정도로)*



참고: enqueue와 visited 묶어서 처리하기

```
def BFS(G, v):						# 그래프 G, 탐색 시작점 v
	#### 초기화 부분
	visited = [0] * (n+1)			# n: 정점(node) 개수  (1번부터 n번까지 써야지)
	queue = []						# 큐 생성
	queue.append(v)					# 시작점 v를 큐에 삽입
	
	#### 순회 방문
	while queue:					# 큐가 비어있지 않다면
		v <- deQueue()
		do(v)						# do sth
		
		if v에 인접 and 미방문인 모든 w
			enQ(w)
			visited[w] <- 1
			
			
	#### Q의 길이를 node 수만큼 잡으면 되어 편함
```





### Example 3

정점 1~7에 대해

간선: 12, 13, 24, 25, 46, 56, 67, 37

모든 정점을 너비우선탐색하여 경로를 출력하시오. 시작 정점은 1로 시작하시오.

cf. -1-2-3-4-5-7-6





