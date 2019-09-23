import numpy as np
import scipy.io.wavfile as spwav


seconds = 1


def readwav(path, time=-1, LR=False):
	SR, stereo = spwav.read(path)
	if time == -1:
		num_samps = stereo.size
	else:
		num_samps = time * SR

	if LR:
		return stereo[:num_samps, 0], stereo[:num_samps, 1] 
	else:
		mono = np.average(stereo, axis=1)
		return mono.astype(np.int16)[:num_samps], SR

def writewav(array, SR, path):
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
