def solution(xs):
    # if only 1 panel, then that is the max:
    if len(xs) == 1:
        return str(xs[0])

    # otherwise, separate negatives from positives:
    positives = []
    negatives = []
    for panel in xs:
        if panel > 0:
            positives.append(panel)
        elif panel < 0:
            negatives.append(panel)

    countPositive = len(positives)
    countNegative = len(negatives)

    # if no positives exist, then max is 0
    if countPositive == 0:
        return str(0)

    totalMaxOutput = 1
    # multiply all positives:
    for panel in positives:
        totalMaxOutput *= panel
    # multiply all negatives:
    for panel in negatives:
        totalMaxOutput *= panel
    # if countNegative is odd, then current total is negative, so divide by negative closest to zero
    if countNegative % 2 == 1:
        totalMaxOutput /= (max(negatives))

    return str(totalMaxOutput)