# Java만이 가지는 특이점

* Java Virtual Machine: Java를 어떤 기기에서도 실행할 수 있도록 하는 가상 머신
* JVM으로 인한 Multi-platform supports

# Python과의 공통점

* OOP Basis: 본래 객체 지향 프로그래밍 언어로 설계됨
  * 절차형 프로그래밍 언어였던 C에 OOP를 입히는 방식으로 만들어진 C++과의 차이점

* Garbage Collector를 탑재
  * 언어 자체에서 메모리 관리를 수월하게 해 주는 Garbage Collection 기법을 염두에 둔 설계
  * C++은 GC를 위해 라이브러리를 사용해야 함

# Python과의 차이점

* 컴파일 언어
  * 코드 전체를 컴파일하여 실행하는 언어로, 한 줄씩 실행하는 인터프리터 언어인 Python과 차이가 있음
  * 대체로 컴파일 언어가 인터프리터 언어보다 작동이 빠르나, 인터프리터 언어 특유의 높은 생산성과 Trade-off가 있다고 여겨짐
  * 특히 Java는 JVM을 통해 작동하므로, Java가 Python에 비해 성능 우위를 가진다고 하기는 애매함 (이 점은 C++과 비교하는 것이 적당할 것)
* 정적 타입(Statically Typed) 언어
  * 자료 형태(type)를 컴파일 시점에 결정
  * <> 자료 형태를 런타임에서 결정하는 동적 타입
  * Java는 변수에 명시적으로 타입을 부여함
  * Python은 변수에 할당되는 값에 따라 타입이 달라질 수 있음 (동적 타입 Dynamically Typed) 
  * 대체로 Static Typing이 디버깅에서 우위를 보여준다고 여겨지지만 이에 대해서는 여러 이견들 또한 존재한다: 문제는 결국 무엇이 더 좋은 것이냐가 아니고 언제 어떻게 쓰는가이다
  * 참고: 왜 Typescript를 쓰는가?


