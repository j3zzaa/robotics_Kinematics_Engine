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