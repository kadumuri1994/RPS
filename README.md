# Rock Paper Scissors

## Description

The familiar game of Rock, Paper, Scissors is played like this: at the same time, two players display one of three symbols: a rock, paper, or scissors. A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.

## Game Rules
1. Winning rules of each of the shapes are as follows:
    - Rock vs Paper -> Paper wins
    - Rock vs Scissors -> Rock wins
    - Paper vs Scissors -> Scissors wins
2. Total number of rounds are 3.
3. If a player wins maximum number of rounds at any particular stage of the game, that player is declared as winner and the game will be terminated.
4. If both players get equal points after all rounds, then the game would be extended with new round/rounds.

### Starting the application:

1. Clone the repository on to your local environment.
2. Navigate to the root folder of this project and open the terminal.
3. Run ```pipenv install``` (Install pipenv on your local env if its not installed). This would create a virtual env for this project and install all the dependencies specified as per pip lock file.
4. Next run ```pipenv shell```. This command would activate the virtual env.
5. Now run the following command to start the game: ```pipenv run python -m main```


### Code Formatter

Black is the code formatter used for this project. For more details refer: https://github.com/psf/black
