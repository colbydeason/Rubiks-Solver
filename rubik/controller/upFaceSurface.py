from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    cornerArray = [UTL, UTR, UBL, UBR]
    cornerColorArray = []
    topColor = theCube.getRelativeSquare(UMM)
    for corner in cornerArray:
        cornerColorArray.append(theCube.getRelativeSquare(corner))
    numberMatching = cornerColorArray.count(topColor)
    while _alignCorner(theCube, numberMatching):
        theCube.rotate("RUrURUUr")
    return theCube.popCurrentRotationStringResetOrientation()

def _alignCorner(cornerCube, numberMatching):
    topColor = cornerCube.getRelativeSquare(UMM)
    if numberMatching == 0 or numberMatching == 2:
        while topColor != cornerCube.getRelativeSquare(LTR):
            cornerCube.rotateCubeR()
        return True
    elif numberMatching == 1:
        while topColor != cornerCube.getRelativeSquare(UBL):
            cornerCube.rotateCubeR()
        return True
    else:
        return False