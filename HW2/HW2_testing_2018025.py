import unittest
from HW2_2018025 import minFunc


class testpoint(unittest.TestCase):
	def test_minFunc(self):
		
		#4 variable kmap 
		self.assertEqual(minFunc(4,"(0,1,2,3,4,5,6,7) d-"),'final expression: w\'')
		
		#4variable kmap
		self.assertEqual(minFunc(4,"(2,3,5,6,7,10,11,13,14) d-"),"final expression: x\'y+xy\'z+yz\'+w\'y" )
		
		#4variable kmap
		self.assertEqual(minFunc(4,'(0,4,8,10,11,12,13,15) d-'),'final expression: y\'z\'+wx\'y+wxz')
		
		#3 variable kmap
		self.assertEqual(minFunc(3,'(0,1,2,3,7) d-'),'final expression: w\'+xy')
		
		#4 variable kmap with dont cares
		self.assertEqual(minFunc(4,'(1,3,7,9,11,15) d(0,2,5)'),'final expression: x\'z+yz') 
		
		#3 variable kmap w
		self.assertEqual(minFunc(3,'(0,1,2,3,4,5) d-'),'final expression: w\'+x\'')
		
		#4 variable kmap with dontcare
		self.assertEqual(minFunc(4,'(2,4,5,6,10) d(12,13,14,15)'),'final expression: yz\'+xy\'')
		
		#4 variale kmap with all choices 1
		self.assertEqual(minFunc(4,'(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) d-'),'1')
		
		#3 variable kmap wit all options 1
		self.assertEqual(minFunc(3,"(0,1,2,3,4,5,6,7) d-"),'1')
		
		#two variable kmap
		self.assertEqual(minFunc(2,'(0,1) d(2)'),'final expression: w\'')





		
                
if __name__=='__main__':
	unittest.main()
