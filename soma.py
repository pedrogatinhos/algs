import unittest

def soma(array, ac=0):
    if array == []:
        return ac
    else:
        pop = array.pop(-1)
        ac =  ac + pop
        return  soma(array, ac)

class TestSoma(unittest.TestCase):
    def test_soma_1(self):
        self.assertEqual(soma([1, 2, 3]), 6)

    def test_soma_2(self):
        self.assertEqual(soma([-1, 0, 1]), 0)

    def test_soma_3(self):
        self.assertEqual(soma([10, -5, 3]), 8)
        

if __name__ == '__main__':
    unittest.main()
