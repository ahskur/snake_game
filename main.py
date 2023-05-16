import time
from Snake import *
from food import *
from Scoreboard import *

# Setup screen with size, color of background and title of screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snacc Game")
# Turn of tracer to hide snake movement
screen.tracer(0)


# Define Snake using class
scoreboard = Scoreboard()
snaker = Snake()
food = Food()

# Make screen detects/listen to keyboard but only certain keys - this time only arrows
# Then is going to call a method to move the snake in the direction
screen.listen()
screen.onkey(snaker.up, "Up")
screen.onkey(snaker.down, "Down")
screen.onkey(snaker.left, "Left")
screen.onkey(snaker.right, "Right")


game_is_on = True


while game_is_on:
    # Call for the screen to refresh AFTER the snake moves - So we get smoother animations
    screen.update()
    # After screen refresh wait 0.1 sec before calling the next movement
    time.sleep(0.1)
    # Call one of the class' methods for the snake to move
    snaker.move()

    # Detect collision with food - If the head is less than 15 units distance, if is triggered
    if snaker.head.distance(food) < 15:
        food.refresh()
        snaker.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snaker.head.xcor() > 280 or snaker.head.xcor() < -280 or snaker.head.ycor() > 280 or snaker.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snaker.segments[1::1]:
        if snaker.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()