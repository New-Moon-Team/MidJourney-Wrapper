import hashlib

def get_md5(string):
    hash_md5 = hashlib.md5(string.encode())
    return hash_md5.hexdigest()
