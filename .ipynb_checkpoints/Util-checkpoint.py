import numpy as np
import scipy.io.wavfile as spwav


seconds = 10
fftlen = 128
SR = -1


def readwav(path, LR=False):
    SR, stereo = spwav.read(path)
    print(stereo)
    if LR:
        return stereo[:seconds*SR, 0], stereo[:seconds*SR, 1]
    else:
        mono = np.average(stereo, axis=1)
        return mono.astype(np.int16)[:seconds*SR]

def writewav(path, array):
    spwav.write(path, SR, array)


def FFT(array, fftlen):
    samps = array.size
    hanning = np.hanning(fftlen)

    ret = np.zeros((samps - fftlen, fftlen))
    for i in range(samps - fftlen):
        window = array[i:i+fftlen] * hanning
        ret[i] = np.fft.fft(window)
    return ret

def invFFT(trans, fftlen):
    samps = array.size
    hanning = np.hanning(fftlen)
    
    ret = np.zeros(samps)
    for i in range(samps - fftlen):
        window = np.real(np.fft.ifft(b2[i]))
        ret[i:i+fftlen] += window * hanning
    ret = ret * 32767 / max(c)
    return ret.astype(np.int16)
