print('-------------- début du programme -----------------------')

import unittest

class Task:
    def __init__(self, description):
        self.description = description

class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)
    


if __name__ == '__main__':
    unittest.main()