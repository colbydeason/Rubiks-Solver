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
    edgeList = [1, 3, 5, 7, 46]
    bottomColor = flowerCube.get()[49]
    for i in range(5):
        topEdge = flowerCube.getRelativeSquare(43)
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
            if ftbCube.getRelativeSquare(1) == ftbCube.getRelativeSquare(4):
                ftbCube.rotate('FF')
                ftbCube.rotateCubeR()
                break
            else:
                ftbCube.rotate('u')
                ftbCube.rotateCubeR()
    ftbCube.resetCubeOrientation()              
                
    