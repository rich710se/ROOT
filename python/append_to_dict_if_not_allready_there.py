
dict = ['192.168.2.1','192.168.2.2']
new_keys = ['192.168.1.1','192.168.2.2','192.168.1.3','192.168.2.4','192.168.1.5','192.168.1.6']

for key in new_keys:
  if key not in dict:
    print('adding' + key)
    dict.append(key)
  else:
    print('skipping' + key)
print(dict)
