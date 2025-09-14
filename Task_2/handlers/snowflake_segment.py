import numpy as np

def snowflake_segment(start, end, order):
    if order == 0:
        return [start, end]
    
    points = snowflake_segment(start, (2 * np.array(start) + np.array(end)) / 3, order - 1)
    points.pop()
    
    points.extend(snowflake_segment((2 * np.array(start) + np.array(end)) / 3, 
                               (np.array(start) + np.array(end)) / 2 + 
                               np.array([- (np.array(end)[1] - np.array(start)[1]), 
                                          (np.array(end)[0] - np.array(start)[0])]) * np.sqrt(3) / 6, 
                               order - 1))
    points.pop()
    
    points.extend(snowflake_segment((np.array(start) + np.array(end)) / 2 + 
                               np.array([- (np.array(end)[1] - np.array(start)[1]), 
                                          (np.array(end)[0] - np.array(start)[0])]) * np.sqrt(3) / 6, 
                               (np.array(start) + 2 * np.array(end)) / 3, 
                               order - 1))
    points.pop()

    points.extend(snowflake_segment((np.array(start) + 2 * np.array(end)) / 3, end, order - 1))
    
    return points