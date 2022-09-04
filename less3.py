import hashlib
s = 'papa'
N = len(s)

def func():
    my_hashes = set()
    strings = set()
    for i in range(len(s)):
        for j in range(len(s) + 1):
            res = (s[i:i + j - 1])
            if res:
                res = hashlib.sha256(res.encode()).hexdigest()
                my_hashes.add(res)
                # strings.add(s[i:i + j - 1])
    return len(my_hashes)
    # print(strings)
    # print(my_hashes)
print(func())