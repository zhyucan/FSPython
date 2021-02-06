# import sys
# sys.path.append('/Users/Yucan/Documents/GitHub/FSPython/day18/blog')
#
# from core import src
# import sys
# import os
#
# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

sys.path.append(BASE_PATH)

from core import src

if __name__ == '__main__':
    user = {
        'name': None,
        'status': False,
    }
    src.main(user)

