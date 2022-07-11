# Breadth First Search
# Depth First Search

# 1.

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""

N, M, V = map(int, input().split())
# N: nodes, M: edges, V: starting point

# 주어진 정보로부터 인접행렬 만들기
ADJ = [[0] * (N+1) for _ in range(N+1)]
for m in range(M):
    start, end = map(int, input().split())
    # 양쪽으로 다 갈 수 있음에 주의
    ADJ[start][end] = 1
    ADJ[end][start] = 1

# DFS 수행할 수 있는 Stack 만들기
stack = [0] * (M * M)
stack_i = -1    # -1이면 빈 스택

# 시작 지점을 먼저 넣어주자
# for n in range(N+1):
#     if ADJ[V][n] == 1:
#         stack_i += 1
#         stack[stack_i] = (V, n)

# 스택이 빌 때까지 돌아보자
# 이미 방문한 노드는 다시 평가할 필요가 없으므로 방문한 노드를 어떤 방식으로든 표시할 필요가 있다
visited = [0] * (N+1)
while stack_i > -1:

    # 스택에서 빼기
    stack[stack_i] = 0
    stack_i -= 1
    pass