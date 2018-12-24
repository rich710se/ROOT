
```python
"""Append dict to dict."""
DICT = ['192.168.2.1', '192.168.2.2']
NEW_KEYS = ['192.168.1.1', '192.168.2.2', '192.168.1.3',
            '192.168.2.4', '192.168.1.5', '192.168.1.6']

for key in NEW_KEYS:
    if key not in DICT:
        print('adding' + key)
        DICT.append(key)
    else:
        print('skipping' + key)
print(DICT)
```