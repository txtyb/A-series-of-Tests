import curses
from time import sleep
s=curses.initscr()
curses.cbreak()
curses.noecho()
hei,wei=s.getmaxyx()
curses.start_color()
curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
w=curses.newwin(0,0)
#w.timeout(500)
w.addstr(int(hei/2)-5,int(wei/2)-5,'Press',curses.A_STANDOUT)
w.addstr(int(hei/2)-5,int(wei/2),' A or',curses.color_pair(1))
w.addstr(int(hei/2)-5,int(wei/2)+5,' Die',curses.color_pair(2))
w.refresh()
w.nodelay(0)
key = w.getch()
if key == ord('a') or  key==ord('A'):
    w.addstr(int(hei/2)-3,int(wei/2),'You Survived.',curses.color_pair(2))
    w.refresh()
else:
    for i in range(0,3):
        curses.flash()
        sleep(0.08)
    w.attron(curses.color_pair(1))
    w.addch(10, 10, '#')
    w.refresh()
    sleep(2)
w.nodelay(1)

