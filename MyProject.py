print('-------------- début du programme -----------------------')

from typing import Counter
import unittest

class Task:
    counter = 0
    def __init__(self, description):
        self.description = description
        self.status = False 
        self.ID = Task.counter
        Task.counter = Task.counter+1 
        # false = todo, true = done
    def setToDone (self):
        self.status = True
    def setToTodo (self):
        self.status = False

def readTheFirstChar (string):
    return string[:1]

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
    def test_IDisUnique(self):
        task1 = Task("learn python")
        task2 = Task("learn TDD")
        self.assertNotEqual (task1.ID, task2.ID)
    def test_setStatusDone (self):
        task = Task("learn python")
        task.setToDone()
        self.assertEqual(task.status, True)
    def test_setStatusTodo (self):
        task = Task("learn python")
        task.setToTodo()
        self.assertEqual(task.status, False)
    def test_ReadTheFirstChar (self):
        head = readTheFirstChar ("+ exemple de commande")
        self.assertEqual(head, "+")


if __name__ == '__main__':
    unittest.main()