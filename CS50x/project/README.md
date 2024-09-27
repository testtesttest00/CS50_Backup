# Simple Minigames v2
Video Demo: [https://youtu.be/4cKpMAWzN1Y](https://youtu.be/4cKpMAWzN1Y)
## Description:

This is a project where I implemented a few minigames using C, Python and HTML (Flask).

### 1<sup>st</sup> language - Python
An extension of my code from my CS50P final project. I have a newly implemented game, 15 Puzzle. The main function I had to code for
was used the moving of the blank tile on the grid. Using this movement function, I was able to scramble the board by running the
function for a random number of times, in a random direction. There is nothing much to write about as used the mainframe from my
previous project and all I did was to add on to the existing code.

*self-note: easiest to code, took approximately 6 hours (given cs50p experience)

### 2<sup>st</sup> language - HTML (Flask)
I implemented the 15 puzzle game on a website! When thinking of games to code for at the start of the project, I stumbled across a
web-app of the 15 puzzle game, and I wanted to see if I could create my version of it. I started off with making a survey/feedback page
as I wanted to remember how flask, requests, redirects etc. worked which took like 3 hours... Then came the coding of the game itself.
In the army camp during admin time, I rewatched the CS50x lecture as I recalled seeing AJAX being demonstrated and I knew I had to use
it on my web application. Went home, surfed the internet coded it in and the next day I wanted to implement key listeners to touch up
on my web api skills. Afterwords I made a leaderboard to test my AJAX skills without getting help from online resources as much as I
could (Besides, I wanted a leaderboard since my python version has a scoresheet).

*self-note: moderately easy to code, took approximately 10 hours (was good that flask was on python :p)

### 3<sup>st</sup> language - C
The final boss was C. I recalled how much I struggled on Problem Set 5 - Speller as I wanted to make an array of array of linked list,
making the memory management a huge mess. I wanted to challenge myself by doing the same again but there really was no point in doing
so. Coding the main game was simple enough and it took one day (of approximately 6 hours), but I took a shortcut in my controls
mechanic, using a clunky 0123 number input but it was convenient. I wanted to make my own version of get_string and get_int but I
figured it took too much time and I wanted to finish my game. Wanting to match my HTML version, I created a leaderboard which was the hard part. I used file I/O to store data since I could not use an SQL database like I did on Flask. I made an hash table (array) of
linked lists to categorise the leaderboard records based on movements taken. I wanted a challenge so I made use of a merge sort
to sort the hash table in order from lowest to highest moves, which surprisingly only took one day of 8 hours. Glad it is over now...

*self-note: hardest to code, took approximately 32 hours over 4 days x.x

# Conclusion
It was a fun and challenging. I made good use of my time learning new skills, especially with the language C, which solidified my
basics with computer memory and pointers. Also, I learnt of the time-complexity of different algorithms. I enjoyed learning SQL and
realised it uses. I also learnt a lot of website-building which I have tried learning when I was younger, but could not understand.
Making notes for SQL and HTML was tiring but helped me internalise my learnings. All in all, it was an enjoyable and beneficial
experience. I am very grateful for CS50x for providing a platform, helper AI, practical problem sets and engaging and informative
lectures for free online for anyone to access and learn. Thank you.

I dont know what else to type here.

Thanks for reading
