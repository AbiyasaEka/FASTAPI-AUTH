import hashlib

result = hashlib.md5('solution'.encode())

print(result.hexdigest())
