* AJAX
* Asynchronous JavaScript 
  * Callback functions
  * Async callbacks
  * Promise
* Axios



----

Last...

Event, ECMAScript Syntax



# AJAX

**Asynchronous JavaScript and XML** - 비동기식 JavaScript와 XML

서버와 통신하기 위해 XMLHttpRequest 객체를 활용

JSON, XML, HTML, 일반 text 형식 등을 포함한 다양한 포맷을 주고받음

현재는 JSON이 



## Features of AJAX

* 페이지 전체를 새로고침하지 않아도 수행되는 "비동기성"
  * 사용자 event가 있으면 전체 페이지가 아닌 일부분만을 업데이트할 수 있음
* AJAX ables...
  * 페이지 새로고침 없는 서버 요청
  * 서버로부터 데이터 받아 작업 수행



비동기식이 아니라면... 트래픽 ++++





## Birth of AJAX

2005년 Google Maps, Gmail 등에 활용되는 기술을 설명하기 위해 만들어진 용어

(메일 전송 중 페이지 전환, 지도 상 스크롤로 지도만 갱신 등)

AJAX는 기술 자체가 아닌 접근법을 의미



## XMLHttpRequest Object

* 서버와 상호작용하기 위해 사용
* 전체 페이지 새로고침 없이 데이터를 받아올 수 있음
* 사용자 작업을 중단하지 않고도 페이지 일부를 업데이트할 수 있음
* 주로 AJAX 프로그램에 사용
* 이름과 달리 모든 종류의 데이터를 받아올 수 있음
* 생성자 `XMLHttpRequest()`



어떤 함수가 종료될 때 XMLHttpRequest가 반환된다면...? 감 잡기



## XMLHttpRequest Sample

```javascript
const request = new XMLHttpRequest()
const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
request.open('GET', URL)
request.send()

const todo = request.response
console.log(`data: ${todo}`)

// 전달 X
```



## 동기식과 비동기식

"기다릴까?"

> 주의: Python은 반드시 동기식, JavaScript는 반드시 비동기식으로 동작하는가?

* 동기식: 순차적, 직렬적 동작 수행
  * 대기 요인이 발생하면 기다리기 때문에 비효율이 발생하나, 결과는 확실함
  * JavaScript에서의 예시
    * 버튼 이벤트 - 경고 메시지를 누르기 전까지 이후 코드가 실행되지 않고 대기
  * JavaScript: Single-threaded
* 비동기식: 응답을 기다리지 않고 다음 코드 실행
  * 유휴 시간이 없지만 기대하지 않은 방식으로 동작할 수도 있음
  * JavaScript에서의 예시
    * 이전 예시 코드: 변수 todo에 응답 데이터가 할당되는 것을 기다리지 않고 빈 문자열 출력
  * 역시 JavaSccript: Single-threaded



> 동기식 처리를 주로 사용하는 분야로 금융이 있다.
>
> 입금 / 출금 과정이 비동기식으로 이루어지면 어떤 일이 일어날까?



그렇다면 왜 비동기를 사용하는가?

* User Experience
* 매우 큰 데이터를 동반하는 앱에서는...
  * 동기식 코드라면 데이터를 모두 불러온 뒤 앱이 실행됨
  * 따라서 사용자 경험에 지장 초래 (응답 없음?)
* 비동기식 코드라면 데이터 R&R과 앱 실행을 함께 진행
  * 지속적으로 응답하는 화면을 보여줌
* 현재 많은 웹 API 기능은 비동기 코드를 사용하여 실행됨



* 참고: Threads



### Blocking vs. Non-Blocking



### Conclusion

"JavaScript is Single-threaded"

JavaScript는 한 개의 Call stack으로 Event를 처리

* 즉시 처리하지 못하는 Event를 Web API로 보내서 처리하도록 함
* 처리된 Event는 Task queue에서 대기
* Call Stack이 비면 Event Loop(담당자)가 Task queue의 front에 위치한 Event를 Call stack으로 보냄



----



## Concurrency Model

* Call Stack
  * 요청이 들어올 때 해당 요청을 순차적으로 처리하는 Stack 형태의 자료구조
* Web API (Browser API)
  * JavaScript Engine이 아닌, Browser 영역에서 제공하는 API
  * setTimeout(), DOM Events 등 시간이 걸리는 작업
* Task Queue
  * 비동기 처리된 callback 함수가 대기하는 Queue 형태의 자료구조
  * Main Thread가 종료된 후 실행, 후속 JavaScript 코드가 차단되는 것을 방지
* Event Loop
  * Call Stack이 비어있는지 확인
  * 비어 있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
  * Task Queue에 대기 중인 callback 함수가 있다면, 가장 앞에 있는 callback 함수를 call stack으로

> setTimeout(, 3000)은 3초 뒤에 출력하라는 의미일까?
>
> : 3초 뒤에 task queue로 이동
>
> cf. Zero Delay

#### Zero Delays

setTimeout에 0초를 주더라도, 0ms 후에 callback 함수가 시작된다는 의미가 아님

실제 실행 시간은 task queue에 대기 중인 작업의 갯수에 따라 다르다



### 순차 비동기 처리

Web API로 들어오는 순서는 중요하지 않고, 어떤 event가 먼저 처리되느냐가 중요

이 때 실행 순서가 불명확해짐

이를 해결하려면...

1. Async callbacks: 비동기 콜백
   * 백그라운드에서 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
   * i.e addEventListner()의 두번째 인자
2. promise-style
   * Modern Web APIs에서의 새로운 코드 스타일
   * XMLHttpRequest 객체를 사용하는 구조보다 조금 더 현대적



# Callback Function

* 다른 함수에 인자로 전달된 함수
* 외부 함수 내에서 호출되어, 일종의 루틴 혹은 작업을 완료
* 동기식, 비동기식 모두 사용됨
  * 단, 비동기 콜백이 많이 사용됨
* 비동기 작업이 완료된 후 코드 실행을 계속하는 데 사용되는 경우를 '비동기 콜백(asynchronous callback)'이라고 함



## First Class Object

"JavaScript의 함수는 First Class Object이다"

* 인자로 넘길 수 있어야
* 함수의 반환값으로 사용할 수 있어야
* 변수에 할당할 수 있어야



## Async Callbacks

* bg에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
* 백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 작업이 완료되었음을 알리거나, 다음 작업을 실행하게 할 수 있음
  * i. e. addEventListener()의 두번째 매개변수
* callback 함수를 다른 함수의 인자로 전달할 때, 함수의 body에서 called back
  정의된 함수는 특정 시점에 callback 함수를 실행하게 됨



### Why we use callback

* callback 함수는 명시적 호출이 아닌, 특정 routine 혹은 action에 의해 호출
* django의 경우 "요청이 들어오면", event의 경우 "특정 event가 발행하면"
  * 이것이 가능한 것은 callback function 개념 때문에 가능



## callback Hell

* 순차적인 연쇄 비동기 작업을 처리하기 위해 다음의 패턴이 지속적으로 반복됨
  * callback 호출
    * 그 다음 callback 호출
      * 그 다음 callback 호출... (연쇄 비동기 작업)
* "callback hell"
* 이 경우 디버깅이 힘들어지고 코드 가독성이 떨어짐

해결책

* Keep your code shallow
* Modularize
* Handle every single error
* Promise callbacks



## Promise

Promise Object: 비동기 작업의 최종 완료 혹은 실패를 나타내는 객체

* 미래의 완료 또는 실패와 그 결과값을 나타냄
* 미래의 어떤 상황에 대한 약속
* 성공: `.then()`
* 실패(거절): `.catch()`

```javascript
axios.get(URL)
  .then(function (response) {
    console.log(response)
    return response.data
  })
  .then(function (data) {
    return data.title
  })
  .then(function (title) {
    console.log(title)
  })
  .catch(function (error) {
    console.log(error)
  })
  .finally(function () {
    console.log('this will be executed.')
  })
```

* `.then(callback)`
  * 이전 작업이 성공했을 때 
  * 각 callback 함수를 이전 작업의 성공 결과를 인자로 전달받음
* `.catch(callback)`
* `.finally(callback)`
  * Promise 객체를 반환
  * 결과와 상관없이 무조건 지정된 callback 함수가 실행
  * 어떤 인자도 전달받지 않음
  * `.then()`과 `.catch()`의 중복작업을 위해 사용됨



* 각각의 .then() block은 서로 다른 promise를 반환
  * `.then()`을 여러개 사용하여 연쇄 작업을 수행할 수 있음
  * 여러 비동기 작업을 차례대로 수행 가능
* .then()과 .catch()는 모두 promise()를 반환하기 때문에 chaining 가능
* 단, 반환값이 반드시 있어야 함
* 반환값이 없다면 다음 함수가 사용할 promise 객체가 없음
* 



## What Promise Secures

* Callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call stack을 완료하기 이전에는 절대 호출되지 않음
* 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
* `.then()`을 여러 번 사용하는 Chaining 가능



# Axios

"Promise based HTTP client for the brower and Node.js"

사용 시 설치 필요: [Axios Github](https://github.com/axios/axios)

브라우저를 위한 Promise 기반의 클라이언트

XHR보다 편리한 AJAX 요청이 가능하도록 해줌

provide extensible interface and handy library



# Appendix: Async & Await

비동기 코드를 작성하는 새로운 'syntactic sugar' (ES8부터 사용)

Promise의 then chaining을 제거하고, 비동기 코드를 동기 코드처럼 표현

```javascript
async function fetchDogImage(URL) {
    const res = await axios.get(URL)
    const breed = Object.keys(res.data.message)[0]
    const dogImages = await axios.get(``)
    console.log(dogImage)
}

URL = 
```



# Conclusion

> "Human-centered Design w/ UX"
>
> Jesse James Garrett



----

[참고 사이트 Loupe](http://latentflip.com/loupe)

[참고 사이트 jsv9000](https://www.jsv9000.app/)

