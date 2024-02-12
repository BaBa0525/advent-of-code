# Day1

## 3.12

```py
num_regex = f"(?=([0-9]|{"|".join(number_letters)}))"
```

Python 3.12 allows double quotes in f-strings.

## regular expressions

### Raw string

We can use `r"..."` to create a raw string. This is useful when we want to use backslashes in our string without having to escape them.

```py
r"\d"
```

### `re.compile`

We can use `re.compile` to compile a pattern, which is faster while reusing it multiple times.

### Lookahead

We can use `(?=...)` to match a pattern only if it is followed by another pattern. It's worth noticing that lookahead doesn't consume any characters, which is useful when matches are overlapping.

```py
num_regex = f"(?=([0-9]|{"|".join(number_letters)}))"
```
