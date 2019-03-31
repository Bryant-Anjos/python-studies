import unittest
from Block import *
from Transaction import *
from ecdsa import SigningKey, NIST384p

class initTest(unittest.TestCase):
    def hash(self):
        self.assertEqual(calculateHash(0, '', 1465154705, [], 0, 0), '5EFADE649896B73D85423254A8A645DD81A97304B15C9E791EC5EF2C4B6B2F60')

    def verifyAmount(self):
        amount = 100
        listUtxo = []

if __name__ == '__main__':
    unittest.run()


