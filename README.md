# SoftwareProcessRubik
Spring 2023 Rubik Project Repository

This application runs on a local host, and uses the url arguments as inputs. Through this, you can run:
1. localhost:8080/rubik/rotate
2. localhost:8080/rubik/solve
Where rubik/rotate rotates a cube given a specific cube and set of rotations, and rubik/solve takes a cube and outputs the solution string given that the cube is solvable (is a real rubiks cube).

## Rubik Rotate
Rubike rotate takes in a cube string and a rotation string, or just a cube string. If the rotation argument is left out of the url, then it rotates the front face.

The rotation string allows for the following rotational inputs:
    **F, f, R, r, L, l, B, b, U, u**
The capital letters refer to clockwise rotation, and the lowercase counterclockwise. 
The supported side rotations are then front face, right face, left face, back face, and up face (NOT bottom face); represented by F and f, R and r, L and l, B and b, U and u

The cube string is a flatened representation of a cube, which you can view in the picture provided labeled cube.png.
The numbers in this picture represent its indexical equivalent in the cube string.
aA-zZ and 0-9 are allowed in the representation of a cube, but only in the ranges that the cubestring can still represent an actual cube (6 different characters, unique centers, 9 of each color, cube is solvable)



