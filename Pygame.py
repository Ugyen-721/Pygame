import turtle 
import os
import math
import random

#set up the screen 
bg = turtle.Screen()
bg.bgcolor("Black")
bg.title("Space Destroyer")
bg.bgpic("Spacebg.gif")

#register the shapes
turtle.register_shape("destroyer.gif")
turtle.register_shape("Player.gif")
#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0
#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-280, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font= ("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player
player = turtle.Turtle()
player.color("blue")
player.shape("Player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#create enemy
enemy = turtle.Turtle()
enemy.color("Red")
enemy.shape("destroyer.gif")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2

number_of_enemies = 5
enemies = []
#add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("Red")
    enemy.shape("destroyer.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

#create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 20

#define bullet state
bulletstate = "ready"

#moving left and right
def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x+= playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bullet as global state
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True 
    else:
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x+= enemyspeed
        enemy.setx(x)
#move the enemy back and down
        if enemy.xcor() > 280:
            #moves all the enemies down
            for e in enemies:
               y = e.ycor()
               y -= 40
               e.sety(y)
            enemyspeed *= -1
    
        if enemy.xcor() < -280:
            for e in enemies:
              y = e.ycor()
              y -= 40
              e.sety(y)
            enemyspeed *= -1
#Check for collision between enemy and bullet
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
#reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
#Update Score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font= ("Arial", 14, "normal"))
    
        if isCollision(bullet, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break  



#move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

#check if bullet has gone to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready" 

delay = input("Press enter to finish.")
