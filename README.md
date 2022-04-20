---------------------------
Peter Piu Piu Pygame (PPPP)
---------------------------
This is my final project of CPSC 4970 Python. 
Out of the three final project options, I chose pygame, and I
called it "Peter Piu Piu Pygame". It is a side-scrolling space
shooting game with a world that is greater than the game screen.

--------------------
### Game Components:
Score and Level:

    Score: score starts at zero. Score increases as the player shoot down the antagonists.

    Level: level starts at Medium and remains Medium when the score is below 150. As
        the score reaches 150 or above level is changed to Hard.

Player:
    
    Spaceship: controlled by the player. Can shoot down antagonists to earn points.
        Game is over once an antagonist hits the spacship.

Antagonists:

    Meteor: +10 points when shot. Appears in Medium and Hard Level.
    UFO: +30 points when shot. Appears in Medium and Hard Level.
    Monster: +50 points when shot. Appears in Hard Level.

----------------
### Game Control

Left or Right key to move the spaceship left or right.
Press space to shoot. Consecutive press of space key leads to consecutive shooting.

Click Exit on top right of the game screen to exit game.

---------------
### Set Up
Run the main program and the game should start.
