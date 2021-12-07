print('-------------- début du programme -----------------------')

import unittest

class Task:
    def __init__(self, description):
        self.description = description
        self.status = False 
        # false = todo, true = done

class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)
    def test_statusExist(self):
        task = Task("learn python")
        self.assertEqual(False, task.status)  
    


if __name__ == '__main__':
    unittest.main()