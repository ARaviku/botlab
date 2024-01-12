import csv
import time
import numpy as np
import lcm
import sys
import matplotlib.pyplot as plt 

sys.path.append('/usr/lib/python3.9/site-packages/')
from mbot_lcm_msgs.twist2D_t import twist2D_t
from mbot_lcm_msgs.pose2D_t import pose2D_t

x_data = []
y_data = []

def my_handler(channel, data):
    msg = pose2D_t.decode(data)
    timestamp = time.time()  
    data_line = f"{timestamp}, {msg.x}, {msg.y}, {msg.theta}\n"

    print(f"Received data x={msg.x}, y={msg.y}, theta={msg.theta}")
    x_data.append(msg.x)
    y_data.append(msg.y)
    
    with open('odometry_data.txt', 'a') as file:
        file.write(data_line)

lc = lcm.LCM()
subscription = lc.subscribe("MBOT_ODOMETRY", my_handler)
print("Subscribed to MBOT_ODOMETRY")

try:
    while True:
        lc.handle()
except KeyboardInterrupt:

    print("Interrupted by user, exiting.")
except OSError as e:
    print(f"LCM handle error: {e}")
    print("Plotting data.")
finally:
    plt.figure()
    plt.plot(x_data, y_data, marker='o')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Odometry Data (X vs Y)')
    plt.grid(True)
    plt.show()
