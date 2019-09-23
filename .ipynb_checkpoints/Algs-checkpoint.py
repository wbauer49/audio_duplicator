


def deleteElements(array, elements):
    ret = np.zeros(array.shape)
    i = 0
    for samp in array:
        if samp in elements:
            ret[i] = samp
            i += 1
    return ret[:i]

def multiplyElements(array, elements, mult):
    arrlen = array.shape
    ret = np.zeros(max(arrlen, arrlen*mult))
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
    ret = np.zeros(array.shape)
    for i in range(array.shape):
        ret[i] = wavetable[array[i]]
    return ret
