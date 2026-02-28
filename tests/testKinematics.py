import math
from core import rotateZ, multiplyMatrices, cleanMatrix, translationMatrix, transformZ

def testRotation():

    startPosition = [[1.0], [0.0], [0.0], [1.0]]

    angle = math.pi/2
    matrix = rotateZ(angle)
    movement = translationMatrix(10.0, 0.0, 0.0)

    rawPosition = multiplyMatrices(movement, startPosition)
    newPosition = multiplyMatrices(matrix, startPosition)

    print(f"Original position: {startPosition}")
    print(f"New position: {cleanMatrix(rawPosition)}")

def testCompoundJoint():
    startPosition = [[5.0], [0.0], [0.0], [0.0]]

    angle = math.pi/2
    lift = 10

    jointMatrix = transformZ(angle, lift)

    rawPosition = multiplyMatrices(jointMatrix, startPosition)
    finalPosition = cleanMatrix(rawPosition)

    print(f"Final Position: {finalPosition}")

if __name__ == "__main__":
    testCompoundJoint()