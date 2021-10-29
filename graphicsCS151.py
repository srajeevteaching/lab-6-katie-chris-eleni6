#Chris, Katie, Eleni
#CS151
#Lab6
#11/4/21

from graphics import *

# This function accepts 3 parameters:
# title, a string
# width, the width of the window being created
# height, the height of the window being created
# The function returns a window "object" (a variable) representing a window
# whose title is title, whose width is width, and whose height is height
# When called, the window is created and shows
def make_window(title, width, height):
    win = GraphWin(title, width, height)
    return win

# This function creates a circle "object" and returns it
# A circle is defined by its center ( x, y ) and its radius, the 3 parameters of this function
# This function creates a circle but does not draw it
def make_circle(x, y, radius):
    return Circle(Point(x, y), radius)

# This function accepts 2 parameters:
# circle, a circle
# color, a color represented by a string such "red", "yellow", ...
# When called, it colors circle using color and draws it inside window
def color_circle(circle, color):
    circle.setFill(color)
    circle.setOutline(color)

# This function accepts 3 parameters:
# window, a window
# circle, a circle
# color, a color represented by a string such "red", "yellow", ...
# When called, it colors circle using color and draws it inside window
def draw_and_color_circle(window, circle, color):
    circle.setFill(color)
    circle.setOutline(color)
    circle.draw(window)

# This function accepts 3 parameters:
# circle, a circle "object"
# moveX, the number of pixels to move along the x axis
# moveY, the number of pixels to move along the y axis
# When called, it moves the position of circle by moveX and moveY pixels
#def move(circle, moveX, moveY):
#    circle.move(moveX, moveY)

# This function accepts 2 parameters:
# window, a window
# title, a string
# When called, it changes the title of window to title
def change_title(window, title):
    window.master.title(title)

# This function accepts 1 parameter:
# ms, a number of milliseconds
# When called, it stops the program for ms milliseconds
def sleep(ms):
    time.sleep(ms)

def whereis(circle):
    print("circle(", int(circle.getCenter().x), ",", int(circle.getCenter().y), ")")

def moveit(circle, dx, dy):
    sleep(10/1000)
    circle.move(dx, dy)

def main():

    startingX = 150
    startingY = 20
    circle = make_circle(startingX, startingY, 25)

    window = make_window("Bouncing Ball", 500, 500)
    window.setBackground("black")
    draw_and_color_circle(window, circle, "red")

    # down and right
    while (circle.getCenter().x + 1 < window.getHeight()):
        moveit(circle, 1, 1)

    color_circle(circle, "green")
    whereis(circle)

    # down and left
    while (circle.getCenter().y - 1 < window.getWidth()):
        moveit(circle, -1, 1)

    color_circle(circle, "blue")
    whereis(circle)

    # up and left
    while (circle.getCenter().x - 1 > 0):
        moveit(circle, -1, -1)

    color_circle(circle, "yellow")
    whereis(circle)

    # up and rcircleight
    while (circle.getCenter().y -1 > 0):
        moveit(circle, 1, -1)

    whereis(circle)

    window.close()    # Close window when done

main()

