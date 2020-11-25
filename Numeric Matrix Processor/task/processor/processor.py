
def addition(a, b):
    p_add = len(a) == len(b)
    if p_add:
        for i in range(len(a)):
            if len(a[i]) != len(b[i]):
                p_add = False
                break
    if not p_add:
        return []
    else:
        result = [[0 for i in a[0]] for j in a]
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = a[i][j] + b[i][j]
        return result


def print_m(matrix):
    print("The result is:")
    is_float = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not matrix[i][j].is_integer():
                is_float = True
                break
    if not is_float:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0.0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = round(matrix[i][j], 2)
    for i in range(len(matrix)):
        print()
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
    print()


def multiply_n(a, n):
    result = [[] for i in range(len(a))]
    for i in range(len(a)):
        result[i] = [x * n for x in a[i]]
    return result


def create_matrix(matrix_number=""):
    m, n = (int(x) for x in input(f"Enter the size of {matrix_number} matrix: ").split())
    print(f"Enter the {matrix_number} matrix:")
    a_m = [[] for j in range(m)]
    for i in range(m):
        a_m[i] = [float(x) for x in input().split(None, n)]
    return a_m


def mult_matrix(a, b):
    p_add = True
    for i in range(1, len(a)):
        if len(a[i]) != len(a[0]):
            p_add = False
            break
    if p_add:
        for i in range(1, len(b)):
            if len(b[i]) != len(b[0]):
                p_add = False
                break
    if p_add:
        p_add = len(a[0]) == len(b)
    if p_add:
        result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result
    else:
        return []


def menu():
    while True:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
        n = int(input("Your choice: "))
        res = []
        if n == 1:
            m1 = create_matrix("first")
            m2 = create_matrix("second")
            res = addition(m1, m2)
        elif n == 2:
            m1 = create_matrix()
            const = float(input("Enter constant: "))
            res = multiply_n(m1, const)
        elif n == 3:
            m1 = create_matrix("first")
            m2 = create_matrix("second")
            res = mult_matrix(m1, m2)
        elif n == 4:
            res = transpose()
        elif n == 5:
            m = create_matrix()
            res = find_determinant(m)
        elif n == 6:
            m = create_matrix()
            res = inverse_matrix(m)
        elif n == 0:
            break
        if res:
            if type(res) is list:
                print_m(res)
            else:
                print("The result is:", res, sep="\n")
        else:
            print("The operation cannot be performed.")


def transpose():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    n = int(input("Your choice: "))
    m = create_matrix()
    for i in range(1, len(m)):
        if len(m[i]) != len(m[0]):
            return []
    result = [[0 for j in range(len(m))] for i in range(len(m[0]))]
    rows = len(result)
    cols = len(result[0])
    if n == 1:
        for i in range(rows):
            for j in range(cols):
                result[i][j] = m[j][i]
    elif n == 2:
        for i in range(rows):
            for j in range(cols):
                result[rows - 1 - i][cols - 1 - j] = m[j][i]
    elif n == 3:
        for i in range(rows):
            for j in range(cols):
                result[i][j] = m[i][cols - 1 - j]
    elif n == 4:
        for i in range(rows):
            for j in range(cols):
                result[i][j] = m[rows - 1 - i][j]

    return result


def find_determinant(matrix, total=0):
    indices = list(range(len(matrix)))
    if len(matrix) == 1 and len(matrix[0]) == 1:
        total = matrix[0][0]
    else:
        if len(matrix) == 2 and len(matrix[0]) == 2:
            val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return val
        for fc in indices:
            s_matrix = copy_matrix(matrix)

            s_matrix = s_matrix[1:]
            height = len(s_matrix)

            for i in range(height):
                s_matrix[i] = s_matrix[i][0:fc] + s_matrix[i][fc+1:]

            sign = (-1) ** (fc % 2)
            sub_det = find_determinant(s_matrix)
            total += sign * matrix[0][fc] * sub_det
    if type(total) is int:
        pass
    elif total.is_integer():
        total = int(total)
    return total


def copy_matrix(matrix):
    s_matrix = [[0 for j in matrix[0]] for i in matrix]
    for i in range(len(s_matrix)):
        for j in range(len(s_matrix[i])):
            s_matrix[i][j] = matrix[i][j]
    return s_matrix


def identity_matrix(n):
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        res[i][i] = 1
    return res


def inverse_matrix(matrix):
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return []
    if len(matrix) != len(matrix[0]):
        return []
    det = find_determinant(matrix)
    if not det:
        return []
    s_matrix = copy_matrix(matrix)
    i_matrix = identity_matrix(len(s_matrix))
    n = len(matrix)
    indices = list(range(n))
    for fd in range(n):
        fd_scaler = 1.0 / s_matrix[fd][fd]
        for j in range(n):
            s_matrix[fd][j] *= fd_scaler
            i_matrix[fd][j] *= fd_scaler
        for i in indices[0:fd] + indices[fd+1:]:
            cr_scaler = s_matrix[i][fd]
            for j in range(n):
                s_matrix[i][j] = s_matrix[i][j] - cr_scaler * s_matrix[fd][j]
                i_matrix[i][j] = i_matrix[i][j] - cr_scaler * i_matrix[fd][j]
    return i_matrix


menu()
# a = create_matrix()
# print_m(inverse_matrix(a))
