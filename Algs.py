import numpy as np


def deleteElements(array, elements):
    ret = np.zeros(array.size, dtype=np.int16)
    i = 0
    for samp in array:
        if samp not in elements:
            ret[i] = samp
            i += 1
    return ret[:i]

def multiplyElements(array, elements, mult):
    ret = np.zeros(max(1, mult) * array.size, dtype=np.int16)
    i = 0
    for samp in array:
        if samp in elements:
            for j in range(mult):
                ret[i] = samp
                i += 1
        else:
            ret[i] = samp
            i += 1
    return ret[:i]

def waveshape(array, wavetable):
    ret = np.zeros(array.shape, dtype=np.int16)
    for i in range(array.shape):
        ret[i] = wavetable[array[i]]
    return ret
