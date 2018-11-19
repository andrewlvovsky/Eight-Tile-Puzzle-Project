# Eight Puzzle Project

### Introduction

This project was meant to show how the A* heuristic search is much faster than uniform cost search for puzzles of greater depth. When it comes to an 8-tile puzzle that only takes 1 or 2 moves to solve, uniform cost search might come in handy. However, it makes more sense to rather use one of the heuristic searches, with a preference for Manhattan distance.

### Implementation

For my implementation, I thought about generalizing as much as I could (in the case of needing to switch to a 15-tile puzzle or higher). I created a Puzzle class that handled all the operations, as well as storing the current state of the puzzle and the goal state for cross-referencing. I created a Node class that held a Puzzle object, as well as the path cost g(n) and heuristic cost h(n). Also, I made sure to “prune” repeated states to improve runtime.

For my programming language, I chose Python because I thought it was the easiest to use for this project. After some hours of coding, I had issues with getting removing nodes from the queue properly based on their respective heuristic values. After countless hours of nail-biting and coffee, I forgot that Python calls-by-reference. I was deleting nodes from references the whole time. It was aggravating when I learned about that, but I soon found out about deepcopy and its usefulness in Python as a hard call-by-value function.

### Brief Explanation on Heuristic Functions

Uniform cost search is a search that takes the route with the lowest cost. In the case of this project, h(n) was set to 0 for easy implementation within the queuing function. The A* Misplaced Tile heuristic is as simple as adding all the tiles that are not in their goal state (this was the easiest to implement for me). The A* Manhattan Distance heuristic took some thought, but I soon realized that h(n) takes the misplaced tile heuristic into consideration in checking for which tiles are misplaced, but then adding the amount of moves it takes to get back to its original position. This leads to a more-sound prediction, and thus is the best search function to use thus far.

### Data

For my test cases, I chose 3 puzzles of varying depth. Because of time-constraints, I didn’t choose puzzles that required more than 12 moves to solve for the sake of the uniform cost search’s poor health. On the next page, there are graphs of the number of nodes that were expanded in each case, as well as the maximum size that the queue held throughout the runtime.

![alt text](https://imgur.com/WXtnGIz "Max Size of Queue")

![alt text](https://imgur.com/rUuKeTm "Number of Nodes Expanded")

As seen, the A* Manhattan distance heuristic search surpasses misplaced by a little but uniform cost search by quite a lot (both in terms of time and space). I was a bit surprised to see how a puzzle with a depth of 12 stored more nodes in its queue than the puzzle with a depth of 15.
