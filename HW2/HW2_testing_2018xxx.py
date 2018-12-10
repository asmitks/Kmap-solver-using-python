import unittest
from final import minFunc



# class testpoint(unittest.TestCase):
	# def test_minFunc(self):


stringIn=input("enter the expression here:")
numVar=int(input("enter the number of variables in kmap"))

minFunc(numVar,stringIn)
		
                
if __name__=='__main__':
	unittest.main()
