[![Build Status](https://travis-ci.com/sng23/miniproject2.svg?branch=dev)](https://travis-ci.com/sng23/miniproject2)

# miniproject2

## Project Task List
Task Todo | In Progress | Review | Done | Build Status
--- | --- | --- | --- | ---
Outline / Dependency graph | SG | |
Modules, Plan, Branching, Final PR | SG | |
Stats |JF | | | [![Build Status](https://travis-ci.com/sng23/miniproject2.svg?branch=stats)](https://travis-ci.com/sng23/miniproject2)
RNG |AK | | | [![Build Status](https://travis-ci.com/sng23/miniproject2.svg?branch=rng)](https://travis-ci.com/sng23/miniproject2)
Sampling | | | | [![Build Status](https://travis-ci.com/sng23/miniproject2.svg?branch=sampling)](https://travis-ci.com/sng23/miniproject2)


## Program modules
* Stats functions        
* Rng functions
* Sampling functions
* Calculator functions (from previous homework)

## Recommended Plan of Attack
We need to divide the tasks among the team members in a way that will minimize how much we trip over each other
* Minimize potential for merge conflicts
* One branch per 'module' or one branch per team member
* Dependencies need to be scaffolded first
* Treat dev like you would treat master

## Branching Strategy
* Recommend all branches come off dev and return to dev, master stays pristine
* When starting for the day, pull from the other branches if they have something you depend on
* When ending for the day, push your branch

## Pull Requests (PR) tentative schedule
* The pull request is a fancy `git pull` with comments attached
* Minor PRs from each module to dev, 3-4 days from completion
* One big final PR from dev to master, last day
* Prof. would probably like to see a small discussion in the comments, at least for dev->master
 
## Low Level Operations Dependencies Example
![](images/program%20operations%20diagram.png)
[link to draw.io program diagram](https://drive.google.com/file/d/1-kmcID1HtiE-PwfVW2D8M-OZXasv8nbQ/view?usp=sharing)

## Changelog
* 3/2/20 SG Rough outline for README.md
* 3/8/20 SG Added more to README.md
* 3/8/20 SG Branch calculator off dev, upload calculator project
* 3/9/20 JF assigned Stats to JF
* 3/9/20 JF Moved Calculator.py to its own Calculator directory
* 3/9/20 JF added. static methods for Addition, Subtraction, Division, Sqrt, multiplication, and square to it's own .py
* 3/10/20 JF added mode formula to statistics 
* 3/10/20 JF added mean formula to statistics 
* 3/10/20 JF added median formula to statistics 
* 3/10/20 JF added mean deviation formula to statistics 
* 3/10/20 JF added mode test to test_statistics
* 3/10/20 JF added median test to test_statistics
* 3/10/20 JF added mean deviation test to test_statistics
* 3/12/20 JF added Standard deviation formula to Statistics
* 3/12/20 JF added Standard deviation test to test_statistics
* 3/12/20 JF added Variance test to test_statistics
* 3/12/20 JF added variance formula 
* 3/12/20 JF added  variance to Statistics.py
* 3/12/20 JF added zscore test to test_statistics
* 3/12/20 JF added zscore function
* 3/12/20 JF added zscore to Statistics.py
* 3/12/20 JF added skewness test to test_statistics
* 3/12/20 JF added skewness function
* 3/12/20 JF added skewness to Statistics.py
* 3/13/20 JF added Quartiles test to test_statistics
* 3/13/20 JF added Quartiles function
* 3/13/20 JF added Quartiles to Statistics.py
* 3/13/20 JF added population correlation test to test_statistics
* 3/13/20 JF added population correlation  function
* 3/13/20 JF added population correlation  to Statistics.py
* 3/15/2020 AK Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
* 3/15/2020 AK Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
* 3/15/2020 AK Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
* 3/15/2020 AK Select a random item from a list
* 3/15/2020 AK Set a seed and randomly.select the same value from a list
* 3/15/2020 AK Select N number of items from a list without a seed
* 3/15/2020 AK Select N number of items from a list with a seed
* 3/15/20 SG Moved RandomTests to tests folder and rename file
