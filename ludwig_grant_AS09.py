# File Name: ludwig_grant_AS05.py
# File Path: /home/ludwigg/Python/PyRpi_AS9/ludwig_grant_AS09.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS9/ludwig_grant_AS09.py

# Grant Ludwig
# 10/25/2019
# AS.09
# Have three balls bounce in a line

from graphics import *
import math
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BALL_RADIUS = 10
NUM_BALLS = 3
WALL_WIDTH = 25
ballDiameter = BALL_RADIUS * 2

balls = []
velocities = []

colors = ["Red",
          "Green",
          "Blue",
          "Purple",
          "Pink",
          "Yellow",
          "Orange",
          "Brown"]

win = GraphWin("Ball Bounce", SCREEN_WIDTH, SCREEN_HEIGHT, autoflush=False)

def setupBalls():
    randomColors = random.sample(colors, NUM_BALLS)

    leftBall = Circle(Point(100,250), BALL_RADIUS)
    middleBall = Circle(Point(250,250), BALL_RADIUS)
    rightBall = Circle(Point(400,250), BALL_RADIUS)
    
    leftBall.setFill("Green")
    middleBall.setFill("Red")
    rightBall.setFill("Blue")

    leftVelocity = [5, 0]
    middleVelocity = [5, 0]
    rightVelocity = [-5, 0]

    balls.append(leftBall)
    balls.append(middleBall)
    balls.append(rightBall)

    velocities.append(leftVelocity)
    velocities.append(middleVelocity)
    velocities.append(rightVelocity)

    for ball in balls:
        ball.draw(win)

def createWalls():
    leftWall = Rectangle(Point(0, 0), Point(WALL_WIDTH, SCREEN_HEIGHT))
    rightWall = Rectangle(Point(SCREEN_WIDTH - WALL_WIDTH, 0), Point(SCREEN_WIDTH, SCREEN_HEIGHT))

    leftWall.setFill("Black")
    rightWall.setFill("Black")

    leftWall.draw(win)
    rightWall.draw(win)

def main():
    win.setBackground("Grey")

    setupBalls()
    createWalls()

    while(True):
        for i in range(0, len(balls)):
            location = balls[i].getCenter()
            if location.x >= SCREEN_WIDTH - WALL_WIDTH - BALL_RADIUS:
                velocities[i][0] = -abs(velocities[i][0])
            elif location.x <= BALL_RADIUS + WALL_WIDTH:
                velocities[i][0] = abs(velocities[i][0])

            for j in range(i + 1, len(balls)):
                ball2Loct = balls[j].getCenter()
                if math.sqrt((ball2Loct.x - location.x)**2 + (ball2Loct.y - location.y)**2) <= (2 * BALL_RADIUS):
                    velocities[i][0] = -velocities[i][0]
                    velocities[j][0] = -velocities[j][0]

            for i in range(0, len(balls)):
                balls[i].move(velocities[i][0], velocities[i][1])

            update(30)
    win.close()    # Close window when done

main()