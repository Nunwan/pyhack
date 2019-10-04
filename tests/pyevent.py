#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()



a=1
while a:
    print("e")
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_RETURN:
                print("bye bye")
                a=0
