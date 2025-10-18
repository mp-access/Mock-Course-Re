In computer science, we say that a function is *pure* if the following two conditions are met:

 1. The function is referentially transparent
 2. The function has no side effects

You are given several non-pure functions and your task is to convert them into pure functions. You will use unit testing to avoid regressions.

## What is referential transparency?

A function is *referentially transparent* if calling it with the same parameters always returns the same value. Here is an example for a function that is **not** referentially transparent:

```python
def not_transparent(x):
    from random import randrange
    return x + randrange(10)
```

It's not referentially transparent, because repeatedly calling the function with the same parameter, for example `not_transparent(5)`, may produce a different return value every time. The following function, on the other hand, is referentially transparent:

```python
def transparent(x):
    return x + 3
```

No matter how many times you call `transparent(5)`, the return value is guaranteed to always be `8`.

## What are side effects?

A function has side effects, if its execution affects state outside the function scope. For example, the following function has side effects:

```python
def side_effects(l):
    l.append(1)
    return l
```

After a function call to `side_effects`, the parameter `l` will have been modified. Compare it to the following function:

```python
def no_side_effects(l):
    return l + [1]
```

`no_side_effects` produces exactly the **same return value** as `side_effects`, but does not modify the input list `l`.

Before proceeding, make sure you unterstand why this is true, and try out these functions on your own, giving it different lists for `l` and observing how both `side_effects` and `no_side_effects` produce the same result, yet only one of them modifies `l`:

```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l1 == l2 # True
side_effects(l1) == no_side_effects(l2) # True, because same return value
l1 == l2 # False, because side_effects modified l1
```

## What is regression testing?

When your code *used to* work correctly, but now fails for some reason, we call this a *software regression*. Developers write unit tests not only to test new code, but also to ensure that existing functionality doesn't break when making changes. This is called *regression testing* because it mitigates against regressions.

## What is a random seed?

Most "random" numbers on a computer are actually *pseudorandom*. A pseudorandom number generator takes an existing number, called a *seed*, and uses some convoluted math to produce a new, **seemingly** random number. Given the same seed, the pseudorandom number generator will return the same number. See [random.seed()](https://docs.python.org/3/library/random.html#random.seed).

# Implementation step 1: extend regression tests
You are given three examples of *impure* functions in `task/script.py`. Each of these functions returns an expected result, but none of them are pure, for one reason or another. If you run `task/script.py` unchanged, you can see that `sort_and_even(numbers)` correctly returns `[-4, 0, 10, 100]`, but that it also modifies the `numbers` list.

Before you start changing `task/script.py`, **you must first finalize the unit tests in `task/tests.py`**. We provide two tests as a template:

 * `test_sort_and_even_rt` checks whether the function returns the same result every time. It does, so this test succeeds.
 * `test_sort_and_even_no_side_effects` checks whether the function is side-effect-free. It is not, so this test fails.

You will need to create four more similar tests, two for `pseudorandom_float` and two for `drive`. Once you've implemented all six tests, three should fail, and three should succeed.

# Implementation step 2: refactor functions
Once your tests are working as expected, modify each of the three functions so that they

 * still return the same result
 * have no more side effects (if they had any)
 * are referentially transparent (if they weren't)

Be sure to utilize your unit tests to confirm that your modifications are working correctly before submitting.

# Notes
 * 💡 Hint: Writing the additional tests should be easy by drawing from both the existing tests and the code at the bottom of `task/script.py`.
 * 💡 Hint: If you're confused by how to refactor `drive`, remember how immutable objects (such as strings or tuples) are "modified": by creating a new instance with the necessary changes applied.
 * 🧠 Good to know: Text books like to use a more elegant definition of *referential transparency*: An expression is referentially transparent if it can be replaced by its value. This is actually true for many expressions. `(1 + 1)` is a function call (to compute addition), and it is referentially transparent, because it can be replaced by its value `2`, and the opposite is true as well: anywhere you use the value `2`, you could also use the expression `(1 + 1)`, and the meaning would not change. That's referential transparency.
 * 🧠 Good to know: Wikipedia has decent articles on the greater concepts of [referential transpancey](https://en.wikipedia.org/wiki/Referential_transparency), [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)), and [pure functions](https://en.wikipedia.org/wiki/Pure_function).
