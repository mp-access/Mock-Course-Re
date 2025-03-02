What would the following snippet print?

```python
x = [1, 2, 3]
y = [4, x, 5]
x.append(y)
def prepend(head, l):
    l.insert(0, head)
    return l
print(prepend(y, x)[0][1][2])
```

