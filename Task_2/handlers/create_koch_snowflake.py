import numpy as np
from .create_koch_snowflake import snowflake_segment

def create_koch_snowflake(order, size):
    p1 = np.array([0, 0])
    p2 = np.array([size, 0])
    p3 = np.array([size / 2, size * np.sqrt(3) / 2])
    
    side1 = snowflake_segment(p1, p2, order)
    side2 = snowflake_segment(p2, p3, order)
    side3 = snowflake_segment(p3, p1, order)
    
    points = side1[:-1] + side2[:-1] + side3
    return np.array(points)