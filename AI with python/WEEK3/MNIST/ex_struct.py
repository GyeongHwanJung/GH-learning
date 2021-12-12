"""
FileName: ex_struct.py
DESC : struct 모듈 실습
"""
import struct

# 문자열 => 바이너리 쓰기 & 읽기 -----------------------
mytext='Good Luck'
with open('mytest.bin', mode='wb') as file:
    file.write(mytext.encode(encoding='utf-8'))

with open('mytest.bin', mode='rb') as file:
    data = file.read()
    print(data.decode(encoding='utf-8'))

# 수치데이터 => 바이너리 쓰기 & 읽기 -------------------
#struct.pack(fmt, v1, v2,...) : bytes로 변환
data=struct.pack('iid', 1, 2, 3.)            # int float float
print('type(data) = {}'.format(type(data)))
print('data => {}'.format(data))

# 바이너리데이터 => 수치데이터 쓰기 & 읽기 -------------------
#(v1, v2, ...) =struct.unpack(fmt, v1, v2 ...) : 수치데이터로 튜플 타입 변환
(i,x,y)=struct.unpack('iid', data)
print('type(data) = {}'.format(type(data)))
print('data => {},{},{}'.format(i, x, y))
