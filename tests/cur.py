#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.addstr(2, 4, ".")
stdscr.addstr(2, 5, "|")
stdscr.refresh()

while True:
    c = stdscr.getkey()
    if c == "j":
        stdscr.addstr(2, 4, "@")
        stdscr.addstr(2, 3, ".")
    elif c == 'q':
        break
    stdscr.refresh()
