import Algs
import Util


a, SR = Util.readwav('allcaps.wav', time=30)
print(a)
elems = set(range(0, 32760))
out = Algs.multiplyElements(a, elems, 5)
print(out)
Util.writewav(out, SR, 'output.wav')
print('done')
