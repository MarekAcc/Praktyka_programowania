import unittest

def add(a):
    if a == "":
        return 0
    
    numbers = a.replace('\n', ',')
    numbers = numbers.split(',')

    for number in numbers:
        if number == "":
            return -1
    
    for number in numbers:
        if int(number) < 0:
            return -1
    

    return sum(int(number) for number in numbers)

class TestMyMethods(unittest.TestCase):

    def test_Empty_String(self):    
        self.assertEqual(add(""), 0)
    def test_One_number(self):
        self.assertEqual(add("4"), 4)
    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
    def test_negative_number(self):
        self.assertEqual(add("1,-3"), -1)
    def test_many_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)
        self.assertEqual(add("0,0,12,1,2"), 15)
    def test_newline(self):
        self.assertEqual(add("1\n2,3,4"), 10)
    def test_many_newlines_commas(self):
        self.assertEqual(add("1\n2,3,"), -1)
        self.assertEqual(add("1\n2,3\n,"), -1)




if __name__ == '__main__':
     unittest.main()
