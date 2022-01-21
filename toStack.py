from pydoc import doc
from stack import Stack
from crane import Crane

import random
import numpy as np


def ToStack(input):
    n = 0
    stackArray = []
    for x in input:
        stackArray.append( Stack(int(input(n)), n+1) )

    return stackArray