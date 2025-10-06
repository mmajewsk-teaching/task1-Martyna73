import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Matrix():
    def __init__(self, arg):
        self.arg = arg
        self.jacie = 'gacie'

    def __add__(self, other_matrix):
        logger.info('Doing adding')
        summed_matrix = []
        for i in range(len(self.arg)):
            summed_matrix.append([])

        if type(other_matrix) == int or type(other_matrix) == float:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    the_sum = self.arg[j][i] + other_matrix
                    summed_matrix[j].append(the_sum)
        else:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    the_sum = self.arg[j][i] + other_matrix.arg[j][i]
                    summed_matrix[j].append(the_sum)
        summed_matrix = Matrix(summed_matrix)
        return summed_matrix

    def __radd__(self, other_arg):
        logger.info('Doing reversed adding')
        summed_matrix = []
        for i in range(len(self.arg)):
            summed_matrix.append([])

        if type(other_arg) == int or type(other_arg) == float:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    the_sum = other_arg + self.arg[j][i]
                    #print(type(other_arg), type(self.arg[j][i]))
                    summed_matrix[j].append(the_sum)
            summed_matrix = Matrix(summed_matrix)
            return summed_matrix
        else:
            raise "Error"


    def __sub__(self, other_matrix):
        logger.info('Doing subtraction')
        subtracted_matrix = []
        for i in range(len(self.arg)):
            subtracted_matrix.append([])

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
        subtracted_matrix = Matrix(subtracted_matrix)
        return subtracted_matrix

    def __rsub__(self, other_matrix):
        logger.info('Doing reverse subtraction')
        subtracted_matrix = []
        for i in range(len(self.arg)):
            subtracted_matrix.append([])

        if type(other_matrix) == int or type(other_matrix) == float:
            for j in range(len(self.arg)):
                for i in range(len(self.arg[j])):
                    the_subtract = other_matrix - self.arg[j][i]
                    subtracted_matrix[j].append(the_subtract)
        subtracted_matrix = Matrix(subtracted_matrix)
        return subtracted_matrix

    def __mul__(self, other_matrix):
        logger.info('Doing multiplying')

        if type(other_matrix) == int or type(other_matrix) == float:
            multipled_mat = []
            for i in range(len(self.arg)):
                multipled_mat.append([])

            for i in range(len(self.arg)):
                for j in range(len(self.arg[i])):
                    the_multipled= self.arg[i][j] * other_matrix
                    multipled_mat[i].append(the_multipled)
            multipled_mat = Matrix(multipled_mat)
            return multipled_mat

        else:
            multipled_mat = []
            for i in range(len(self.arg)):
                multipled_mat.append([])
            for i in range(len(self.arg)):
                row1 = []
                for j in range(len(self.arg[i])):
                    val1 = self.arg[i][0] * other_matrix.arg[0][j] + self.arg[i][1] * other_matrix.arg[1][j] + \
                           self.arg[i][2] * other_matrix.arg[2][j]
                    #print("val: ",val1)
                    row1.append(val1)
                multipled_mat[i] = row1
            multipled_mat = Matrix(multipled_mat)
            return multipled_mat

    def __matmul__(self, other_matrix):
        logger.info('Doing multiplying')

        if type(other_matrix) == int or type(other_matrix) == float:
            multipled_mat = []
            for i in range(len(self.arg)):
                multipled_mat.append([])
            for i in range(len(self.arg)):
                for j in range(len(self.arg[i])):
                    the_multipled= self.arg[i][j] * other_matrix
                    multipled_mat[i].append(the_multipled)
            multipled_mat = Matrix(multipled_mat)
            return multipled_mat

        else:
            multipled_mat = []
            for i in range(len(self.arg)):
                multipled_mat.append([])
            for i in range(len(self.arg)):
                row1 = []
                for j in range(len(self.arg[i])):
                    val1 = val1 = self.arg[i][0] * other_matrix.arg[0][j] + self.arg[i][1] * other_matrix.arg[1][j] + \
                           self.arg[i][2] * other_matrix.arg[2][j]
                    row1.append(val1)
                multipled_mat[i]=row1
            multipled_mat = Matrix(multipled_mat)
            return multipled_mat

    def __str__(self):
        string_with_list = ''
        for i in range(len(self.arg)):
            string_with_list += '|'
            for j in range(len(self.arg[i])):
                if j != len(self.arg[i])-1:
                    d = str(self.arg[i][j])+', '
                else:
                    d = str(self.arg[i][j])
                string_with_list = string_with_list + d
            string_with_list += '|' + '\n'
        return string_with_list




if __name__ == '__main__':
    mat_3x3 = Matrix([[1, 2,5],
                       [7, 9,9],
                       [7,9,9]])
    mat_3x3v3 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    mat6= Matrix([[2,2,2],[4,4,4],[6,6,6]])
    m1 = Matrix([[1, 2,5],[3, 4,5],[7,9,8]])
    m2 = Matrix([[3,3,3], [1,1,1], [1,1,1]])
    m3 = Matrix([[3,3,3], [4,4,4], [1,1,1]])

    m2 += m1
    print(m2)
    m3 = m2 + m1
    print(m3)
    m3 -= m2
    print(m3)
    m3 = m2 - m1
    print(m3)
    m3 = m2 @ m1

    m2 += 4.5
    print(m2)

    print(m3)
    m3 -= 4.5
    print(m3)
    m3 = - 4.5
    print(m3)
    m3 = m2 - 4.5
    print("po zmianie: ",m3)
    m3 = m2 @ 4.5

    m3 = m1 * 4.5
    m3 = m2 * m1
    print(m3)
