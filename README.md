# Ducktales DuckieTown ReinforcementLearning project
This is a homework project for an elective subject at Budapest University of Tehcnology and Economics 

## Getting started

The following instructions are to be executed on Linux. (We executed them successfully on Ubuntu 18.04.3 LTS)

### 1. The following tools/software are inevitable

- Python
- pip
- git

#### To install them on Ubuntu run the following instructions in the command prompt
```
apt-get install python3
apt-get install python3-pip
apt-get install git
```
### 2. The neccessary packages and the git repository
```
pip3 install --upgrade pip

git clone https://github.com/duckietown/gym-duckietown.git
cd gym-duckietown
pip3 install -e .
```
### Getting the content of this repository
```
cd ~
git clone https://github.com/bogarrichard/Ducktales_DuckieTown_ReinforcementLearning.git
```
### Injecting our code into the original repository's environment
Now copy the files from your local Ducktales_DuckieTown_ReinforcementLearning repository to the local gym-duckietown (Except the Readme file of course)
#### Run the following in command prompt
```
cd gym-duckietown
python3 Our_Basic_Control.py
```
#### If you are lucky it will open a window and run the simulation with our basic conrtol demonstration.

## Troubleshooting

#### There is a high probability that you're gonna encounter some issues during the steps above.
#### Here are a few of them and the solutions worked for us.

### 1. Pyglet problem
#### If there is a problem with pyglet maybe you should try installing it separately because for some reasons it wasn't among
#### the other dependencies.
```
pip3 install pyglet
```
### 2. Can't find setup.py
#### No universal solution found yet

## Further information 
#### For extra info go to the original repository's github page:
https://github.com/duckietown/gym-duckietown
