# Peter Piu Piu Pygame (PPPP)

This is my final project of CPSC 4970 Python. 
Out of the three final project options, I chose pygame, and I
called it "Peter Piu Piu Pygame". It is a side-scrolling space
shooting game with a world that is greater than the game screen.
![demo1](ppp_demo_images/demo1.png)
![demo2](ppp_demo_images/demo2.png)
![demo3](ppp_demo_images/demo3.png)

--------------------
### Game Components:
Score and Level:

    Score: score starts at zero. Score increases as the player shoots down the antagonists.

    Level: level starts at Medium and remains Medium when the score is below 150. As
        the score reaches 150 or above, level is changed to Hard.

Player:
    
    Spaceship: controlled by the player. Can shoot down antagonists to earn points.
        Game is over once an antagonist hits the spacship.

Antagonists:

    Meteor: +10 points when shot. Appears in Medium and Hard Level.
    UFO: +30 points when shot. Appears in Medium and Hard Level.
    Monster: +50 points when shot. Appears in Hard Level.

----------------
### Game Controls
Left or Right key to move the spaceship left or right.

Press space to shoot. Consecutive press of space key leads to consecutive shooting.

Click Exit on top right of the game screen to exit game.

------------------
### Game Start Menu
Game will start with a start menu in which player is able to choose
starting the game at Medium Level or at Hard Level.

Press 1 to start at Medium Level.

Press 2 to start at Hard Level.

Once game is over (when the spaceship gets hit), the start menu
will be shown to enable restart of the game.

---------------
### Set Up
Install pygame and run main in peter_piu_piu_pygame.py and the game should start.
