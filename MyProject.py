print('-------------- début du programme -----------------------')

import unittest

class Task:
    def __init__(self, description):
        self.description = description
        self.status = False 
        self.ID = 0
        # false = todo, true = done

class Test(unittest.TestCase):
    def test_taskExist(self):
        task = Task("learn python")
        self.assertEqual("learn python", task.description)
    def test_statusExist(self):
        task = Task("learn python")
        self.assertEqual(False, task.status)  
    def test_IDExist(self): 
        task = Task("learn python")
        self.assertGreaterEqual (task.ID, 0)


if __name__ == '__main__':
    unittest.main()