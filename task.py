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
#from mnozenie_maciezy import multiplying_matrix

class Matrix():
    def __init__(self, arg):
        self.arg = arg
        self.jacie = 'gacie'

    def __add__(self, other_matrix):
        summed_matrix = [[], [], []]
        if type(other_matrix) == int or type(other_matrix) == float:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    #print(type(self.arg), type(other_matrix))  # other_matrix.jacie
                    the_sum = self.arg[j][i] + other_matrix
                    summed_matrix[j].append(the_sum)
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

    def __sub__(self, other_matrix):
        subtracted_matrix= [[], [], []]

        if type(other_matrix) == int or type(other_matrix) == float:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    the_substract= self.arg[j][i] - other_matrix
                    subtracted_matrix[j].append(the_substract)
        else:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    the_substract = self.arg[j][i] - other_matrix.arg[j][i]
                    subtracted_matrix[j].append(the_substract)
        return subtracted_matrix

    def __rsub__(self, other_matrix):
        # do dokoncxzenia
        subtracted_matrix = [[], [], []]
        for j in range(len(self.arg)):
            for i in range(len(self.arg[j])):
                the_subtract = other_arg - self.arg[j][i]
                subtracted_matrix[j].append(the_subtract)

        return subtracted_matrix

###############no generalnie to trzeba zrobic takie puste listy pod operacje zeby nie psulo mi rozmiarow NxN bo na razie mam tylko 3x3
    def __mul__(self, other_matrix):
        if type(other_matrix) == int or type(other_matrix) == float:
            multipled_mat = [[],[],[]]
            for i in range(len(self.arg)):
                for j in range(len(self.arg[i])):
                    the_multipled= self.arg[i][j] * other_matrix
                    multipled_mat[i].append(the_multipled)

            return multipled_mat

        else:
            multipled_mat = []
            for i in range(len(self.arg)):
                # print(matrix1[i])
                row1 = []
                for j in range(len(self.arg[i])):
                    val1 = self.arg[i][0] * other_matrix.arg[0][j] + self.arg[i][1] * other_matrix.arg[1][j] + \
                           self.arg[i][2] * other_matrix.arg[2][j]
                    row1.append(val1)
                multipled_mat.append(row1)

            return multipled_mat


if __name__ == '__main__':
    mat_2x2 = Matrix([[1,2], [3,4]])
    mat_3x3 = Matrix([[1, 2,5],
                      [3, 4,5],
                      [7,9,8]])
    mat_3x3v2 = Matrix([[1, 2,5], [3, 4,5], [7,9,8]])
    mat_3x3v3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    matrix3x3v4 = Matrix([[3,3,3], [4,4,4], [1,1,1]])
    matrix4v4 = Matrix([[1,1,1,1],[2,2,2,2], [3,3,3,3],[4,4,4,4]])

    #the_sum = mat_3x3v3.sum_matrix(mat_3x3, mat_3x3)

    #matrix3 = (mat_3x3v3.__add__(mat_3x3v2)).__add__(nanan)
    #matrix3 = Matrix.__add__(mat_3x3v3,mat_3x3v2)
    #matrix3 = mat_3x3v3 + mat_3x3v3
    # matrix3 = mat_3x3v3 + 5
    # matrix4 = mat_3x3v2 + matrix3x3v4
    # matrix5 = 1 + mat_3x3v3
    #matrix5 = 5.__add__(mat_3x3v3)
    #print(matrix3, '\n', matrix4, '\n', matrix5)
    #print(int.__add__(3,4))
    #mat6 = 5 + mat_3x3v3
    mat7 = mat_3x3v3 * 4
    mat6= Matrix([[2,2,2],[4,4,4],[6,6,6]])
    #mat8 = matrix4v4  * 3
    #print(mat6.dot_product(matrix3x3v4))
    print("mnożenie: ",mat7)



#/home/ms/PycharmProjects/level_2_zadan/task1-Martyna73/task.py