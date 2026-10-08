# ⚽ Python Football Match Simulator

A Python command-line football match simulator that generates random events throughout a 90-minute match and tracks team statistics, scores, and individual goal scorers.

## Features

* Create a home and away team
* Add 5 players to each team
* Simulate a full 90-minute football match
* Generate random match events
* Track goals
* Track shots
* Track corners
* Track fouls
* Track yellow cards
* Track individual goal scorers
* Display live match events
* Display half-time score
* Display full-time score
* Display final team statistics
* Add a delay between match events to simulate a live match

## Match Events

The simulator can randomly generate:

* Shot
* Goal
* Corner
* Foul
* Yellow card
* Nothing

The events are randomly selected during each simulated minute.

## Example

```text
Enter the home team: Barcelona
Enter the away team: Real Madrid

Barcelona player 1: Player1
Barcelona player 2: Player2
...

Real Madrid player 1: Player1
Real Madrid player 2: Player2
...

12' Barcelona takes a shot- Player3
27' Goal! Real Madrid- Player2
41' Corner for Barcelona
45' Foul by Real Madrid

_____HALF TIME_____

Barcelona 0 - 1 Real Madrid

58' Yellow Card for Barcelona- Player4
72' Goal! Barcelona- Player1
84' Barcelona takes a shot- Player5

_____FULL TIME_____

Barcelona 1 - 1 Real Madrid
```

## Statistics Tracked

For each team, the simulator tracks:

| Statistic    | Description            |
| ------------ | ---------------------- |
| Goals        | Number of goals scored |
| Shots        | Number of shots        |
| Corners      | Number of corners      |
| Fouls        | Number of fouls        |
| Yellow Cards | Number of yellow cards |

The simulator also records how many goals each player scored.

## How It Works

### 1. Team Setup

The program asks for:

* Home team name
* Away team name
* Five players for each team

Each team receives its own statistics dictionary.

### 2. Match Simulation

The match is divided into two halves:

```text
1 - 45 minutes
46 - 90 minutes
```

For each minute, the program randomly chooses an event.

### 3. Event Processing

Depending on the selected event, the appropriate function is called:

```text
shot()
goal()
corner()
foul()
yellow_card()
```

### 4. Goal Tracking

When a goal occurs, the program:

* Increases the team's goal count
* Increases the team's shot count
* Selects a player who scored
* Records the player's goal total

### 5. Final Statistics

After the match, the program displays the final score, team statistics, and goal scorers.

## Technologies Used

* Python
* `random`
* `time`
* Dictionaries
* Nested dictionaries
* Lists
* Functions
* Loops
* Conditional statements
* Dictionary updates
* Random selection
* String formatting

## How to Run

Make sure Python is installed.

Run:

```bash
python football_match.py
```

No external libraries are required.

## What I Practiced

This project helped me practice:

* Working with nested dictionaries
* Managing multiple pieces of related data
* Creating reusable functions
* Using global program state
* Random event generation
* Using `random.choice()`
* Updating dictionary values dynamically
* Tracking individual players
* Building a time-based simulation
* Using loops to simulate a 90-minute match
* Formatting live terminal output
* Organizing a larger Python program into multiple functions

## Current Limitations

* Match events are completely random.
* Event probabilities are not based on real football statistics.
* There are no substitutions.
* There are no red cards.
* There is no stoppage time.
* There are no assists.
* Player statistics other than goals are not tracked individually.
* The match always runs with a one-second delay per minute.
* Match data is not saved after the program ends.

## Disclaimer

This project is a learning project designed to practice Python programming concepts such as data structures, functions, randomness, loops, and simulation.
