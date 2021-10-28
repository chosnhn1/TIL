# JavaScript: an Introduction



Server >> Response w/ HTML, CSS & JS >> Browser >>



## Why do we use JavaScript?

동적인 브라우저 화면: 브라우저를 조작할 수 있는 유일한 언어



# A Brief History of JavaScript

[Sir Timothy John Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee)

[Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich)



## JavaScript in Browser War

Netscape Navigator (NN) "Mocha"

Mocha > LiveScript > JavaScript (1995)

Microsoft's Internet Explorer "JScript"

Google's Chrome



Cross-Browsing and Web Standard





## Standard-Making

1996 Netscape

ECMA International >> ECMAScript 1

the 'rule' of JS

2015 JavaScript ES6+: "Next-gen of JavaScript"

Increased Usage of Vanilla JavaScript



----



# Document Object Model: DOM

## Browser Actions

* DOM Control
  * HTML Control
* BOM Control
  * Control Browser Objects
* JavaScript Core (ECMAScript)
  * Data Structure(Object, Array), Conditional Expression, Iteration



## DOM

* Document Programming Interface
* Logical Tree Model
* Every Element as Object
* Attribute, Method, Language features
* Main Objects
  * window
  * document
  * navigator, location, history, screen



Parsing

## DOM Manipulation

2-step

1. Select
2. Manipulation



#### Inheritance Structure

* EventTarget
* Node
* Element
  * Usual class
* Document
  * Web Page, DOM entry point
* HTMLElement
  * All types of HTML elements



### Selection

Methods

* `Document.querySelector(selector)`
  * Receive CSS selector
  * Return first element
  * nothing? = Return NULL
* `Document.querySelectorAll(selector)`
  * Receive CSS selector
  * Can Receive many selectors
  * Return NodeList
* `getElementById(id)`
* `getElementByTagName(name)`
* `getElementsByClassName(names)`



무엇을 반환하는가?

단일 element

* querySelector

HTMLCollection

* `getElementByTagName(name)`
* `getElementsByClassName(names)`

NodeList

* querySelectorAll



#### HTMLCollection vs. NodeList

HTMLCollection

* name, id, index 속성으로 각 항목에 접근 가능

NodeList

* index로만 접근 가능
* 배열에서 사용할 수 있는 다양한 함수, 메서드 사용 가능



### append DOM

* `Element.append()`
  * 
* `Node.appendChild()`
* 



### property

* `Node.innerText`
  * 
* `Element.innerHTML`
  * return HTML Markup
  * caution: XSS

cf. XSS (Cross-site Scripting)



### Delete DOM

* `ChildNode.remove()`
  * Node가 속한 트리에서 해당 Node를 제거
* `Node.removeChild()`
  * DOM에서 자식 Node 제거하고, 제거된 Node 반환



----





* JavaScript만이 할 수 있는 일들
* Node.js
* MERN (MongoDB, Express.js, React.js, Node.js)

Machine Language > Compiler / Interpreter > Programming Language

JS Engine

[참고: HTMLCollection,NodeList](https://devsoyoung.github.io/posts/js-htmlcollection-nodelist)

유사배열



참고: 가변배열로서의 Python List (주소가 들어가는 배열)



----



DOM 선택: Collection

* Live Collection
  * 문서가 바뀔 때 실시간 업데이트
  * HTMLCollection, NodeList등
* Static Collection
  * 





# Event

네트워크 활동, 사용자와의 상호작용 등 사건의 발생을 알리기 위한 객체

* 마우스 클릭, 키보드 입력 등 사용자 행동을 통해 발생
* 특정 메서드 호출을 통해서도 발생 가능



## Event Handler: `addEventListener()`

`EventTarget.addEventListener()`

* 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
* 이벤트를 지원하는 모든 객체를 대상으로 지정할 수 있음

`target.addEventListener(type, listener[, options])`

* type
  * 반응할 이벤트 유형
* listener
  * 알림받을 객체 (대개 함수)



## Event Cancel: `preventDefault()`

현재 이벤트의 기본 동작을 중단

`Event.preventDefault()`

"이벤트를 취소할 수 있는 경우", 이벤트의 전파를 막고



단, 취소할 수 없는 이벤트들 또한 있음

i.e. scroll

event.cancellable 값으로 취소가능한지 확인할 수 있음







----

참고

ASI: Automatic Semicolon Insertion

JavaScript는 자동으로 세미콜론을 삽입



JS Coding Style Guide: 합의된 원칙과 일관성 하에 작성

cf. Google의 스타일 가이드, Airbnb의 스타일 가이드



