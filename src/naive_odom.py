import math
import numpy as np

class NaiveOdom:
    def __init__(self, r, d, x = 0, y = 0, theta = 0):
        self.r = r
        self.d = d
        self.x = x
        self.y = y
        self.theta = theta
    
    def calculate_odom(self, sr, sl, t):
        