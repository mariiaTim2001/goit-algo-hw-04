import numpy as np
import matplotlib.pyplot as plt
from handlers.snowflake_segment import create_koch_snowflake

def main():
    try:
        level = int(input("Enter recursion level (integer ≥ 0): "))
        if level < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    size = 1000

    snowflake_points = create_koch_snowflake(level, size)

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.plot(snowflake_points[:, 0], snowflake_points[:, 1], color='blue')
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    ax.set_title(f"Koch Snowflake – Level {level}")

    plt.show()

if __name__ == "__main__":
    main()
