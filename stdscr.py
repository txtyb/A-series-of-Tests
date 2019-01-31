import curses
from time import sleep
stdscr=curses.initscr()
stdscr.timeout(500)
curses.start_color()
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_GREEN)
stdscr.addstr(10,10,'Surprise Mother Fucker',curses.color_pair(1))
stdscr.refresh()
stdscr.touchwin()
stdscr.refresh()
curses.flash()
stdscr.nodelay(0)
key=stdscr.getch()
if key == ord('a'):
    stdscr.addstr(12,10,'Oh Hahahahahah',curses.A_STANDOUT)
    stdscr.refresh()
stdscr.nodelay(1)
