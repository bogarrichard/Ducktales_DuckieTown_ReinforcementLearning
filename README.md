# Ducktales_DuckieTown_ReinforcementLearning

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
### Running the simulation with keybord input
#### Run the following in command prompt
```
python3 ./manual_control.py --env-name Duckietown-udem1-v0
```
#### If you are lucky it will open a window and run the simulation. You can control the vehicle with the arrows

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

## Furthert information 
#### For extra info go to the original repository's github page:
https://github.com/duckietown/gym-duckietown
