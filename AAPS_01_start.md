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
- ...



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



