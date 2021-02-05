log = print

import sys

# log(sys.path)

# log(__file__)
import os

log(os.path.dirname(__file__))

sys.path.append(os.path.dirname(__file__) + '/tt')

# log(sys.path)


from t import *


def read1():
    log('adsf')


# read2()

