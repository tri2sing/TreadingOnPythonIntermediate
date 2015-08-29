'''
Created on Jul 24, 2015

@author: Sameer Adhikari
'''

from operator import setitem

# Convert all the values in a dictionary to string

data01 = { 'count': 0,
          'sum': 1
        }

data02 = { 'count': 0,
          'sum': 1
        }

def update_dict(d, k, v):
    d[k] = v

print(data01)
[update_dict(data01, k, str(v)) for k, v in data01.items()]
print(data01)

print(data02)
[setitem(data02, k, str(v)) for k, v in data02.items()]
print(data02)
