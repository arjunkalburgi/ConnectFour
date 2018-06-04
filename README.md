# ConnectFour

### The Goal 

The requirements of the project were that the project needed to be based off of things we learned in class (algorithms). Most projects were games with GUI's that were shown in-class. I wanted it to be a website, as websites are more accessible. 

### The Approach 

With the help of mentors from the Computer Engineering Club, I built the Flask and Web aspects of the project. Doing design myself as well. 

### The Result

Though I'm extremely proud of the project, feedback from friends was strongly against the design. It was fun to play against the interestingly quirky AI, but the bright primary colours were what people really commented on. 

Visit the site to see for yourself! 



#### Below is the README written as of April 2015

INTRODUCTION

This ConnectFour project was created for our CMPUT 275 class at the University of Alberta. The requirements of the project were that the project needed to be based off of things we learned in class. CMPUT 275 is all about algorithms (search graphs, other trees and dynamic programming) and also included some classes. We decided to do ConnectFour because it satisfies two of the course topics, dynamic programming and classes. 

Our program uses classes to create the Connect Four experience. The actual game logic is really made up of only two functions. The first is a class called board (found in /game/Board.py) that defines the basic rules of the classic Connect Four board, such as 7 rows and 7 columns, and includes numerous functions to play the game, such as adding piece, checking for a winner and clearing the board. The second is the minimax function called SBM (found in /game/connectfour.py) that uses dynamic programming to search through all the possible placements that the computer can put it’s piece, searching for the best move to return to the game. There is more about board and SBM below. 

The order that the following topics are discussed is the exact same order that we went through to create the game. Some of the topics are more about how the game works that about creating the game itself however, so for those of you attempting to recreate this game those topics may not be of much help. Additionally, explanations of how aspects of the game were created will not be discussed thoroughly, but should be discussed well enough to start you on your way. 



BOARD

All files mentioned in this section can be found in the /game/ folder and functions in /game/Board.py.
Our board class was initially very tiny. Slowly we built it up to become the grand file it is now. We started by first initialising (__init__()) the class with number or rows, columns and a board full of zeros. We kept the board as a tuple of lists in an attempt to save ourselves errors down the road in case we tried to overwrite the board in some way. Since tuples are immutable, at least some of the board would be safe from our bubbling selves. We then continued to write print_board(), add_piece() and rm_piece() accordingly. These would allow us to nicely see our board when we were playing in the terminal, add pieces to the board to simulate gameplay and remove a piece for similar reasons already talked about. At this point we could pretty much play ConnectFour with each other, however it was getting very annoying to type in so many commands when playing by ourselves. This prompted the creation of test.py which would go through game states for us. test.py needed a lot more functions though, so we created available_cols() so once the computer filled up a row (which is the only thing it would do at the time) it would know to go to the next one, and checkwin() so that the stupid computer would stop when we beat it. Once we had this very simple version of the game running, we set out to make the computer smarter by creating the heuristic function move_value() and minimax function SBM(). These are both discussed later. 

The board class also has some other functions in it that would come later on in the game’s development. These include clear_board(), immutable(), and overwriting the comparison functions. The comparison functions should be overwritten for all classes and thus done so here. Even though the game does not use them explicitly, the class should be able to stand on it’s own and therefore are present to make it more complete.

The other function placed in Board.py, namely, checkthree2() is discussed below. 



MINIMAX

The minimax algorithm is used to determine which moves a computer player makes in games like tic-tac-toe, checkers, connect four, and chess. These kinds of games are called games of perfect information because it is possible to see all the possible moves. A game like scrabble is not a game of perfect information because there’s no way to predict your opponent’s moves because you can’t see his hand. You can think of the minimax algorithm as similar to the human thought process of saying, “OK, if I make this move, then my opponent can only make two moves, and each of those would let me win. So this is the right move to make.”
- This is an excellent description of minimax functions by Flying Machine Studios, here is a link to the entire article.

It is obvious from the above description that our minimax function needs several important things: a function to switch whose turn the computer is thinking as, a function to assign values to moves that can be made and finally a function to determine what move is the best to make. 

Our minimax function (SBM() for Search Best Move) handles all three of these things, thus making it the core of the computer’s thinking process. At the beginning of the function, it chooses which player it will act as. Then for each of the possible columns we can put a piece in, it assigns a value to putting the piece in the value and adds that value to a recursive call of the same function. And finally, once it gets values for all the pieces that it tried, it can determine which one was the best and return that value for us to use. The second step here makes up the bulk of the function, it is comprised of two substeps. Firstly, calling move_value() and secondly adding the move to the board and recursively calling the function.
move_value() function is part of Board.py (explained above) and is a “heuristic” function (explained furthur below, under Heuristic). Essentially it estimates the value that the particular move could be. 
The second part is a little bit more complicated and is actually the heart of the theory of the minimax function. Above it was explained that in games like this it is best to think ahead to see what the opponent can do to influence your decision. By recursively calling the function, this is effectively what we are doing. Thus we see that we call add_piece() to add a piece in that spot temporarily in order to calculate the best possible return for the opponent, who then also considers the best possible return for you and so on. Once we have a value that is influenced by the recursive calls, we can add it to the heuristic value and clear the piece we just put in with rm_piece(). With this added value, we can compare it to the values taken from attempting the other columns. The maximum of these would then directly influence where the computer plays. 
It is important to discuss the parameters of the function. player is clearly to know which player the computer is acting as at that time, memo stores previous computations in case they come up later, board is the connect four board, required for the heuristic function and so that it knows where it can play and finally, the variable of interest, depth, is the number of recursive calls we call. Going back to the initial explanation of the function, how many times do you think to yourself, “Well then I could go there, then the opponent can go there, then I could go here ...”? The number of times that you switch your thinking, is the effectively the depth of the function. This is why every time SBM() calls itself depth is decremented by 1, eventually it gets to zero, where there is a case to stop recursively calling itself. A further description about how our game uses depth is in below under Levels.

With these recursive functions it can be important to know their run-time. The run-time of this function is O(nx) where n is the number of available columns (usually 7) and x is the depth of the computation. The values that depth takes is also explained below under Levels. 



HEURISTIC

A heuristic evaluation is a review methodology for a quick, cheap and informative way of assessing an interface such as game state. A set of heuristics or general rules of thumb, are used to critique and give values to this game state. At the end of each heuristic evaluation you end up with an overall estimation of the value of the game state. Based on this description, you should be able to figure out how our heuristic function can return a value to the minimax function for a particular move. 

Our function, move_value() in the board class, first determines the row location of where the piece would be, thus getting both the row and column data. Then it estimates this value using another function, checkthree2() located at the bottom of the Board.py file, to check if combinations exist on the board. For example, checkthree2() will look if there are pieces in the board both to the left and to the right of the current piece. Then, based on whose turn the minimax is trying to give a value to, will return whether or not that is a good or bad choice. If it makes or stops a combination of three it will give a high value, but if it makes a combination of three for the opponent it will give a low value. Naturally, if a combination of three does not exist, the function will return a neutral value, namely 0. 

Along with checkthree2() there are sub-functions to help it check for diagonal combinations. The heuristic here is so big that it was getting really confusing to write, so we broke it down into sub-functions. 

It should also be mentioned that we went through several iterations of this heuristic function. All of checkfour(), checkfour2() and checkthree() were created before we finally settled with checkthree2(). We struggled a lot with trying to make the heuristic function any good, it was really tough to create of all those cases and then giving them values. Eventually we settled for checkthree2() because it seemed to work a majority of the time. Sometimes you can play the computer and it acts very stupid, this is due to bugs in the heuristic function not properly evaluating cases. In a more perfect world, our heuristic would have all kinds of different values to evaluate plays with, and our minimax would aggressively use the evaluations. However, in the time constraints we had on the project, and considering how ridiculously intimidating the process of creating a proper heuristic is, it made more sense for us to work on other areas of the project. 



LEVELS

In selecting the difficulty level of the game, the user is allowed to choose three different levels (found in the in home page). When a user chooses a difficulty and clicks submit, a corresponding number will be stored in localStorage. When computing the computer’s turn, the client sends this value to the server to use as the depth of the minimax function. A reminder, the depth will decide how many times the minimax function is recursively called. The larger the depth value, the more computation the computer will compute and the longer the computer takes to play it’s turn. However, it would also make the computer a tougher opponent since it thinks further down the game. 

Right now there are three different levels that the user can choose, corresponding to depths of 3, 5, and 7. Previously we had 5 levels corresponding to depths of 1, 3, 5, 7, and 9. We decided to change this however as a depth of 9 takes too long per step (up to 30 seconds!), and a depth of 1 made the computer so easy that you could win the game in four steps. Thus we reduce the number of levels to three to avoid the “too slow” and “too stupid” conditions. 



FLASK

Flask is a microframework for Python, specifically, Flask is a micro-webdevelopment-framework for Python. It's easy to learn and simple to use, enabling us to make our app a web app in a short amount of time. Flask can be used for building complex, database-driven websites, but here we’ve kept it simple with static HTML pages and a few AJAX calls. The idea was that the website should just be a GUI to the python app that we ran through the terminal. At base level this is exactly what we have, if you don’t understand AJAX, don’t worry, we explain below but if you do you can go to the play() function in /app/templates/base.html file. There you can see that once the user chooses a column and places a piece in it, the function checks if there is a winning combination on the board, then computes where the computer’s play should be, places it on the board and again checks if there is a winning combination on the board. 

To learn and run flask we used the following tutorial, and then built our application using what we learned.

If you want to recreate our app, I would recommend starting with this tutorial. When you are installing extensions you only need to install the flask extension and you can skip most parts of tutorial (only part one, two and fifteen are vital for this app). 



AJAX REQUESTS 

AJAX stands for Asynchronous JavaScript and XML, it is not a new programming language or technique, but it is very useful for exchanging data between a client and a server for websites and web-applications. What makes it so useful is that AJAX can be used to update parts of a web page without reloading the whole page.
Generally, computer’s and users interact by: the user inputs some data or makes a choice by clicking a button that sends the data to the server. The server takes a look at the data and sends back a whole new web page, which is loaded into the browser. Obviously reloading a page every time you want to do something is annoying and time-consuming for the user, especially when you consider our ConnectFour where we really only want to change the colour of simple HTML elements. XMLHttpRequest (AJAX Request) moves the browser-server interaction to behind the scenes, so the user can just keep on playing with the same page, even while elements on the page are talking to the server! This is perfect for our use! To implement AJAX Requests we again mostly followed the guide on the aforementioned tutorial. We simplified the AJAX requests from there and added requests for each function that we have that required data from our python files. 
AJAX requests are asynchronous, which means that they can run parallel to other processes. Unfortunately for us, we needed each step to be synchronous, so we could control whether or not to continue on once we check if there was a winner. In play() we used the fact that AJAX allows us to write code once the function returns back to the client in order to avoid its asynchronous nature. 
On the server side of each of these AJAX requests we manipulate the board depending on which request it is using our previous python game code. The server side of the AJAX requests are in /app/views.py. Here you can get a deeper look at how similar this is to our previous python only code, you can find all the same function calls (in python) as test.py! You’ll notice that for all these AJAX function calls, what is returned to us is always something ‘jsonified’. This is because AJAX only works with strings, we can only communicate strings across. Anything that is not a string, must be made a string and parsed on the other side.



HEROKU and Sessions

What good is a web app if it’s not on the web? After the app was working well while hosting it on the computer, we set to host it via the cloud, thus making it a true web app. Heroku is the cloud application platform that we used to deploy our web app as a website. Heroku is really nice because it’s designed to do all the work of servers, deployment, operations and hosting for us making it really easy to use! All you need is the project uploaded to github and Heroku’s own tutorial. 
Due to the fact that it is so simple and many of the processes are hidden, there’s not really much I can say about it other than it’s great!

However, there is something we can say about the result of putting it on the web. If we had multiple people trying to play the game, it would glitch, because views.py was designed to only handle one game at a time. This resulted in boards from both users overlapping and messing up! Flask has a smart way to fix this called flask.sessions! This gives us the ability to store different variables for different users. However, upon implementation of flask’s sessions we found that trying to store our board class in the session variable gave an error. It seemed that flask’s session variables won’t work with larger variables. To solve this problem, we changed the design of the AJAX requests. Now, the user’s data (namely the board and the difficulty value) is held in localStorage on the website and the AJAX requests send that data to the server to do the computation, which then sends it back and saves it in localStorage. This way, since nothing is stored on the server, multiple users are not confused. 
