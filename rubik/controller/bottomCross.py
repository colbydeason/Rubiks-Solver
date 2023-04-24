from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Solve flower
    #     a) check each side and move white edge pieces to the top to form the flower
    # Step 2: Solve cross
    #     b) match up edge to face center and rotate side 
    
    if theCube.bottomCrossDone():
        return ''
    _solveFlower(theCube)
    _flowerToBottom(theCube)
    
    if not theCube.bottomCrossDone():
        return 'error: unsolvable cube'
    return theCube.popCurrentRotationStringResetOrientation()

def _solveFlower(flowerCube):
    edgeList = [FTM, FML, FMR, FBM, DTM]
    bottomColor = flowerCube.get()[DMM]
    for i in range(5):
        topEdge = flowerCube.getRelativeSquare(UBM)
        if topEdge == bottomColor:
            flowerCube.rotateCubeR()
            continue
        else:
            for j in range (4):
                if flowerCube.getRelativeSquare(edgeList[0]) == bottomColor:
                    flowerCube.rotate('FuR')
                    flowerCube.rotateCubeR()
                    flowerCube.rotateCubeR()
                    break
                if flowerCube.getRelativeSquare(edgeList[1]) == bottomColor:
                    flowerCube.rotate('Ul')
                    break
                if flowerCube.getRelativeSquare(edgeList[2]) == bottomColor:
                    flowerCube.rotate('uR')
                    flowerCube.rotateCubeR()
                    flowerCube.rotateCubeR()
                    break
                if flowerCube.getRelativeSquare(edgeList[3]) == bottomColor:
                    flowerCube.rotate('FUl')
                    break
                if flowerCube.getRelativeSquare(edgeList[4]) == bottomColor:
                    flowerCube.rotate('FF')
                    flowerCube.rotateCubeR()
                    break
                flowerCube.rotate('u')
                flowerCube.rotateCubeR()
    
    flowerCube.resetCubeOrientation()
    
def _flowerToBottom(ftbCube):
    for i in range(4):
        for j in range(4):
            if ftbCube.getRelativeSquare(FTM) == ftbCube.getRelativeSquare(FMM):
                ftbCube.rotate('FF')
                ftbCube.rotateCubeR()
                break
            else:
                ftbCube.rotate('u')
                ftbCube.rotateCubeR()
    ftbCube.resetCubeOrientation()              
                
    