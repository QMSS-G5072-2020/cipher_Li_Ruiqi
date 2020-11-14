from cipher_rl3167 import __version__
from cipher_rl3167 import cipher_rl3167

def test_version():
    assert __version__ == '0.1.0'
    
def test_for_not_alphabet():
    expected = '!ee'
    actual = cipher_rl3167.cipher('!dd',1,True)
    assert actual == expected