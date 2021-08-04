# CSS Flexbox Layout

Display / Position / Float / Flexbox / Grid System / Table Layout / Multiple-column layout



## Float Recap

### float

* 본래는 썸네일식 이미지 삽입을 위해 도입됨
* 점차로 웹 사이트의 전체 레이아웃을 그리는 데에 활용하게 됨
* none / left / right: 기본값, 왼쪽 띄우기, 오른쪽 띄우기

참조: x-index

### float clear

윗쪽 요소에 float 적용: 아래 요소들이 딸려올라가면서 구조가 깨짐

그럼 어떻게...? 딸려올라가지 않도록 투명한 block 요소를 삽입

```css
.clearfix::after {
    content: "";
    display: block;
    clear: both;
}
```



float / flexbox / grid layout

float는 새 기술들에 역할을 이전하고 현재 본래 기능으로 돌아가는 추세

MDN "legacy layout"

여전히 float로 레이아웃을 짜는 경우도 있음



## flexbox

한계가 많은 float를 대체하기 위해 도입됨

인터페이스 내 요소들의 공간배분과 정렬에 쓰이는 단방향 레이아웃

* 요소: Flex Container / Flex Item (부모 / 자식)
* 축: main axis / cross axis (메인축 / 교차축)

축 시작지점 : 왼쪽 / 위쪽이 시작 (기본값)



### 컨테이너 / 아이템

container는 display: flex 혹은 inline-flex로 받아 설정됨

정렬 컨트롤을 container가 수행

item은 container의 컨텐츠



flex에 적용하는 속성

배치 방향 설정

flex-direction

메인축 방향 정렬

justify-content

// justify-self

// justify-content

교차축 방향 정렬

align-items

align-self

align-content

기타

flex-wrap

flex-flow

flex-grow

order

// flex-shrink

// flex-b



flex-direction

main axis를 설정

* row (기본값): 좌-우
* row-reverse : 우-좌
* column :상-하
* column-reverse : 하-상

justify / align

각각 main axis, cross axis 정렬



align-content: 여러 줄을 동시 정렬

align- items: 한 줄을 정렬

align-self: 요소 하나를 정렬



flex-wrap

* nowrap (기본값): 내용물이 넘쳐도 강제로 한 줄을 유지
* wrap: 내용물이 넘치면 보일 수 있게 다음 줄로 넘김
* wrap-reverse: 내용물이 넘치면 cross축의 반대 방향으로 넘김



flex-direction&wrap의 shorthand

```css
.container {
    flex-flow: column wrap;
}
```



justify-content

* flex-start: 기본값, main axis의 시작지점에 붙여서
* center: 가운데 정렬
* flex-end: main axis의 끝지점에 붙여서
* space-between: 양쪽 정렬
* space-around: 좌우 균등 정렬
* space-evenly: 내외 등간정렬



align-items:

* stretch: 기본값
* flex-start
* center
* flex-end



align-self:

주의: 해당 자식 요소에 적용

* auto: 기본값
* flex-start
* center
* flex-end
* ...



```css
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
```



참고: baseline



order: 자식 요소에 순서 부여

* 0: 기본값
* 1, 2, 3...: 순서에 따라 차순위로 밀림
* -1 -2: 앞으로 미는 방법 (음수값)

grow: main 축에서 남은 공간을 배분

주의: 원래 공간 + 남은 공간의 비율 배분이므로

배분받고 난 공간 비율을 grow 비율로 혼동하지 말 것





justify-items, justify-self?

: 불필요 (margin auto); W3C 문서 참조

'그거 margin으로 다 돼!'



## sum

부모에서 display: flex

참조: inline-flex

기본값:

item은 row로 나열, flex-start에서 시작, stretch, nowrap으로 설정



