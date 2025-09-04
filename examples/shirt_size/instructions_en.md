The following table contains the sizes for T-shirts in the US market. The intervals are defined
in mathematical notation, "()" meaning "non-inclusive" and "\[]" meaning inclusive.

| Chest (cm) | Size |
| ---------- | ---- |
| \[80, 90]  | XS   |
| (90, 98]  | S    |
| (98, 104] | M    |
| (104, 111]| L    |
| (111, 124]| XL   |

Write a function `get_size` that returns the right T-Shirt size  for a given measurement of the chest circumference. The measurement in cm is provided as a `float` variable called `circumference`. For invalid sizes (i.e., measures outside the limits stated in the table), return `"N/A"` as the size.

