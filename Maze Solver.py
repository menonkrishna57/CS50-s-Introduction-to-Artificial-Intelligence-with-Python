dimen=list(map(int,input().split()))#0-Number of lines 1-Width of the maze
maze=[]
def mazeinputer():#Inputs the maze into a list
    for i in range(dimen[0]):
        mazeline=input().strip()
        maze.append(mazeline)

def checker():#Checks if the maze is a valid maze with a start and end
    qccheck=True
    if '*' not in maze[0]:
        qccheck=False
    elif '*' not in maze[-1]:
        qccheck=False

def startend():#Decides the start and end point
    global startpoint,endpoint
    startpoint=None
    endpoint=None
    success=0
    for i in range(dimen[1]):
        if maze[0][i]=='*' and startpoint is None:
            startpoint=i
        if maze[-1][i]=="*" and endpoint is None:
            endpoint=i
    else:
        if startpoint is None:
            print("Failed to Detect Start Point")
        else:
            success+=1
        if endpoint is None:
            print("Failed to Detect End Point")
        else:
            success+=1
    return success

def optionmaker(lno,pos):#Line Number and Position
    options=[]
    
