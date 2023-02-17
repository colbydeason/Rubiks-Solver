from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Solve flower
    #     a) check each side and move white edge pieces to the top to form the flower
    # Step 2: Solve cross
    #     b) match up edge to face center and rotate side 
    
    edgeList = [1, 3, 5, 7, 46]
    bottomColor = theCube.get()[49]
    for i in range(4):
        topEdge = theCube.getRelativeSquare(43)
        if topEdge == bottomColor:
            theCube.rotate('U')
            continue
        else:
            for j in range (4):
                if theCube.getRelativeSquare(edgeList[0]) == bottomColor:
                    theCube.rotate('FuRUU')
                    break
                if theCube.getRelativeSquare(edgeList[1]) == bottomColor:
                    theCube.rotate('Ul')
                    break
                if theCube.getRelativeSquare(edgeList[2]) == bottomColor:
                    theCube.rotate('uRUU')
                    break
                if theCube.getRelativeSquare(edgeList[3]) == bottomColor:
                    theCube.rotate('FUr')
                    break
                if theCube.getRelativeSquare(edgeList[4]) == bottomColor:
                    theCube.rotate('FFU')
                    break
                theCube.rotate('u')
                theCube.rotateCubeR()
    
    
    
    return theCube.popCurrentRotationString()