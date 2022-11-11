def translateNumberToCoordinates(position):
    row = position // 8;
    column = position % 8;

    coordinates = [];
    coordinates.append(row);
    coordinates.append(column);

    return coordinates;


def checkBoundaries(startingCoord, direction):
    # ensure the move is possible (within bounds) - so row and column > 0 but < 8
    return 0 <= (startingCoord + direction) < 8


def getListOfCoordsOfNextMoves(startingCoords):
    startingCoordsRow = startingCoords[0];
    startingCoordsColumn = startingCoords[1];

    nextMovesCoords = [];

    # 2 down, 1 right
    if (checkBoundaries(startingCoordsRow, 2)) and (checkBoundaries(startingCoordsColumn, 1)):
        nextMoveCoord = [startingCoordsRow + 2, startingCoordsColumn + 1];
        nextMovesCoords.append(nextMoveCoord);
    # 2 down, 1 left
    if (checkBoundaries(startingCoordsRow, 2)) and (checkBoundaries(startingCoordsColumn, -1)):
        nextMoveCoord = [startingCoordsRow + 2, startingCoordsColumn - 1];
        nextMovesCoords.append(nextMoveCoord);
    # 1 down, 2 right
    if (checkBoundaries(startingCoordsRow, 1)) and (checkBoundaries(startingCoordsColumn, 2)):
        nextMoveCoord = [startingCoordsRow + 1, startingCoordsColumn + 2];
        nextMovesCoords.append(nextMoveCoord);
    # 1 down, 2 left
    if (checkBoundaries(startingCoordsRow, 1)) and (checkBoundaries(startingCoordsColumn, -2)):
        nextMoveCoord = [startingCoordsRow + 1, startingCoordsColumn - 2];
        nextMovesCoords.append(nextMoveCoord);

    # 2 up, 1 right
    if (checkBoundaries(startingCoordsRow, -2)) and (checkBoundaries(startingCoordsColumn, 1)):
        nextMoveCoord = [startingCoordsRow - 2, startingCoordsColumn + 1];
        nextMovesCoords.append(nextMoveCoord);
    # 2 up, 1 left
    if (checkBoundaries(startingCoordsRow, -2)) and (checkBoundaries(startingCoordsColumn, -1)):
        nextMoveCoord = [startingCoordsRow - 2, startingCoordsColumn - 1];
        nextMovesCoords.append(nextMoveCoord);
    # 1 up, 2 right
    if (checkBoundaries(startingCoordsRow, -1)) and (checkBoundaries(startingCoordsColumn, 2)):
        nextMoveCoord = [startingCoordsRow - 1, startingCoordsColumn + 2];
        nextMovesCoords.append(nextMoveCoord);
    # 1 up, 2 left
    if (checkBoundaries(startingCoordsRow, -1)) and (checkBoundaries(startingCoordsColumn, -2)):
        nextMoveCoord = [startingCoordsRow - 1, startingCoordsColumn - 2];
        nextMovesCoords.append(nextMoveCoord);

    return nextMovesCoords


def solution(src, dest):
    if (src == dest):
        return 0;
    else:
        # 1. translate number to coordinates:
        startingCoords = translateNumberToCoordinates(src);
        destinationCoords = translateNumberToCoordinates(dest);

        # 2. start at startingCoords:
        nextMoves = [startingCoords];
        numOfMoves = 0;
        while (destinationCoords not in nextMoves):
            numOfMoves += 1;
            # 3. create list of coordinates of next moves (based on coordinates from previous move possibilities)
            newNextMoves = []
            for index in range(len(nextMoves)):
                newNextMoves.extend(getListOfCoordsOfNextMoves(nextMoves[index]));
            nextMoves = newNextMoves;

        return (numOfMoves);


print(f'({solution(0, 1)} moves for 0,1');  # 3 moves
print(f'({solution(0, 2)} moves for 0,2');  # 2 moves
print(f'({solution(0, 17)} moves for 0,17');  # 1 move
print(f'({solution(19, 36)} moves for 19,36');  # 1 move
print(f'({solution(0, 63)} moves for 0,63');  # 6 moves
print(f'({solution(0, 62)} moves for 0,62');  # 5 moves