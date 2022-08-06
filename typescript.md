# TypeScript

## Syntax

```javascript
const user = {
	name: "Chris",
	age: 30
}
```

```js
const user: {name: string, age: number} = {
	name: "Chris",
	age: 30
}
```

```js
interface User {
	name: string
	age?: number
}
	
const user1: User = {
	name: "Chris",
	age: 30
}
	
const user2: User = {
	name: "Brian",
	age: 25,
}
```


```js
class User {}
interface IUser {}
interface UserInterface {}
```


```js
let page: string | number = 1
let isError: boolean | null = null
```

```js
type ID = string | null;

interface UserInterface {
	id: ID
}

const ids: ID[] = ["asdf1234", "asdf4312", "aaaa2222"]
const idsEmpty: ID[] = []
```


## `void`, `any`, `never`
```js
const sayHello = (): void => {
	console.log("hello")
}
```

```js
let sth: any = "hehe you silly one"
// why you use TypeScript when you also use any?
```

```js
const neverEnds = (): never => {
	console.log("hello?")
	throw "never"
}
```

```js
let aAny: any = 1
let aUnknown: unknown = 10

let aAny = "hello"
let aUnknown = "world" // it will give you an error

console.log(aAny.hello())
console.log(aUnknown.hello()) // this also be an error
```

```js
let bUnknown: unknown = 10
let bNew: string = bUnknown as string

let wow: string = "1"
let numberWow: number = (wow as unknown) as number
```

```js

```
