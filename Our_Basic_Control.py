# Import necessary packages
import time
import sys
import argparse
import math
import numpy as np
import gym
from gym_duckietown.envs import DuckietownEnv
import cv2


# Parsing the input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--env-name', default=None)
parser.add_argument('--map-name', default='udem1')
parser.add_argument('--no-pause', action='store_true', help="don't pause on failure")
args = parser.parse_args()

# Creating the gym environment for the duckietown simulation
if args.env_name is None:
    env = DuckietownEnv(
        map_name = args.map_name,
        domain_rand = False,
        draw_bbox = False
    )
else:
    env = gym.make(args.env_name)

# Initial reset and render to start 
obs = env.reset()
env.render()

# Variables for the control demonstration
Start = time.time()
Elapsed = 0
Speed = 0.6
Steering = 2.0
i = 0

while True:
    # Changing the directions in every 2 sec
    Elapsed = time.time()
    if((Elapsed - Start) > 2):
        Speed = -1*Speed
        Steering = -1*Steering
        Start = time.time()
        i += 1
    
    # Generating the change in the simulation environment
    obs, reward, done, info = env.step([Speed, Steering])
    ## obs Is the NxMx3 Array of pixels seen through the camera. We will use this as input in our network.
    obs = obs[100:,:,:]

    # Visualizing the cropped image
    cv2.imshow("Cropped", obs)
    key = cv2.waitKey(1) & 0xFF
    if(key == ord('q')):
        cv2.destroyAllWindows()
        break


    # Rendering the actual frame
    env.render()
    
    # After 10 seconds the program closes
    if(i == 5):
        break
