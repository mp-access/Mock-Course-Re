The following table contains the sizes for T-shirts in the US market. The intervals are defined
in mathematical notation, "()" meaning "non-inclusive" and "\[]" meaning inclusive.

| Chest (cm) | Size |
| ---------- | ---- |
| \[80, 90]  | XS   |
| (90, 98]  | S    |
| (98, 104] | M    |
| (104, 111]| L    |
| (111, 124]| XL   |

Write a program that determines the right T-Shirt size for a given measurement of the chest circumference. The measurement in cm is provided in a `float` variable called `circumference`. The size of the T-Shirt is calculated by a function called `get_size` and your task is to complete the function.

Please make sure that your solution is self-contained within the `get_size` function. That is, only change the body of the function, not the code outside the function. Your function is expected to return the right size in a string.

For invalid sizes (i.e., measures outside the limits stated in the table), return `"N/A"` as the size.

