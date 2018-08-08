# 99 Bottles

```python
"""
99 Bottles of Beer.
"""
from time import sleep
for num in range(99, 0, -1):
    if num > 1:
        print(str(num) + " bottles of beer on the wall, " + str(num) + " bottles of beer.")
        if num >2:
            suffix = str(num -1) + " bottles of beer on the wall."
        else:
            suffix = str(num) + " bottle of beer on the wall."
    elif num == 1:
        print(str(num) + " bottle of beer on the wall, " + str(num) + " bottle of beer.")
        suffix = "no more beer on the wall!"
    print("Take one down, pass it around, " + suffix)
    print("--")
    sleep(2)
```