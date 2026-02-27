from core import multiplyMatrices

def runTest():
    # 1. Conformable Matrix Test (3x2 multiplied by 2x3)
    matrixA = [
        [1.0, 2.0],
        [3.0, 4.0],
        [5.0, 6.0]
    ]
    
    matrixB = [
        [7.0, 8.0, 9.0],
        [10.0, 11.0, 12.0]
    ]
    
    print("Executing M x N Matrix Multiplication Test...")
    result = multiplyMatrices(matrixA, matrixB)
    
    print("Result Matrix (3x3):")
    for row in result:
        print(row)
        
    # 2. Dimensionality Gateway Test (3x2 multiplied by 1x2)
    print("\nExecuting Dimensionality Gateway Test...")
    invalidMatrixC = [
        [1.0, 2.0]
    ]
    
    try:
        multiplyMatrices(matrixA, invalidMatrixC)
        print("FAILURE: Gateway did not block the operation.")
    except ValueError as e:
        print(f"SUCCESS: Gateway intercepted error -> {e}")

if __name__ == "__main__":
    runTest()