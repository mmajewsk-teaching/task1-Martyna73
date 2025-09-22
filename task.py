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
    def __init__(self, arg):
        self.arg = arg
        self.jacie = 'gacie'

    def __add__(self, other_matrix):
        summed_matrix = [[], [], []]
        if type(other_matrix) == int:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    #print(type(self.arg), type(other_matrix))  # other_matrix.jacie
                    the_sum = self.arg[j][i] + other_matrix
                    summed_matrix[j].append(the_sum)

        # elif type(self.arg) != 'Class':
        #     print('hell yeah')
        #     for j in range(len(other_matrix.arg[0])):
        #         for i in range(len(other_matrix.arg[1])):
        #             self.arg[j][i] = self.arg
        #             the_sum = self.arg[j][i] + other_matrix
        #             summed_matrix[j].append(the_sum)
            # for j in range(len(self.arg)):
            #     for i in range(len(self.arg[j])):
            #         # print(type(self.arg), type(other_matrix))  # other_matrix.jacie
            #         the_sum = self + other_matrix.arg[j][i]
            #         summed_matrix[j].append(the_sum)
        else:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    #print(type(self.arg), type(other_matrix))  # other_matrix.jacie
                    the_sum = self.arg[j][i] + other_matrix.arg[j][i]
                    summed_matrix[j].append(the_sum)
        return summed_matrix

    def __radd__(self, other_arg):
        summed_matrix = [[], [], []]
        for j in range(len(self.arg)):
            for i in range(len(self.arg[j])):
                # print(type(self.arg), type(other_matrix))  # other_matrix.jacie
                the_sum = other_arg + self.arg[j][i]
                summed_matrix[j].append(the_sum)

        return summed_matrix



    #p3 = p1 + p2 + po
    #p3 = p1.__add__(p2).__add__(po)
    #p5 = 4 + p1
    #p5= 4.__add__(p1)

    # def sum_matrix(self, arg2):
    #     summed_matrix = [[],[],[]]
    #
    #     for j in range(len(self.arg)):
    #         for i in range(len(self.arg[j])):
    #             the_sum = self.add(self.arg[j][i], arg2[j][i])
    #             #the_sum = self.arg[j][i] + arg2[j][i]
    #             summed_matrix[j].append(the_sum)
    #     return summed_matrix
    #
    # def subtract_matrix(self, arg2, lambda):
    #     return do_sth(lambda ())


    def substract_matrix(self, arg1, arg2):
        subtracted_matrix= arg
        for j in range(len(arg1.arg)):
            for i in range(len(arg1.arg[j])):
                the_substract = self.arg[j][i] - arg2[j][i]
                subtracted_matrix[j].append(the_substract)
        return subtracted_matrix


    def dot_scalar_matrix(self, row1, row2,):

        print(row1, row2)
        row1v2= row1[0]*row2[0]
        row2v2 = row1[1] * row2[1]
        scalar = row1v2 + row2v2

        #print("dot scalar: ",scalar)
        return scalar


if __name__ == '__main__':
    mat_2x2 = Matrix([[1,2], [3,4]])
    mat_3x3 = Matrix([[1, 2,5],
                      [3, 4,5],
                      [7,9,8]])
    mat_3x3v2 = Matrix([[1, 2,5], [3, 4,5], [7,9,8]])
    mat_3x3v3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    matrix3x3v4 = Matrix([[3,3,3], [4,4,4], [1,1,1]])

    #the_sum = mat_3x3v3.sum_matrix(mat_3x3, mat_3x3)

    #matrix3 = (mat_3x3v3.__add__(mat_3x3v2)).__add__(nanan)
    #matrix3 = Matrix.__add__(mat_3x3v3,mat_3x3v2)
    #matrix3 = mat_3x3v3 + mat_3x3v3
    matrix3 = mat_3x3v3 + 5
    matrix4 = mat_3x3v2 + matrix3x3v4
    matrix5 = 1 + mat_3x3v3
    #matrix5 = 5.__add__(mat_3x3v3)

    print(matrix3, '\n', matrix4, '\n', matrix5)
    #print(int.__add__(3,4))


#/home/ms/PycharmProjects/level_2_zadan/task1-Martyna73/task.py