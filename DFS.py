from Point import Point
import turtle



def inboundcheck(x, y):
    if(x < 0 or y < 0 or x > 7 or y > 7):
        return True
    return False


def tour(matrix, x,y, count,lst, first):
    if(x < 0 or y < 0 or x > 7 or y > 7):
        return count
    cp = matrix[x][y]
    if(cp.hasBeenVisited()):
        if(first):
            first = not first
        else:
            return count
    if(count == 63):
        return count

    count = count + 1
    print(count)
    cp.toggleVisited()
    count = tour(matrix,x+2,y+1,count,lst, first)
    count = tour(matrix,x+2,y-1,count,lst, first)
    count = tour(matrix,x+1,y+2,count,lst, first)
    count = tour(matrix,x+1,y-2,count,lst, first)
    count = tour(matrix,x-1,y+2,count,lst, first)
    count = tour(matrix,x-1,y-2,count,lst, first)
    count = tour(matrix,x-2,y+1,count,lst, first)
    count = tour(matrix,x-2,y-1,count,lst, first)

    if(count == 63):
        lst.goto(cp.x, cp.y)
        lst.stamp()
        return count
    else:
        count = count - 1
        cp.toggleVisited()
        return count
