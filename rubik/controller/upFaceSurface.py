from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpSurface(theCube: Cube) -> str:
    while _alignCorner(theCube):
        theCube.rotate("RUrURUUr")
    return theCube.popCurrentRotationStringResetOrientation()

def _alignCorner(cornerCube):
    cornerArray = [UTL, UTR, UBL, UBR]
    cornerColorArray = []
    topColor = cornerCube.getRelativeSquare(UMM)
    for corner in cornerArray:
        cornerColorArray.append(cornerCube.getRelativeSquare(corner))
    numberMatching = cornerColorArray.count(topColor)
    
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