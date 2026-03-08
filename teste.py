import sys
sys.path.append("/storage/emulated/0")
from quadrado import quadrado


def main():
   
   test_positivos()
   test_negativos()
   test_zero()
   

def test_positivos():
    num = 1
    mul = 1
    while True:
        assert quadrado(num) == mul * mul
        num += 1
        mul += 1
        
        if num >= 999999:
            break
   
def test_negativos():
    num = 1
    mul = 1
    while True:
        assert quadrado(num) == num * num
        num -= 1
        mul += 1
        
        if num <= -999999:
            break             
 
def test_zero():
    assert quadrado(0) == 0             
    
if __name__ == "__main__":
   main()
 
     