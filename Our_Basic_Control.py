
import time
import sys
import argparse
import math
import numpy as np
import gym
from gym_duckietown.envs import DuckietownEnv

parser = argparse.ArgumentParser()
parser.add_argument('--env-name', default=None)
parser.add_argument('--map-name', default='udem1')
parser.add_argument('--no-pause', action='store_true', help="don't pause on failure")
args = parser.parse_args()

if args.env_name is None:
    env = DuckietownEnv(
        map_name = args.map_name,
        domain_rand = False,
        draw_bbox = False
    )
else:
    env = gym.make(args.env_name)

obs = env.reset()
env.render()

Start = time.time()
Elapsed = 0
Speed = 0.6
Steering = 2.0

while True:

    Elapsed = time.time()
    if((Elapsed - Start) > 2):
        Speed = -1*Speed
        Steering = -1*Steering
        Start = time.time()

    obs, reward, done, info = env.step([Speed, Steering])
    ## obs Is the NxMx3 Array of pixels seen through the camera
    obs = obs[:,240:]
    env.render()
