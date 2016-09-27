import hashlib

obj = hashlib.md5(bytes('1111', encoding='utf-8'))
obj=hashlib.md5()
# obj.update(bytes('123', encoding='utf8'))
# # obj.update(bytes('456',encoding='utf8'))
# obj.update(bytes('123456',encoding='utf8'))
#
#
# result = obj.hexdigest()
# print(obj)
# print(obj.digest())
# print(result)

#

#
# def md5(fname):
#     hash_md5 = hashlib.md5()
#     with open(fname, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()
#
# dd=md5('index.py')
# print(dd)
#
# with open('index.py','r+') as f:
#     for line in f:
#         print(line)


f=open('index.py','r+')