import rubik.model.constants
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    
    # Solving Breakdown
    #
    # Step 1: Solve flower
    #     a) check each side and move white edge pieces to the top to form the flower
    # Step 2: Solve cross
    #     b) match up edge to face center and rotate side 
    
    
    bottomFaceColor = theCube.get()[4]
    
    
    
    
    
    return theCube.getCurrentRotationString()
