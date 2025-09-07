#Matrix. 


#Write a class that can represent any 2𝑥2 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1 -------> mnozenie
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

class Matrix():
    def __init__(self, row1, row2):
        self.row1 = row1
        self.row2 = row2

    def sum(self, row1, row2, row1v2, row2v2):
        for el in self.row1:
            i=0
            row1v2[i] = row1[i] + row1v2[i]
            i = i+1

        for el in self.row2:
            i=0
            row2v2[i] = row2[i] + row2v2[i]

        print(row1v2, row2v2)

    def dot_scalar(self, row1, row2,):

        print(row1, row2)
        row1v2= row1[0]*row2[0]
        row2v2 = row1[1] * row2[1]
        scalar = row1v2 + row2v2

        print("dot scalar: ",scalar)



matrix1 = Matrix([1,2,3], [4,5,6])
matrix2 = Matrix([11,22,33], [44,55,66])

matrix1.sum([1,2,3], [4,5,6], [11,22,33], [44,55,66])
matrix2.dot_scalar([1,2], [3,-5])