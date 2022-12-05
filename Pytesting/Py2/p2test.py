import unittest
from p2 import sum
n = int(input("Enter the number of elements : "))
list1 = []
for i in range(0, n):
    ele = int(input())
    list1.append(ele)


class TestP2(unittest.TestCase):
      def test_p2(self):
            self.assertEqual(4, sum.sumofnumbers(list1))

if __name__=="__main__":
      unittest.main()