import turtle
from Point import Point
from Board import create_board
from DFS import tour

if __name__ == "__main__":
    wn = turtle.Screen()
    board = turtle.Turtle()
    create_board(board)



    knight = turtle.Turtle()
    knight.shape("turtle")
    knight.penup()
    knight.speed(1)
    #knight.goto(-224,224)
    #knight.stamp()
    knight.goto(-224,224)
    knight.pendown()
    #p = Point(75,75)
    #p2 = Point(150, 200)
    #print(p.x, p.y)
    #knight.penup()
    #knight.goto(p.x,p.y)
    #knight.stamp()
    #knight.goto(p2.x,p2.y)
    #knight.stamp()


    matrix = [[0 for i in xrange(8)] for i in xrange(8)]
    cx = -224
    cy = 224
    for i in range(0,8):
        for j in range(0,8):
            cp = Point(cx, cy)
            matrix[i][j] = cp
            cx = cx + 64
        cx = -224
        cy = cy - 64

#    for i in range(8):
#        for j in range (8):
#            p = matrix[i][j]
#            print(p)
#            #knight.penup()
#            knight.goto(p.x,p.y)
#            knight.stamp()

    count = 0
    lst = []
    #matrix[0][0].toggleVisited()
    first = True
    count = tour(matrix, 0,0,count, knight, first)
    #print(lst)

    print(count)




    wn.exitonclick()
