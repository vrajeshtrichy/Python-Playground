boxes = [0, 1, 2, 3, 4, 5, 6, 7]

for e in boxes:
    otherBoxes = boxes
    otherBoxes.remove(e)
    # print(otherBoxes)
    for o in otherBoxes:
        print(e, o)
# BigO is (b x o) --> Quadratic Time