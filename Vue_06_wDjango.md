Vue.js w/ django

# Server & Client

Client

* Request service to server
* Send corresponding parameters, forms, ...
* Represent response for user



# CORS

## Same-Origin Policy (SOP)

* Policy prevents interactions: 특정 origin에서 불러온 script 등이 다른 출처에서 가져온 resource와 interact하는 것을 방지하는 정책
* 잠재적 공격 위험 방지
* 두 URL의 Protocol, Port, Host가 모두 같아야 동일한 출처라 할 수 있음



## Cross-Origin Resource Sharing (CORS)

* 교차 출처 자원 공유
* 추가 HTTP Header >> 특정 출처에서 실행 중인 web app이 다른 origin의 resource에 access할 수 있는 auth 부여하도록 browser에 알려주는 체제
* If origin (Protocol + Port + Host) is different: CO Http Request
* 보안 문제로 브라우저는 Cross-origin HTTP request를 제한 (SOP)
* 올바른 CORS Header를 포함한 response를 해야



"CORS Policy"

서버에서, 어떤 호스트에서 자신의 컨텐츠를 불러갈 수 있는지 지정



## Using CORS

`Access-Control-Allow-Origin` 등

해당 응답이 주어진 출처로부터 요청 코드와 공유될 수 있는지

cf. `Access-Control-Allow-Origin: *`



### Case

1. Vue.js에서 A Server로 요청
2. A Server: ACAO에 특정한 origin을 포함시켜 응답
3. 브라우저는 ACAO 확인 후



`django-cors-headers` 라이브러리



----

참고: CORS deals with SOP Problem

SOP로 방어할 수 있는 리디렉션 해킹 (cf. Phishing)

[SOP(MDN Document)](https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy)

Backend에서 어떤 출처를 신뢰하는지 CORS 설정



Postman에서 처리되는 요청이 Browser에서 처리가 안 된다면? 브라우저의 SOP 때문일 수 있다



----

# Authentication & Authorization

(Revisited)

## Authentication

* 인증
* `401 Unauthorized`

## Authorization

* 권한 부여
* 보안 환경에서 Authorization은 Authentication을 따라야 함
* Authenticated라고 해서 Authorization이 되는 건 아님
* `403 Forbidden`



# JWT

## Authentication / Authorization Methods

* Session Based
* Token Based
  * JWT Token
* Authentication Platform



### 참고: Session Based

Cookie, Session in state-less Web



## Json Web Token: JWT

* JSON 포맷을 활용한 안전한 정보교환 표준 포맷

* Self-contained JWT

  * 별도 인증수단 필요없음
  * 자체 인증 필요 정보가 모두 갖기 때문

* 

  

Data + 인증 정보



* HTML, HTTP 환경에서 사용하기 용이
* 인증수단 자체의 보안 수준이 높음
* JSON 범용성
* Server Memory에 정보를 저장하지 않아 Server 자원 절약 가능



## JWT Structure

. 연산자를 통한 구분

Header.Payload.Signature



* Header
  * type and hashing algorithm
* Payload
  * data of token
* Signature
  * encoding value and hash



Logout?



### Comparison

|                      | Session          | JWT                   |
| -------------------- | ---------------- | --------------------- |
| 인증수단 저장 위치   | Server           | Client                |
| 인증수단 정보 민감성 | Low (Session ID) | High (Self-Contained) |
| 유효 기간            | Y                | Y                     |
| 확장성               | Less             | More                  |



`set_password()`

* 암호 해싱 처리: 사용자의 암호를 문자열 데이터로 설정
* User 객체를 저장시키지는 않음



참조: Hashing



