#!/usr/bin/env python
#  將 data 轉換成一維陣列
# 不可以使用list slice
answer = None
data = [ [1,2,3,4,5], [6,7,8,9,10], [11,12,13, [100,200, 300, 400, ['FOO'] ], 14,15] ]
assert answer == [1,2,3,4,5,6,7,8, 9,10, 'A', 11,12,13, 100, 200, 300, 400, 'FOO', 14,15], answer
