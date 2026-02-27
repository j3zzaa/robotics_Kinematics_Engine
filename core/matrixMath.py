import math
def dotProduct(vectorA, vectorB):
    '''
    Calculates the dot product of two 1d vectors.
    '''
    if len(vectorA) != len(vectorB): 
        raise ValueError("Mathematical Error, Vectors must be identical length")
    
    result = 0.0
    for i in range(len(vectorA)):
        result += vectorA[i] * vectorB[i]

    return result

def multiplyMatrices(matrixA, matrixB):

    columnsA = len(matrixA[0])
    rowsB = len(matrixB)

    if columnsA != rowsB:
        raise ValueError("Inner Dimensions Must Match: "
                         f"columnsA {columnsA} != rowsB {rowsB}")

    rowsA = len(matrixA)
    columnsB = len(matrixB[0])

    matrixC = [[0.0 for _ in range(columnsB)] for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(columnsB):

            rowVector = matrixA[i]

            columnVector = []
            for k in range(rowsB):
                columnVector.append(matrixB[k][j])

            matrixC[i][j] = dotProduct(rowVector, columnVector)

    return matrixC

def rotateX(theta):
    R_x = [
        [1, 0, 0],
        [0, math.cos(theta), math.sin(-theta)],
        [0, math.sin(theta), math.cos(theta)]

]

    return R_x

def rotateY(theta):
    R_y = [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [math.sin(-theta), 0, math.cos(theta)]
    ]

    return R_y

def rotateZ(theta):
    R_z = [
        [math.cos(theta), math.sin(-theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1],
    ]

    return R_z

def cleanMatrix(matrix, tolerance=1e-15):

    cleanedMatrix = []

    for row in matrix:
        newRow = []
        for value in row:
            if abs(value) < tolerance:
                newRow.append(0.0)

            else:
                newRow.append(round(value, 10))

        cleanedMatrix.append(newRow)

    return cleanedMatrix


