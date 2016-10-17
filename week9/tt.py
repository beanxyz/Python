import os, hashlib


def get_size(start_path='c:\\temp'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


dir1 = "c:/temp/Junos.msi.zip"
dir2 = "C:\\Users\yli\pycharmprojects\Exercise\week9\FTP Assignment\\ftproot\ccc\junos.msi.zip"
a = md5(dir1)
b = md5(dir2)
print(a, b)
