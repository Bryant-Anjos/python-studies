from Block import *
from Transaction import *
from ecdsa import SigningKey, NIST384p

genesis = Block(0, '', 1465154705, '5EFADE649896B73D85423254A8A645DD81A97304B15C9E791EC5EF2C4B6B2F60', 0, 0)

bc = Blockchain(genesis)