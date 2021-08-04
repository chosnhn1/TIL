# Bootstrap

"The most popular HTML, CSS and JavaScript library in the world"

* Twitter에서 시작된 Open-source Front-end Library
* 거의 대부분의 요소 내장
* 다양한 브라우저, 디바이스에서 접속할 때 표시될 디자인(Cross-browsing)에 소요되는 시간 대폭 감소
* One-source Multi-use
* 반응형 웹 디자인 (Responsive Web Design)





reset & normalize

user-agent style



### Normalize / Reset CSS

user agent stylesheet를 초기화 (브라우저마다 다르게 표시하는 것을 초기화)

Normalize CSS: W3C 표준 기준으로 맞추되, 요건을 불충족하는 브라우저 기준으로 맞춘다.

Reset CSS: 브라우저 기본 설정을 다 날린다. 여러 문제가 있어 잘 쓰이지는 않는다. (not recommended)



## Initializing Bootstrap

1. 파일 받기
2. CDN

#### Content Delivery (Distribution) Network



#### Responsive Web Design

웹 디자인에 대한 접근 방식

* Media Queries
* Flexbox
* Bootstrap Grid System
* Viewport Meta Tag



## Grid System

12 Column / 6 Default Responsive Tiers

Flexbox로 제작된 시스템

container, rows, column을 통한 컨텐츠 배치와 정렬

* 12개의 Column
* 6개의 Grid breakpoints



### class

row: columns의 wrapper (반드시 row의 자식은 column)

gutters: 반응적인 column 사이의 padding

col, col-*



### Grid breakpoints

특정 px 조건에 대한 지점이 정해져 있음: viewport 단위에 따라 px을 사용



