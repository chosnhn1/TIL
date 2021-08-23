# Stack

자료를 누적하는 선형 구조



* 선형 구조: 자료 간 1대1 관계
* 비선형 구조: 자료 간 1대N 관계

스택에 자료를 삽입, 꺼낼 수 있음.

마지막 자료가 먼저 호출됨: 후입선출(LIFO)



## Stack의 구현

필요 자료구조와 연산:

* 구조
  * C에서는 Array 사용
  * 저장소 자체를 stack이라 부르기도
  * 마지막 삽입된 위치를 top이라 부름
* 연산
  * push: 삽입
  * pop: 삭제(삽입역순)
  * isEmpty: 공백확인
  * peek: top 반환(확인)



### 삽입 / 삭제 과정

Array[0], [1], [2], ... [초기 크기]

top = -1

```
push
> top += 1
> Array[top] <- A

push
> top += 1
> Array[top] <- B

pop
> Array[top] out -> B
> top -= 1

#############################

push(n)
    top += 1
	stack[top] = n

pop()
	t = stack[top]
    top -= 1
    return t

pop()
	top -=1
	return stack[top+1]

#########################

stack이 다 찼는데 push
stack이 비었는데 pop 등의 상황도 구현해야

pop에서 지우는 동작을 별도로 구현하지 않아도 괜찮음
(push시 덮어쓰기)
```

top as 'stack pointer'

#### stack의 push 알고리즘

```
def append():
	
```



#### stack의 pop 알고리즘

```
def pop():
	if len(s) == 0:
		# underflow
		return
	else:
		return s.pop(-1);
```

검사: 디버깅 용도로 보게 될 것

미리 검사



구현 시 주의사항

* 1차원 배열 사용 시
  * 구현 용이
  * 크기 변경 난항
* 동적 연결리스트로 구현
  * 구현 복잡
  * 메모리 효율적 사용



## Stack 응용

### 1. 괄호검사

Conditions

* 좌괄호 / 우괄호 갯수
* 왼쪽 괄호 는 오른쪽 괄호보다 먼저
* 괄호 사이에는 포함관계만 가능



구현

```
if (     (   ㅑ == 0  )    ) && (  j == 0  )
```

여는 괄호: push

닫는 괄호: pop하여 비교

종료 시 스택에 괄호가 남았다면? 오류

아직 닫는 괄호가 남았는데 스택이 비었다면 오류



#### Summary

* open parenthesis
  * push
* close par
  * pop and compare
* not matching: X Con3
* empty stack: X Con1 or Con2
* stack remains: X Con1



### 2. Function Call

함수 호출/복귀 수행순서 관리

* 마지막 호출이 먼저 실행됨 (LIFO)
* 함수 수행에 필요한 변수들, 복귀 주소 등을 Stack Frame에 저장해서 System Stack에 삽입
* 함수 종료 시 System Stack의 top 원소를 pop하면서, Frame의 복귀 주소를 참조하여 복귀
* 전체 수행이 종료되면? System Stack이 빎



참고: 재귀 함수와 Stack 구조



#### 재귀호출

자기 자신을 호출하여 순환 수행

작업특성에 따라 일반적 호출방식보다 프로그램 크기를 줄이고 간단하게 작성 가능. ex) factorial

재귀호출: 같은 모습이지만, 다른 함수를 내부에서 호출하는 것과 비슷하다



##### 예시

fact(4) = 4 * fact(3)

fact(3) = ...

fact(1) return 1

factorial n=4인 경우의 실행 순서

0. fact(4)
1. fact(3) 호출
2. fact(2) 호출
3. fact(1) 호출
4. return 1
5. return 2
6. return 3



호출을 할지, 중단을 할지 두 부분으로 나누어져 있어야

```
def f(n):
	if ~~~ :
		return A
	else:
		f(n-1)
```



Python은 재귀깊이가 정해져 있음: 1000

*알고리즘 접근 시 1000번이 넘어가는 깊이라면 접근방식이 잘못되었을 수 있음*



##### 피보나치 수열

```python
def fibo(n):
    if n < 2 :
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

갈라져나오는 재귀호출의 예시







## Memoization

재귀호출 예시(피보나치)에서 

```python
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append()
```





----

# Dynamic Programming (DP)

동적 계획 알고리즘

입력 크기가 작은 부분 문제를 먼저 해결하고, 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결, 최종적으로는 원래 주어진 입력의 문제를 해결하는 알고리즘



## Dynamic Programming in Fibonacci Example

fibo(n) = fibo(n-1) + fibo(n-2)

전체 문제가 부분 문제들의 합으로 이루어짐



1) 부분 문제로 나누기
2) 가장 작은 부분문제부터 해를 구함
3) 그 결과를 테이블에 저장, 부분 문제 해를 활용하여 상위 문제의 해를 구한다



```
def fibo2(n):
	f = [0, 1]
	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2])
	
	return f[n]
```



```python
def fibo(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
        
    return table[n]

n = int(input())
table = [0] * [n+1]
print(fibo(n))
```

## DP의 구현

recursive / iterative

memoization + 재귀보다 반복구조로 DP를 구현하는 것이 성능효율적

Why? 시스템 호출 스택을 사용하는 overhead 발생



```python
def factorial(n):
    # f(n) = n * f(n-1)
    # f(0) = f(1) = 1
    # f(2) = 2 * f(1), f(3) = 3 * f(2) = 3 * 2 * f(1), ...
    table[0] = 1
    for i in range(1, n+1):
        table[i] = i * table[i-1]
    
    return table[n]

n = int(input())
table = [0] * (n+1)

print(factorial(n))

```



공식을 찾기

Memoization? DP? 단순반복?



# Depth First Search (DFS, 깊이 우선 탐색)

그래프 구조 which is 비선형구조: 모든 자료를 빠짐없이 검색하는 것이 중요

(자료 간 일대다 복잡한 연결관계)

* 깊이 우선 탐색 (Depth First Search, DFS)
* 너비 우선 탐색 (Breadth First Search, BFS)



시작점 한 방향으로 경로가 있는 곳까지 탐색 > 갈 곳이 없게 됨 > 가장 마지막 갈림길 정점으로 되돌아와 다른 방향의 정점으로 탐색을 계속 반복 > 모든 정점을 방문

가장 마지막에 만난 갈림길로 돌아가 깊이 우선 탐색을 반복: Stack을 사용가능함

* 정점 = node, vortex
* 간선 = edge
* '인접'의 방향이 있는지 주의

1. 시작 정점 v를 결정하여 방문
2. 정점 v에 인접한 정점 중...
   1. 방문하지 않은 정점 w가 있다면:
      v를 스택에 push하고 w를 방문, w를 v로 삼아 2를 반복
   2. 방문하지 않은 정점이 없다면:
      탐색 방향을 바꾸기 위해 스택을 pop, 가장 마지막 방문 정점을 v로 해 다시 2를 반복
3. 스택이 빌 때까지 2를 반복



#### Example

```
visited[], stack[] initialize
DFS(v):
	v visit;
	visited[v] <- True;
	do {
		if (v의 인접 node 중 search not visited)
			push(v);
			while(w){
				w visit;
				visited[w] <- True;
				push(w);
				v <- w;
				v의 인접 정점 중 방문 안한 w 찾기
			}
				
	}
```

AB, AC, BD, BE, CE, DF, EF, FG w/ stack, visited

1. A visit, 
2. push(A); B visit; visited[B] <- true
3. push(B); D visit; visited[D] <- true
4. push(D); F visit; visited[F] <- true
5. push(F);  G visit; visited[G] <- true
6. push(E); C visit; visited[C] <- true
7. w 소진
   pop(stack);
8. pop(stack);
9. push(F); G visit; visited[G] <- true

A-B-D-F-E-C-G



*참고*: 인접행렬, N,M (a, b) (노드 엣지 정보 전달)

```python
V, E = map(int, input().split())
ad = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    ad[n1][n2] = 1
    ad[n2][n1] = 1
```

```python
def dfs(s, V):
    visited = [0] * (V+1)
    stack = []
    visited[s] = 1
    i = s  # visiting node i
    visited[i] = 1  # True
    print(node[i])
    
    while i != 0:  #True
        for w in range(1, V+1):  # determine w
            if adj[i][w] == 1 and visited[w] == 0:
                print(node[w])
                stack.append(i)  # route stacked
                i = w  # move to visited node
                visited[w] = 1
                break
                
            else:
                if stack:
                    i = stack.pop()
                else:
                    # break
                    i = 0
                    
    
    
```





----



재귀를 이용한 배열 접근

e. g. "배열 A에 2가 들어 있으면 1, 아니면 0":

```
f(N, v):
	for i: 0 -> N
		if A[i] == v:
			return 1
	else:
		return 0
```

```
f(i, N, V):
	if i == N:
		# 중지
		# 배열에 V가 없는 경우
		return 0
	elif A[i] == V:
		# 배열에 V가 있는 경우
		return 1
	else:
		# 남은 원소 있으며, V를 아직 찾지 못함
		f(i+1, N, V)
		
```



최적화되지 않은 라이브러리들의 특징:

함수호출이 과하게 쌓임