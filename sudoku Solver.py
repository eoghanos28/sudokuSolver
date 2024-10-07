def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    locations={}
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x]==0:
                locations[y,x]=[]
                for y1 in range(len(puzzle)):
                    if puzzle[y1][x]!=0:
                        if puzzle[y1][x] not in locations[y,x]:
                            locations[y,x].append(puzzle[y1][x])
                for x1 in range(len(puzzle)):
                    if x1 != x:
                        if puzzle[y][x1]!=0:
                            if puzzle[y][x1] not in locations[y,x]:
                                locations[y,x].append(puzzle[y][x1])
                for curBoxX in range(x-(x%3),(x-(x%3))+3):
                    for curBoxY in range(y-(y%3),(y-(y%3))+3):
                        if x==curBoxX and y==curBoxY:
                            continue
                        if puzzle[curBoxY][curBoxX] != 0 and puzzle[curBoxY][curBoxX] not in locations[y,x]:
                            locations[y,x].append(puzzle[curBoxY][curBoxX]) 
    high=[[],[]]
    locations = dict(sorted(locations.items(), key=lambda item: len(item[1]), reverse=True))
    loc=list(locations.items())
    #locations now contains a sorted dict with each position and what is in each other position
    while locations != {}:

        for i in range(1,10):
            if i not in loc[0][1]:
                locations.pop((loc[0][0][0],loc[0][0][1]))
                puzzle[loc[0][0][0]][loc[0][0][1]]=i
                for y in range(len(puzzle)):
                    if puzzle[y][loc[0][0][1]] == 0:
                        if y != loc[0][0][0] and i not in locations[(y,loc[0][0][1])]:
                            locations[y,loc[0][0][1]].append(i) 
                for x in range(len(puzzle[loc[0][0][1]])):
                    if puzzle[loc[0][0][0]][x] == 0:
                        if x != loc[0][0][1] and i not in locations[loc[0][0][0],x]:
                            locations[loc[0][0][0],x].append(i)
                #work on square around added now
                for curBoxX in range(loc[0][0][1]-(loc[0][0][1]%3),(loc[0][0][1]-(loc[0][0][1]%3))+3):
                    for curBoxY in range(loc[0][0][0]-(loc[0][0][0]%3),(loc[0][0][0]-(loc[0][0][0]%3))+3):
                        if (loc[0][0][1]==curBoxX and loc[0][0][0]==curBoxY) or puzzle[curBoxY][curBoxX] != 0:
                            continue
                        if puzzle[curBoxY][curBoxX] == 0 and i not in locations[curBoxY,curBoxX]:
                            locations[curBoxY,curBoxX].append(i)
                locations = dict(sorted(locations.items(), key=lambda item: len(item[1]), reverse=True))
                loc=list(locations.items()) 
                break
    return puzzle      


            





puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

answersudoku=sudoku(puzzle)

for i in range(len(answersudoku)):
    print(answersudoku[i])



