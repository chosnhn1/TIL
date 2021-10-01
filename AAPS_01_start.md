# Applied APS



# Software Problem Solving

요즘 강조되는 요소: 재사용성



What if SPS Capability?: Constructing Big Picture w/ languages, data structures and libraries





PS Strategies

Intuition and Systemic Approaches

Intuition is also important, but...

Training w/ systemic approaches

- backwards?
- downwards?
- 비슷한 문제?
- 단순한 방법?
- 문제의 단순화?
- 그림으로 그려볼 수 있을까?
- 수식으로 표현할 수 있을까?
- 문제를 분해할 수 있을까?
- 뒤에서부터 



# (Time) Complexity

Different algorithms to a single problem

Spatial Efficiency / Time Efficiency



Asymptotic Notation of Time Complexity

점근적 표기: when input size n become huge... (infinite)

* big O
* big Omega Ω
* Big Theta Θ



## Analyzing Time Complexity

### Big-O

점근적 상한 ()

연산량의 최대(최악의 경우)를 결정하는 차수만을 남겨서 표기

O(n) = n^2: "실행시간이 n^2에 비례한다"

### Big-Ω

점근적 하한()

### Big-Θ

When Big O = Big-Ω, that is Big-Θ



### Frequently Used Big-O

* O(1): Constant Time
* O(logn): Logarithmic time
* O(n): Linear time
* O(nlogn): Log-linear time
* O(n^2): Quadratic time
* O(n^3): Cubic time
* O(2^n): Exponential time



# Standard I/O

Python 3's Standard I/O

* Input
  * raw: input()
    * All input values are regarded as str
  * eval: eval(input())
    * Input values will be evaluated
    * not recommended (for security)
* Output
  * print()
    * Print values w/ last "\n"
  * print('text', end='')
  * print('%d' % number)
    * Output formatting





* file input/output

  * ```python
    import sys
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    
    text = input()
    print(text)
    ```

  * 



# Bit Operators

| Operator | Function                              |
| -------- | ------------------------------------- |
| &        | AND op per bit                        |
| \|       | OR op per bit                         |
| ^        | XOR op per bit                        |
| ~        | invert bit (monadic operator like +-) |

XOR를 어떻게 써먹을 수 있을까?

반전과 비교

AND: 특정 bit를 0으로 만들고 싶다!

OR: 특정 bit를 1로 만들고 싶다!

XOR: bit의 비교와 toggle

~: toggle all bits (invert)



| Operator | Function                                               |
| -------- | ------------------------------------------------------ |
| <<       | move bit columns of operand to left<br />i.e. num << 2 |
| >>       | move bitcolumns of operand to right<br />i.e. num >> 2 |

01001000 << 2: 00100000 (n번 2를 곱하는 효과)

01001000 >> 2: 00001010 (n번 2를 나누는 효과)



1 << n

* 값은 2^n
* 원소가 n개인 모든 부분집합의 수





i & (1 << j): i의 j번째 비트가 1인가 아닌가?

0: 0이다

not 0: 1이다



----



```python
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
        print (output)
        
        
    for i in range(-5, 6):
        print('%3d = '%i, end='')
        
```



```python
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output, end='')
    
a = 0x10
x = 0x01020304  # 4byte

print('%d = '%a, end='')
Bbit_print(a)
print()

print('0%X = '%x, end='')
for i in range(0 4):
    Bbit_print((x >> i*8) & 0xff)
```

16진수 한 자리 = 4bit

그럼 16진수 두 자리는? 1byte!

masking





## Endianness

엔디안: memory 등 1차원 공간에 여러개의 연속된 대상을 배열하는 방법

HW architecture마다 다름

cf. `x = 0x01020304`

* Big-endian
  * 큰 단위가 앞에 나오는 방식
  * 네트워크에서 많이 쓰임
* Little-endian
  * 작은 단위가 앞에 나오는 방식
  * 데스크탑 컴퓨터에서 쓰임

|               | 0x1234 | 0x12345678  |
| ------------- | ------ | ----------- |
| big-endian    | 12 34  | 12 34 56 78 |
| little-endian | 34 12  | 78 56 34 12 |
|               |        |             |

```python
import sys
print(sys.byteorder)
```

```python
def ce(n): # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p

x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)
    
print('x = %d%d%d%d'%(p[0], p[1], p[2], p[3]))
p = ce(x)
print('x = %d%d%d%d'%(p[0], p[1], p[2], p[3]))
```

```python
def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)


```



# 진수

2진수, 8진수, 10진수, 16진수, ...

from 10진수: 해당 수로 나누어 나머지를 거꾸로 읽기

MSB(Most Significant Bit) / LSB(Least Significant Bit)

i.e

149(10 )= 10010101(2) = 225(8) = 95(16)





## Negative Integer with Bits

보수: Compliment

1's compliment

부호와 절대값으로 표현된 값을, 부호 비트를 제외한 나머지 비트에 대해 0은 1로, 1은 0으로 변환한다.

+6: 0 000 0000 0000 0110

-6: 1 000 0000 0000 0110 부호와 절대값 표현식

-6: 1111 1111 1111 1001 # 1의 보수 표현 (전부 반전)

(여기에 6을 더하면, 모두 1인 결과가 나온다)

(여기에 1을 더하면 자릿수 바뀜)

1의 보수의 단점: -0이라는 값이 생겨버림 



2's compliment

1의 보수 방식으로 표현된 값의 최하위 비트에 1을 더한다

-6: 1111 1111 1111 1010 # 2의 보수 방식으로 표현



2의 보수 형식으로 음수를 표현하면 부호를 따로 관리하지 않아도 연산할 수 있다!



## Real Number: 실수

0.0001(2) = 0.0625



1001.0011(2) = 

1 0 0 1 . 0 0 1 1

2^3, 2^0, 2^-3, 2^-4



컴퓨터는 실수를 표현하기 위해 부동소수점(floating-point) 표기법을 사용

1001.0011 = 1.0010011 * 2^3



IEEE754

단정도 실수 (32bit)

[부호 1bit / 지수 8bit / 가수 23bit]

배정도 실수 (64bit)

[부호 1bit / 지수 11bit / 가수 52bit]

가수부 mantissa: 유효자릿수를 부호화된 고정소숫점으로 표현

지수부 exponent: 실제 소수점의 위치를 승으로 표현



단정도 실수의 지수부는 어떻게 만들지?

음수 표현을 위해 익세스 표현법 사용







example: [1001.0011] 만들기

| 부호          | 지수부                           | 가수부                                  |
| ------------- | -------------------------------- | --------------------------------------- |
| 0<br />(양수) | 10000010<br />(소숫점의 위치: 3) | 00100110000000000000000<br />(10010011) |

[0 10000010 00100110000000000000000000]



컴퓨터는 실수를 근사적으로 표현:

이진법으로 표현 불가능한 실수는 근사값으로 저장되기 때문에, 이 과정에서 발생하는 오차가 계산 과정에서 영향을 미칠 수 있다.

a = b ? (X)

abs(a - b) < 1e-6 ? (이런 식으로...)

비교뿐만 아니라, 함수/프로그램 내에서 오차가 계속 누적되는 방식으로 작동하면 문제가 생길 수 있으므로 이 점도 고려하여야 한다.



실수 자료형의 유효자릿수

32bit > 6

64bit > 15



### Python의 Real Number Range

Python은 더 많은 bit를 사용해서 더 넓은 범위의 실수를 표현

Python Max: 약 1.8 * 10^308, 이 이상은 inf로 표현

Python Min: 약 5.0 * 10^-324, 이 이하는 0으로 표현



----



