import pygame
from pygame.locals import *
import time
import numpy as np
import lcm
import sys
sys.path.append('/usr/lib/python3.9/site-packages/')
from mbot_lcm_msgs.twist2D_t import twist2D_t

LIN_VEL_CMD = 100.0 # rad/s
ANG_VEL_CMD = 50.0 # rad/s

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")
# pygame.init()
# pygame.display.set_caption("MBot TeleOp")
# screen = pygame.display.set_mode([100,100])
# pygame.key.set_repeat(5)
time.sleep(0.01)
running = True
fwd_vel = 0.3
turn_vel = 0.785398
# while(running):
    # print("stu")
    # for event in pygame.event.get():
    #     if event.type==pygame.QUIT:
    #         running = False
    #         pygame.quit()
    #         sys.exit()
    #     key_input = pygame.key.get_pressed()  
    #     if(~key_input[pygame.K_LEFT] & ~key_input[pygame.K_LEFT] & ~key_input[pygame.K_LEFT] & ~key_input[pygame.K_LEFT]):
    #         turn_vel = 0
    #         fwd_vel = 0
    #     if key_input[pygame.K_UP]:
    #         fwd_vel = LIN_VEL_CMD
    #     elif key_input[pygame.K_DOWN]:
    #         fwd_vel = -LIN_VEL_CMD
    #     else:
    #         fwd_vel = 0
    #     if key_input[pygame.K_LEFT]:
    #         turn_vel = ANG_VEL_CMD
    #     elif key_input[pygame.K_RIGHT]:
    #         turn_vel = -ANG_VEL_CMD
    #     else:
    #         turn_vel = 0.0
command = twist2D_t()
for i in range(1000):
    command.vx = fwd_vel
    # command.wz = turn_vel
    print( command.vx)
    # print(command.wz)
    lc.publish("MBOT_VEL_CMD",command.encode())
    time.sleep(0.01)
