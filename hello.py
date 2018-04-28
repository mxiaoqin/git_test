import  unittest




class TestDiv(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001(self):
        self.assertEqual(div(1,1),1)

    def test_002(self):
        self.assertRaises(ZeroDivisionError,div,1,0)

def div(a,b):
    return a/b

if __name__=='__main__':
    unittest.main(verbosity=2)