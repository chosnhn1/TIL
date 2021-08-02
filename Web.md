# HTML

W3C (World Wide Web Consortium)

WHATWG >> 웹 표준 제정의 주도자



HTML: HyperText Markup Language

Hypertext: texts are linked via hyperlinks

HTTP: HyperText Transfer Protocol



```html
<h1>
    Sebastian Vettel
</h1>
Sebastian Vettel is German F1 driver.
<h2>
    Career
</h2>
Sebastian Vettel made his debut in 
```

Markup language: 태그 등으로 문서, 데이터의 구조를 명시하는 언어

프로그래밍 언어는 아니다 (조건, 반복 등 흐름제어 불가)

웹 컨텐츠의 의미와 구조를 정의

*.html



```html
<!doctype html>
<html lang="ko">
    <head>
        <meta charset="UTF-8"
              <title>HTML Document</title>
        머리
    </head>
<body>
    몸통
    
</body>
</html>
```

Open Graph Protocol



Document Object Model (DOM) Tree

DOM provides structured representation of documents

programming languages can access via DOM

"Web page의 object-oriented representation"



Elements

```html
<h1>contents</h1>
```

* tag (usually open-close set)
* contents

디버깅이 좀 어렵다 (따로 오류를 뱉지 않고 페이지 표시만 이상해짐)

elements can be nested



Attributes

```html
<a href="https://www.google.com"></a>
```

Different tags have different attributes

주의: no spaces & doublequotes are convention

* additional infos
* used in starting tags
* HTML Global Attributes
  * id, class, hidden, lang, style, tabindex, title



`<div>`: tag for making structure (semantic)

HTML has new semantic tags: ('야 div 좀 그만 써라')

* header
* nav
* aside
* section
* article
* footer



```html
<div></div>
<div>
    <div>
        
    </div>
</div>
<div></div>
```



```html
<header></header>
<section>
	<article>
        
    </article>
</section>
<footer></footer>
```

semantic, non-semantic tags

non-semantic tags are necessary

semantic tags are recommended, very useful at delivering meanings



Semantic Web

assigning metadata to web pages: Webpage as a Database



Inline and Block

Block: charge all block for room

Inline: take only their spaces



Group Contents

`<p>` `<hr>`

Text Elements

`<b>` vs `<strong>`

`span` div:block vs span:inline



Table tags

직접 구현은 잘 안 쓰이는 추세



Form tags

`<form>`: provide data to server



`<input>`

https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input





# CSS: Cascading Style Sheets

deciding style and layouts of HTML page

```css
h1 {
    color: blue;
    font-size: 15px;
}
```

Selector {Declaration Property: value}



How to styling?

* Inline
* Embedding
* Link file

인라인: 태그 안에서 직접 작성

내부 참조: head 내에 `<style>` 태그로 지정

링크 파일: 외부에 css파일을 만들고 `<link rel="stylesheet">`로 불러오기 (모듈화!)



## Selector: 선택자

HTML 문서에서 특정 요소를 선택하기 위해 사용된다.

* 기본 선택자 ()
* 결합자 (Combinators)
* 의사 클래스/요소 (Pseudo-class)

### 선택자의 종류

**선택의 원칙: 구체적인 것이 우선한다!**

* 기본 선택자
  * 전체 선택자 `*`
  * 요소 선택자
  * 클래스 선택자 `.classname`
  * ID 선택자 `#idname`
  * 속성 선택자

*클래스 선택자는 여러 곳에서 사용할 수 있으나, id 선택자는 단 한 곳에서만 쓰기 (여러 곳에 써도 작동은 하나 convention)*

선택자 사이는 공백으로 구분 `<div class="a b c">`



자식 결합자

`.box > p` "box 클래스의 자식인 p 태그"

자손 결합자

`.box p` "box 클래스의 자손들 중 p 태그"



### Cascading Order: CSS의 적용 순위

내부 우선권 계산: 1. Importance 2. Specificity 3. 

1. `!Important`
   * 개발에 많은 난점을 불러오므로 거의 사용하지 않음
2. Specificity 
   * inline > id selector > class >  > 요소 선택자
3. 소스 선택자



ex. 같은 레벨이라면? 나중에 선언된 것이 우선 (참조하는 순서는 중요하지 않음)



* importance는 거의 안 씀
* id 선택자도 쓰지 않을 것임

(cascade breaker)

* 거의 모든 tag에 class를 적용할 것임



### Inheritance in CSS

CSS는 부모 요소 속성을 전부 자식에게 상속하지 않는다

* 상속됨: text 관련 요소들, ...
* 비상속됨: box model, position 등...



## Metrics in CSS

* Pixel: px
  * Fixed metric
* Percentage: %
  * used in flexible layout

* em
  * related size by inheritance (multiple)
  * ex) 2em = 2 x parent element
* rem
  * related size by root element `<html>`
  * 통일된 비율을 고정하려 할 때 많이 씀
* viewport
  * visible area on device display
  * 웹 컨텐츠의 보이는 영역
  * vw, vh, vmin, vmax



## Colors in CSS

* Color Keywords
  * non-case-sensitive
  * 
* RGB Value
  * `#FFFFFF`
  * `rgb(0, 0, 0)`
  * `rgba(0, 0, 0, 0.5)` 투명도(alpha값)
* HSL Value
  * `hsl()`
  * `hsla()`



Document Representation

Text Manipulation, Color, Background Color, List and Table



## Combinators: 결합자

* 자손 결합자 ` `(space)
* 자식 결합자 `>`
* 일반형제 결합자 `~`
* 인접형제 결합자 `+`

일반형제: A의 형제 중 뒤에 위치하는 모든 B

인접형제: A의 형제 중 바로 뒤에 위치하는 B

```css
div span {
    자손
}
div > span {
    자식
}
div ~ span {
    일반형제
}
div + span {
    인접형제
}
```



## CSS Box Model

CSS constructs All HTML elements by boxes

content padding margin border

[Margin[Border[Padding[Content ~~~]]]]

바깥여백 테두리 안쪽여백 내용

```css
.margin-padding {
    margin: 10px;
    padding: 2px;
}

.border {
    border-width: 2px;
    border-style: dashed;
    border-color: black;
}
```

Box Shorthand

```css
.margin-2 {
    margin: 10px 20px;
}
.margin-3 {
    margin: 10px 20px 30px;
}
.margin-4{
    margin: 10px 20px 30px 40px;
}
```

상하 / 상하-좌우 / 상부터 clockwise

```css
.border {
    border: 2px dashed black;
}
```

non-order-sensitive (`black dashed 2px ;`? OK)



CSS는 넓이를 안쪽 contents 기준으로 잡는다

border, padding이 붙어 늘어나는 것을 감안해야 하는가?

border-box 적용하기 (기준점을 border로 옮기기)

```css
.box-sizing {
    box-sizing: border-box;
}
```

```css
* {
    box-sizing: border-box;
}
```



마진 상쇄

block A의 top과 block B의 bottom에 적용된 각각의 margin이 둘 중 큰 마진 값으로 결합하게 되는 현상

보통 이 현상을 방지하기 위해 한 쪽으로만 margin값을 줌



## CSS Display

Block: 줄 바꿈이 일어나는 요소

div, ul, ol, li, p, hr, form 등

inline: 줄바꿈이 일어나지 않는 요소

line-height로 상하여백을 지정

span a img input label, b, em, i, strong 등



Block

기본은 너비의 100%



속성에 따른 수평 정렬

margin-right: auto; == text-align: left;

좌측 자동마진 = 우측 정렬



inline-block

inline처럼 한 줄에 표시 가능하지만 block처럼 width-height-margin 속성 모두 지정할 수 있다.



none

해당 요소를 화면에 표시하지 않는다. (차지하는 공간 = 0)

(vs. Hidden)



## CSS Position

문서 상에서 요소를 배치하는 방법을 지정한다.

static (default값)

* 일반적인 요소의 배치 순서 (좌측 상단)
* 부모 요소 내에서 배치될 때는 부모 요소 위치를 기준으로

좌표 property: (top bottom left right)

* relative
* absolute
* fixed

### Positioning Methods

* relative
  * 자기 자신의 static 위치를 기준으로 이동
  * 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
* absolute
  * 일반적 문서 흐름에서 제거됨, 레이아웃에서 공간을 차지하지 않게 됨
  * 가장 가까이 있는 non-static 조상 요소를 기준으로 이동 (없다면 body에 할당)
  * 위치를 부모에 맞추고 싶다면? absolute
* fixed
  * 일반적 문서 흐름에서 제거됨, 레이아웃에서 공간을 차지하지 않게 됨
  * viewport만을 기준으로 이동
  * 스크롤 시에도 항상 같은 곳에 위치



```css
.relative {
    position: relative;
    top: 100px;
    left: 100px;
}
```

```css
.parent {
    position: relative;
}
.absolute {
    position: absolute;
    top: 100px;
    left: 200px;
}
```



```css
.fixed {
    position: fixed;
    bottom: 0;
    right: 0;
}
```



absolute를 쓰기 전에 반드시...! 부모를 만들어야 한다

(body에 붙지 않도록)



absolute의 특징:

페이지의 다른 요소의 위치와 간섭하지 않는 격리된 UI를 만드는 데 사용



----

Frontend

인터페이스의 외형



HTML, CSS, JavaScript

* HTML: backbone
* CSS: representation
* JavaScript: movement







Jargons

Vanilla JS: JS dev w/o frameworks

Bootstrap: 

CSS: 계단형 상속(Cascading Style)

SEO: Search Engine Optimization



