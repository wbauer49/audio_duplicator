import Algs
import Util


a = Util.readwav('allcaps.wav')
print(a)
elems = [i**2 for i in range(256)]
out = Algs.deleteElements(a, elems)
Util.writewav(out)
