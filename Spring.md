# Java Spring Framework

Java 플랫폼의 오픈소스 애플리케이션 프레임워크

* 경량 컨테이너로서 Java Object를 직접 관리
* POJO(Plain Old Java Object) 방식 Framework: 가벼운 객체
* DI(Dependency Injection: 의존성 주입)
* IoC(Inversion of Control: 제어역전)
* MVC 구조
* AOP(Aspect-Oriented Programming: 관점 지향 프로그래밍) 지원
* 높은 확장성
* iBATIS / Hibernate 등 데이터 영속성 관리 ORM 등 다양한 서비스 제공

전자정부 표준 프레임워크의 기반 기술로 사용되고 있음

참고: 왜 스프링인가?
https://spring.io/why-spring

---

Framework의 특징

* 모듈화
  * 참고: 캡슐화 (Encapsulation): 클래스 내의 변수들을 외부 접근으로부터 은닉
* 재사용성
* 확장성
  * 참고: 다형성(Polymorphism): 단일한 수행에 대해 각각의 객체들이 고유 방법으로 응답
  * i.e. `1+2` and `'안녕'+'하세요'`
* IoC (제어역전, 제어의 역흐름)
  * 원래 개발자가 관리 / 통제해야 했을 객체들을 프레임워크가 제어
  * 생산성 향상