log = print

import hashlib


s = 'I love you'.encode('utf-8')

md5 = hashlib.md5('salt'.encode('utf-8'))

md5.update(s)

log(md5.hexdigest())

