# Simple Minigames
Video Demo: [https://youtu.be/mpBqloim3m8](https://youtu.be/mpBqloim3m8)
## Description:

This is a project where I implemented 3 simple games and a scoresheet to keep track of scores, where I coded whenever I was free on weekends.

### 1<sup>st</sup> game - Tic-Tac-Toe
Simple game of Tic Tac Toe. Supports PvP and PvE. Was done after I stopped coding for many months so it is likely highly unoptimised.

Consists of 18 functions

- init
    - allows user to choose to play as x or o
- str
    - prints a viewer-friendly status of the board
    - takes in board positions and bolds them (winning positions)
- displaypos
    - helps with debug when i first started (when i had not thought of better ways to fufill that purpose)
    - takes in board postion, prints its value
- saveboard
    - saves a temporary save of the board
- checksetter
    - sets self.board as temporary save (from above)
    - done when i realised board.setter is not used when editting board values
    - strategically placed around the code to periodically check if board is maliciously altered
- start
    - starts game separately after class object is initialised
    - allows player to choose gamemode
- cpu (gamemode 1)
    - allows player to choose between 2 difficulties
        - easy: cpu gives random output
        - easy++: cpu outputs based on my (poorly written) code
    - allows player to choose between who to go first
    - takes leftover symbol (o if player is x, vice-versa)
- computation
    - branches out to other functions based on cpu difficulty to return cpu input positions
- random
    - random function for easy cpu difficulty
    - was an experiment giving random cpu sequences using hash(self) (i still do not know what hash is)
- tttcalculator
    - hard code for easy++ cpu difficulty
    - focuses on going for the win / avoiding losses
    - accesses ttthardcode if no immediate win / loss
- ttthardcode
    - second part of the hard code for easy++ cpu difficulty
    - hardcodes a simple strategy based on player positions
    - only has 1 strategy per situation so it is repetitive over multiple rounds
    - should be able to win / draw no matter what
    - situations
        - if going first, takes center
        - if going second, moves based on player position (if on corner, if on edge, if on center)
- pnp (gamemode 2)
    - will give second player leftover symbol (o if player 1 is x, vice-versa)
- nextmove
    - takes in position and edits self.board on that position
    - knows which symbol to input based on nextplayer function
    - displays differently based on gamemode
    - triggers itself if last turn is not reached
- nextplayer
    - uses a turn counter to determine active player
    - spits out correct symbol for nextmove to use for board input
- checkwin
    - hard coded to check winning all possible positions
    - does not do anything if no wins on board
- end
    - looks scary when called (self.end)
    - takes input for winning player
    - takes input for winning positions
    - prints out congratulatory sentence
    - sets self.lastmove to be true to prevent nextmove from being cyclically called (flaw in my code)
    - is called when turns > 9, player defaults to none and a tie happens
- newgame
    - was called by end to as player if they want to replay
    - creates a new object
    - is not used as replay feature is moved to main
- board (property)
    - checks if board is a valid and if its values are correct
    - is unable to prevent malicious code if they change positional value to a valid input (x, o, .)

### 2<sup>nd</sup> game - Scissors Paper Stone
Another simple game, Scissors Paper Stone. Only supports PvP. It is called this in Singapore but you may know it as Rock Paper Scissors. I decided to code this after spending weeks on Tic Tac Toe. It took me 15 minutes.

Consists of 6 functions

- init
    - sets player and cpu value as 10 by default for no reason
- str
    - prints out what the player and cpu chose
- start
    - starts the game separately after initialising
    - takes in player's move
- computation
    - output cpu's move using python's random module
- faceoff
    - logic to determine winner
- end
    - congratulates winner / print out tie

### 3<sup>rd</sup> game - Connect 4
Last simple game in the collection. Only supports PvP. I wanted to code this before coding for Scissors Paper Stone, but I thought it would be too hard. After finishing Scissors Paper Stone, I wanted to code for this otherwise I would feel defeated. This took me 2 weekends.

Consists of 11 functions

- init
    - does not do much
- str
    - prints viewer-friendly board
- save_board
    - saves temporary save of board
- check_setter
    - updates self.board with temporary save from above
    - done as board.setter is not used if only board values were updated
- start
    - separately starts game after initialisation
    - allows player 1 to choose symbol (x or o), gives player 2 leftover symbol
- next_move
    - uses a turn based system to keeps track of whose move it is
    - if too many turns, triggers tie using end function
- board_input
    - takes in column to update player symbol (based on next_move)
- check_win
    - uses for loops to check vertical wins
    - uses for loops to check horizontal wins
    - also uses for loops to check diagonal wins (with the help of math)
    - main reason why i did not think i could code this initially
- end
    - if player argument is provided, they are the winner
    - if not provided, it is a tie
- board (property)
    - checks if board is a valid list
    - checks each value in nexted list if they are valid (x, o, .) using for loop

### Score Sheet
I thought of making the score sheet after finishing the code for Tic Tac Toe. It will only display score of games if they are played. It takes inputs with a format of (gametype(int), winner(str))

### Main
The first function in this readme not in a class.

Starts by welcoming the player, then starting the games, both facillitated by the other 3 functions in this code. Replay feature was implemented here.

Results are inputted into the score sheet object.

### Start Game
The first function at the same indentation of main().

Allows player to choose which game to play.

Automatically returns results of each game to main, allowing scores to be tracked.

### Welcome
The second function at the same indentation of main().

Prints the welcome message (with a secret ;))

A simple "Press Enter to Continue" which might take in user input?

### ~~Secret~~
~~The third and final function at the same in indentation of main().~~

~~Checks if the user input was the secret password.~~

~~Allows the main player to breeze through all the games.~~

# Conclusion
It was a fun experience and first step into coding. Throughout the project, I found joy in thinking and implementing different features into my code.

There were more that I wished I could do, such as making a better user UI (I wonder if it is possible to code a clickable UI)
, but I thought that I wanted to start CS50X ASAP. Also, the code was meant to only consist of TicTacToe and I scrambled to think of and code in the Score Sheet and 2 other games after re-reading the project requirements (I had not made the 3 other functions at main() indentation at that time). I think I could have coded in a way where pytest can be used better but I was too late to realise my functions do not return, and I used self.___ instead to save data. This made pytest hard to implement and my workflow for coding is still amateurish where checks are hard to make and I learnt that. Nevertheless, it is too much of a hassle to redo all my code at this point unfortunately.

I dont know what else to type here.

Thanks for reading
