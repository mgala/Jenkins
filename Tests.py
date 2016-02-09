from csv1 import *
from unittest import TestCase

__author__ = 'Mateusz Gala'
class Tests(TestCase):
    def setUp(self):
        self.csv = csv1()
        self.f1 = self.csv.openfile("Book1.csv", "rt")
        self.f2 = self.csv.openfile("Book2.csv", "rt")

        self.d1 = self.csv.dialekt(self.f1)
        self.d2 = self.csv.dialekt(self.f2)

        self.r1 = self.csv.read(self.f1, self.d1)
        self.r2 = self.csv.read(self.f2, self.d2)

        self.out = self.csv.mergefiles(self.r1, self.r2)

        self.read_test = ['1', '2', '3', 'zweite zeile']
        self.out_test = [['1', '2', '3', 'zweite zeile'], ['1', '2', '3',]]
        pass

    def test_open_file(self):
        self.assertRaises(FileNotFoundError, self.csv.openfile, "irgendwas.csv", "rt")

    def test_read_file(self):
        reader = self.csv.read(self.f1, self.d1)
        for row in reader:
            assert(row == self.read_test)

    def test_append_files(self):
        out = self.csv.mergefiles(self.f1, self.f2)
        for row in out:
            assert(row == self.out_test)

    def test_write_file(self):
        self.assertRaises(TypeError, self.csv.outputfile, "wrongType", "semicolon", self.out)

    def test_close_file(self):
        self.assertRaises(AttributeError, self.csv.close_file, "wrongAttribute")