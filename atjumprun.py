#!/usr/bin/env python
# vim: set ts=4 sw=4 sta et sts=4 ai ci:
"""
@ jump run - a platformer demo

Copyright 2008 Donald E. Llopis (machinezilla@gmail.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301
USA
"""

import os
import sys
import math
import pygame
from pygame.locals import *
from pygame.time import Clock


SCREEN_WIDTH = 256
SCREEN_HEIGHT = 128
SCREEN_WIDTH_HALF = SCREEN_WIDTH / 2
SCREEN_HEIGHT_HALF = SCREEN_HEIGHT / 2
TILEMAP_WIDTH = 25
TILEMAP_HEIGHT = 25
TILE_WIDTH = 16
TILE_HEIGHT = 16
TILE_WIDTH_HALF = TILE_WIDTH / 2
TILE_HEIGHT_HALF = TILE_HEIGHT / 2
TILE_X_MAX = (SCREEN_WIDTH / TILE_WIDTH) + 1
TILE_Y_MAX = (SCREEN_HEIGHT / TILE_HEIGHT) + 1

WORLD_X_MAX = (TILEMAP_WIDTH * TILE_WIDTH) - 1
WORLD_Y_MAX = (TILEMAP_HEIGHT * TILE_HEIGHT) - 1

V_WIDTH = (SCREEN_WIDTH / TILE_WIDTH) / 2
V_HEIGHT = (SCREEN_HEIGHT / TILE_HEIGHT) / 2

GRAVITY = -1
V0 = SCREEN_HEIGHT / 2


def generate_map():
    pass

def main():

    pygame.init()
    clock = Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('@ Jump Run')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    player_img = pygame.image.load("player.png").convert()
    tile_img = pygame.image.load("tile.png").convert()
    star_img = pygame.image.load("star.png").convert()

    tile_map = [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
            0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,
            0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
            0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
            2, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2,
            2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2,
            2, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0, 0, 0, 1, 1,
            2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
            2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 2, 0, 2, 0, 2, 2,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]

    key = [False, False, False, False, False]

    wx = 0
    wy = WORLD_Y_MAX - (TILE_HEIGHT * 2)
    TX = wx / TILE_WIDTH
    TY = wy / TILE_HEIGHT
    prev_TY = TY

    player_jump = False
    player_fall = False

    t = 0.0
    v = 0

    vy = 0

    while True:

        delta = clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    key[0] = True
                if event.key == K_DOWN:
                    key[1] = True
                if event.key == K_LEFT:
                    key[2] = True
                if event.key == K_RIGHT:
                    key[3] = True
                if event.key == K_SPACE:
                    key[4] = True
            elif event.type == KEYUP:
                if event.key == K_UP:
                    key[0] = False
                if event.key == K_DOWN:
                    key[1] = False
                if event.key == K_LEFT:
                    key[2] = False
                if event.key == K_RIGHT:
                    key[3] = False
                if event.key == K_SPACE:
                    key[4] = False

        if key[2]:
            wx -= 2
            if wx < 0:
                wx = 0
            # tile collision check left
            tx = wx / TILE_WIDTH
            ty = wy / TILE_HEIGHT
            i = (ty * TILEMAP_HEIGHT) + tx
            if tile_map[i] == 1:
                tx += 1
                wx = tx * TILE_WIDTH

        if key[3]:
            prev_wx = wx
            wx += 2
            if wx > (WORLD_X_MAX - TILE_WIDTH + 1):
                wx = WORLD_X_MAX - TILE_WIDTH + 1
            # tile collision check right
            tx = (wx+TILE_WIDTH) / TILE_WIDTH
            ty = wy / TILE_HEIGHT
            i = (ty * TILEMAP_HEIGHT) + tx
            if tile_map[i] == 1:
                tx -= 1
                wx = tx * TILE_WIDTH

        if key[4]:
            if not player_jump and not player_fall:
                player_jump = True
                vy = 10

        if player_jump:
            wy -= vy
            vy += GRAVITY
            if vy <= 0:
                player_jump = False
                player_fall = True
                vy = 0

        if player_fall:
            vy -= GRAVITY
            wy += vy
            prev_TY = TY

        # tile collision check up or down
        r = wx % TILE_WIDTH
        s = wy % TILE_HEIGHT

        TX = wx / TILE_WIDTH
        TY = wy / TILE_HEIGHT

        if player_jump:
            tx0 = TX
            tx1 = TX + 1
            ty = TY
            i0 = (ty * TILEMAP_HEIGHT) + tx0
            i1 = (ty * TILEMAP_HEIGHT) + tx1

            a = tile_map[i0] == 1

            if s:
                if r:
                    b = tile_map[i1] == 1
                    c = a or b
                else:
                    c = a

                if c:
                    ty += 1
                    wy = ty * TILE_HEIGHT
                    TY = ty
                    player_jump = False
                    player_fall = True
                    vy = 0
                    s = 0

        if player_fall:

            dy = TY - prev_TY
            if dy > 1:
                dy = dy + 2
            else:
                dy = 2

            ty = TY

            while dy:
                tx0 = TX
                tx1 = TX + 1
                
                if ty >= TILEMAP_HEIGHT:
                    ty = TILEMAP_HEIGHT-1
                i0 = (ty * TILEMAP_HEIGHT) + tx0
                i1 = (ty * TILEMAP_HEIGHT) + tx1

                if s:
                    a = tile_map[i0] == 1
                    if r:
                        b = tile_map[i1] == 1
                        c = a or b
                    else:
                        c = a

                    if c:
                        ty -= 1
                        wy = ty * TILE_HEIGHT
                        TY = ty
                        prev_TY = ty
                        player_fall = False
                        vy = 0
                        break
                ty += 1
                dy -= 1


        # check for player fall
        if not player_fall and not player_jump:
            tx0 = TX
            tx1 = TX + 1
            ty = TY + 1
            if ty >= TILEMAP_HEIGHT:
                ty = TILEMAP_HEIGHT - 1
            i0 = (ty * TILEMAP_HEIGHT) + tx0
            i1 = (ty * TILEMAP_HEIGHT) + tx1

            a = tile_map[i0] == 0

            if r:
                b = tile_map[i1] == 0
                c = a and b
            else:
                c = a

            if c:
                player_fall = True
                vy = 0

        # check for star collection
        index = (TY * TILEMAP_HEIGHT) + TX
        if tile_map[index] == 2:
            tile_map[index] = 0
        if r:
            index = (TY * TILEMAP_HEIGHT) + TX + 1
            if tile_map[index] == 2:
                tile_map[index] = 0
        if s:
            ty = TY+1
            if ty >= TILEMAP_HEIGHT:
                ty = TILEMAP_HEIGHT-1
            index = (ty * TILEMAP_HEIGHT) + TX
            if tile_map[index] == 2:
                tile_map[index] = 0
            if r:
                index = (ty * TILEMAP_HEIGHT) + TX + 1
                if tile_map[index] == 2:
                    tile_map[index] = 0
            
        # adjust the viewport rectangle
        dx_min = 0
        dx_max = 0
        dy_min = 0
        dy_max = 0

        wx_min = (wx + TILE_WIDTH_HALF) - SCREEN_WIDTH_HALF
        if wx_min < 0:
            dx_min = 0 - wx_min
            wx_min = 0

        wx_max = wx_min + SCREEN_WIDTH  - 1
        if wx_max > WORLD_X_MAX:
            dx_max = wx_max - WORLD_X_MAX + 1
            wx_max = WORLD_X_MAX
            wx_min -= dx_max

        wy_min = (wy + TILE_HEIGHT_HALF) - SCREEN_HEIGHT_HALF
        if wy_min < 0:
            dy_min = 0 - wy_min
            wy_min = 0

        wy_max = wy_min + SCREEN_HEIGHT - 1
        if wy_max > WORLD_Y_MAX:
            dy_max = wy_max - WORLD_Y_MAX + 1
            wy_max = WORLD_Y_MAX
            wy_min -= dy_max

        # keep player image centered on the screen otherwise if at 
        # world max/min then let player wander around the screen
        
        px = SCREEN_WIDTH_HALF - (TILE_WIDTH/2)
        py = SCREEN_HEIGHT_HALF - (TILE_HEIGHT/2)

        # moving to the left
        if dx_min > 0:
            px = wx

        # moving to the right
        elif dx_max > 0:
            px =  SCREEN_WIDTH - (WORLD_X_MAX - wx) 

        # moving up
        if dy_min > 0:
            py = wy

        # moving down
        elif dy_max > 0:
            py = SCREEN_HEIGHT - (WORLD_Y_MAX - wy)

        """
        print "wx: %d wy: %d" % (wx, wy)
        print "px: %d py: %d" % (px, py)
        print "dx_min: %d dx_max: %d" % (dx_min, dx_max)
        print "dy_min: %d dy_max: %d" % (dy_min, dy_max)
        print "wx_min: %d wy_min: %d" % (wx_min, wy_min)
        print "wx_max: %d wy_max: %d" % (wx_max, wy_max)
        """

        # draw tilemap
        screen.blit(background, (0, 0))

        x = 0
        y = 0
        sy = 0 - (wy_min % TILE_HEIGHT)
        ty = wy_min / TILE_HEIGHT

        while y < TILE_Y_MAX:
            tx = wx_min / TILE_WIDTH
            sx = 0 - (wx_min % TILE_WIDTH)
            x = 0
            while x < TILE_X_MAX:
                i = (ty * TILEMAP_HEIGHT) + tx
                if tile_map[i] == 1:
                    screen.blit(tile_img, (sx, sy))
                if tile_map[i] == 2: 
                    screen.blit(star_img, (sx, sy))
                sx += TILE_WIDTH
                tx += 1
                if tx == TILEMAP_WIDTH:
                    break
                x += 1
            sy += TILE_HEIGHT
            ty += 1
            if ty == TILEMAP_HEIGHT:
                break
            y += 1

        screen.blit(player_img, (px, py))

        pygame.display.flip()


if __name__ == '__main__':
    main()

