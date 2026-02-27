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





