import math
from core import rotateZ, multiplyMatrices, cleanMatrix

def testRotation():

    startPosition = [[1.0], [0.0], [0.0],]

    angle = math.pi/2
    matrix = rotateZ(angle)

    newPosition = multiplyMatrices(matrix, startPosition)

    print(f"Original position: {startPosition}")
    print(f"New position: {cleanMatrix(newPosition)}")

if __name__ == "__main__":
    testRotation()