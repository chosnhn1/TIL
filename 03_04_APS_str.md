컴퓨터에서의 문자 표현

글자에 대응하는 숫자를 정해서 메모리에 저장

lower, upper alphabet = 52 < 2^6 (64)



이러한 코드 체계를 통일할 필요성 ++ > 1967년 ASCII 코드

ASCII: 7bit encoding, 128 chars, 33 non-printable / 95 printable

Extended ASCII: 8bit but less compatible



ASCII as world standard, but... 다른 나라들의 언어는?

유니코드 Unicode



유니코드의 Character Set

UCS-2

UCS-4

변수 크기의 정의, but 바이트 순서 표준화 안되면서 외부 인코딩 필요하게 됨

big-endian, little-endian



유니코드 인코딩 (Unicode Transformation Format, UTF)



Python Encoding

* 2.x: 첫 줄에 UTF-8 명시
* 3.x: 생략 가능 (기본이 됨)
* 다른 인코딩 방식이 필요하면 명시해주면 됨



문자열의 분류

String

fixed length

variable length

- length controlled (Java)
- delimited (C)



```python
s1 = 'a b a'
s2 = sl.replace('a', 'd')
s3 = s1.split()

print(s1.isalpha())
```



```python
s1 = 'ab a'
s1[0] = 'B'  # Error
# immutable
```



C는 ASCII

Java는 UTF-16저장

python은 UTF-8



문자열 뒤집기

```python
s = list(input()) # 문자열을 리스트로 저장
```

```python
# len(s)//2 만큼 수행

n = len(s)  # 글자수
for i in range(n//2):
    s[i], s[n-1-i] = s[n-1-i], s[i]
```

C: 위 방식의 알고리즘으로 직접 구현해야

Java: 클래스로 구현

Python: slicing 으로도 가능



```python
cnt = [0] * 26
s = 'aba'
for x in s:
    cnt[ord(x) - ord('a')] += 1
print(cnt)
print(chr(65))

# 소문자 count를 해주는 코드

s = 'aBa'
for x in s:
    if 'a' <= x <= 'z':
        cnt[ord(x)-ord(a)] += 1
    elif 'A' <= x <= 'Z':
        print(x)
    elif '0' <= x <= '9':
        print('숫자')
```



### String Compare: 문자열 비교

C: strcmp() "string compare"

```c
int my_strcmp(const char *str1, const char *str2)
{
    int i = 0;
    while(str1[i] != '\0')
        
}
```



Java: equals() method

Python: ==(\__eq__), is



### ASCII number to Integer

C: atoi(), itoa()

Java: parse

Python: int(), str() repr() float()

*리스트에 별개로 저장된 숫자는 어떻게 변환하지?*



# Pattern Matching

Pattern Matching Algorithms

* Brute Force / Naive Algorithm (Old-school Pattern Search)
  * 1번 찾기...
  * 1번 맞으면 2번 맞나 보기
  * 2번 아니면 다시 1번 찾기....
* Rabin-Karp Algorithm (카프-라빈 알고리즘)
  * 해시값만 비교하다가 해시가 일치하면 실제 패턴 검사
* KMP Algorithm
  * Knuth-Morris-Pratt Algorithm
  * 경계 정보를 활용해서 비교하지 않아도 되는 구간을 패스
* Boyer Moore Algorithm (보이어-무어 알고리즘)



## Brute Force

```
if t[i] = p[j]
	i+=1 j+=1

...
if t[i] != p[j]  #어 틀렸다

	i = i-j+1
	j = 0  # 다시...
	
# ====
p: pattern; t: given string
M = len(p); N = len(t)

def BruteForce(p, t):
	i = 0
	j = 0
	
	while j < M and i < N:  # 인덱스가 벗어나지 않도록
		if t[i] != p[j]:
			i = i - j  # 비교 시작점으로 회귀
			j = -1
			
		i = i + 1 # 이전과 다른 위치
		j = j + 1 # 0
	if j == M : return i - M # 검색 성공, 패턴이 시작되는 인덱스 반환
	else: return -1 # 검색 실패
```



```
for i: 0 -> N-M
    for j: 0 -> M-1
        if p[j] != t[i+j]:
            break
        if j = M-1:
        	return -1
```



최악의 경우 시간복잡도 O(MN)

그럼 어떻게 비교횟수를 줄일 수 있을까?



## KMP Algorithm

불일치 시 알게 된 앞부분에 대해 다시 비교하지 않기

next[M]: 불일치 발생 시 이동할 다음 위치

패턴 전처리로 next[M]를 구해서 그만큼 널뛰기



O(M+N)

패턴 위치별로 매칭에 실패했을 때 돌아갈 자리를 준비

```
next = [0] * M
cnt = 0
i = 1
while i < M:
	if p[i] == p[cnt]
		cnt += 1
		next[i] = cnt
		i += 1
	else:
		if cnt != 0:
			cnt = next[cnt-1]
			
		else:
			next[i] = 0
			i += 1 # 일치된 게 없었으니 그냥 하나씩 가자
```



## Boyer Moore Algorithm

from right to left

Many commercial SWs uses Boyer Moore

1. 오른쪽 끝을 확인
2. 패턴에 있나 확인
3. 보유 여부에 따라 점프 (최대 len(p)만큼 점프)

### example

cf. 'move'의 skip배열

e = 0, v = 1, o = 2, m = 3, 나머지 글자는 4칸을 뛰면 됨



skip배열



보이어 무어는 텍스트를 다 안 봐도 된다 (!)

최악의 경우 O(mn)

일반적으로 O(n)보다 빠르다



## Comparison

m 길이 패턴을 n 길이에서 찾기

| algorithm   | O()   |
| ----------- | ----- |
| Brute-force | O(mn) |
| Rabin-Karp  | O(n)  |
| KMP         | O(n)  |



## 문자열 암호화

Caesar 암호와 암호표

### bit열 암호화

XOR(Exclusive OR) 연산 사용

| x    | XOR (x XOR y) | y    |
| ---- | ------------- | ---- |
| 0    | 0             | 0    |
| 0    | 1             | 1    |
| 1    | 0             | 1    |
| 1    | 1             | 0    |



## 문자열 압축

Run-length Encoding Algorithm

cf. ABBBBBBA : A1B6A1

cf. 허프만 코딩 알고리즘 (Huffman Coding Algorithm)

