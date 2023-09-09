#!/bin/python3

import main
import unittest
import os
from colorama import Fore

unittest.TestLoader.sortTestMethodsUsing = None


class CustomTestSuite(unittest.TestSuite):
    def __init__(self):
        # Add test methods in the desired order
        tests = [
            TestPyShell("test_create_file_1"),
            TestPyShell("test_create_folder_2"),
            TestPyShell("test_mv_3"),
            TestPyShell("test_cp_4"),
            TestPyShell("test_rm_5"),
            TestPyShell("test_rmdir_6"),
        ]
        super().__init__(tests)


class TestPyShell(unittest.TestCase):
    def test_create_file_1(self):
        file_path = "test1.txt"
        file_path2 = "test2"
        file_path3 = 1234
        file_path4 = True
        file_path5 = "test5/test5.txt"

        main.create_file(file_path)
        main.create_file(file_path2)
        main.create_file(file_path3)
        main.create_file(file_path4)

        self.assertTrue(os.path.exists(file_path) and os.path.isfile(file_path))
        self.assertTrue(os.path.exists(file_path2) and os.path.isfile(file_path2))
        self.assertTrue(
            os.path.exists(str(file_path3)) and os.path.isfile(str(file_path3))
        )
        self.assertTrue(
            os.path.exists(str(file_path4)) and os.path.isfile(str(file_path4))
        )
        self.assertRaises(NameError, main.create_file, file_path5)

    def test_create_folder_2(self):
        folder_path = "test5"
        folder_path2 = "test6.txt"
        folder_path3 = 7890
        folder_path4 = False

        main.create_folder(folder_path)
        main.create_folder(folder_path2)
        main.create_folder(folder_path3)
        main.create_folder(folder_path4)

        self.assertTrue(os.path.exists(folder_path) and os.path.isdir(folder_path))
        self.assertTrue(os.path.exists(folder_path2) and os.path.isdir(folder_path2))
        self.assertTrue(
            os.path.exists(str(folder_path3)) and os.path.isdir(str(folder_path3))
        )
        self.assertTrue(
            os.path.exists(str(folder_path4)) and os.path.isdir(str(folder_path4))
        )

    def test_mv_3(self):
        path1a = "True"
        path2a = "True.txt"
        path1b = "False"
        path2b = "Folder"
        path1c = "1234"
        path2c = "numbers.txt"

        main.mv(path1a, path2a)
        main.mv(path1b, path2b)
        main.mv(path1c, path2c)

        self.assertTrue(os.path.exists(path2a) and os.path.isfile(path2a))
        self.assertTrue(os.path.exists(path2b) and os.path.isdir(path2b))
        self.assertTrue(os.path.exists(path2c) and os.path.isfile(path2c))

    def test_cp_4(self):
        path1 = "True.txt"
        path2 = "!False.txt"
        path3 = "Folder"
        path4 = "copy_of_Folder"
        path5 = "numbers.txt"
        path6 = "nums"

        main.cp(path1, path2)
        main.cp(path5, path6)

        self.assertTrue(os.path.exists(path1) and os.path.isfile(path2))
        self.assertRaises(IsADirectoryError, main.cp, path3, path4)
        self.assertTrue(os.path.exists(path5) and os.path.isfile(path6))

    def test_rm_5(self):
        path1 = "True.txt"
        path2 = "test2"
        path3 = "test1.txt"
        path4 = "nums"
        path5 = "numbers.txt"
        path6 = "!False.txt"
        path7 = "Folder"

        main.rm(path1)
        main.rm(path2)
        main.rm(path3)
        main.rm(path4)
        main.rm(path5)
        main.rm(path6)
        main.rm(path7)

        self.assertFalse(os.path.exists(path1))
        self.assertFalse(os.path.exists(path2))
        self.assertFalse(os.path.exists(path3))
        self.assertFalse(os.path.exists(path4))
        self.assertFalse(os.path.exists(path5))
        self.assertFalse(os.path.exists(path6))
        self.assertFalse(os.path.exists(path7))

    def test_rmdir_6(self):
        path1 = "7890"
        path2 = "test5"
        path3 = "test6.txt"
        path_cr = "a.txt"

        # NameError
        main.rmdir(path1)
        main.rmdir(path2)
        main.rmdir(path3)

        main.create_file(path_cr)
        self.assertRaises(NameError, main.rmdir, path_cr)
        main.rm(path_cr)

        self.assertFalse(os.path.exists(path1))
        self.assertFalse(os.path.exists(path2))
        self.assertFalse(os.path.exists(path3))


if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(), defaultTest="CustomTestSuite")
