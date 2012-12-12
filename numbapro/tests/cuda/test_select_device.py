from numbapro import cuda

import unittest
import threading
import numpy as np
def newthread():
    cuda.select_device(0)
    stream = cuda.stream()
    A = np.arange(100)
    dA = cuda.to_device(A, stream=stream)
    stream.synchronize()
    del dA
    del stream
    cuda.close()

class TestSelectDevice(unittest.TestCase):
    def test(self):
        for i in range(10):
            t = threading.Thread(target=newthread)
            t.start()
            t.join()

if __name__ == '__main__':
    unittest.main()