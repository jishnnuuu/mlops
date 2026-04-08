import hashlib

data = "version 1 data".encode()
md5_hash = hashlib.md5(data).hexdigest()

print(md5_hash)