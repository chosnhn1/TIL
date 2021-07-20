```python
numbers = [1, 2, 3, 4, 5, 6]
*a, = numbers
print(*a)

*a, b = numbers
print(*a, '///', b)

a, *b = numbers
print(a, '///', *b)

a, *b, c = numbers
print(a, '/', *b, '/', c)

a, b, *lista, c = numbers
print(a, '/', b, '/', *lista, '/', c)
```



```python
lunch = ['짜장면', '초밥', '피자']
for idx, menu in enumerate('lunch'):
    print(idx, menu)
    
```

