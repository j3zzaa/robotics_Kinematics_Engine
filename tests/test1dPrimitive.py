from core import dotProduct

def runTest():

    vectorA = [1.0, 2.0, 3.0]
    vectorB = [4.0, 5.0, 6.0]

    print("Executing 1D Dot Product Test: ")
    result = dotProduct(vectorA, vectorB)

    print(f"Vector A: {vectorA}")
    print(f"Vector B: {vectorB}")
    print(f"Result: {result}")
    print(f"Expected: 32.0")

if __name__ == "__main__":
    runTest()