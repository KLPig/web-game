import web
import pygame as pg
import time
import input
from tkinter import messagebox as msgbox

port = 8080

conn = web.NetWork(port)

try:
    conn.recv()
    if msgbox.askyesno("Ball Game", "Would you like to join a created game?"):
        addr = input.input_window('Host Address', 'Enter the address of the host to join the game:')
        conn.cmd("p2Connect@" + addr)
        p = 2
    else:
        conn.cmd("createGame")

        msgbox.showinfo("Ball Game", "Waiting for opponent to join...")
        msgbox.showinfo("Ball Game", "Your address: \n" + conn.cmd("getAddr"))

        while not eval(conn.cmd("checkStart")):
            time.sleep(3)
        p = 1

    pg.init()

    window = pg.display.set_mode((960, 300), pg.SCALED)
    font = pg.font.SysFont('Arial', 24)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                conn.close()
                exit()
        conn.cmd("update")
        conn.cmd(f"setPlat{p}:{pg.mouse.get_pos()[1] // 3}")
        x, y, ax, ay, pt1, pt2, sc1, sc2 = map(int, conn.cmd("getData").split(';'))
        window.fill((255, 255, 255))
        pg.draw.circle(window, (0, 0, 0), (x * 3, y * 3), radius=15)
        pg.draw.rect(window, (255, 0, 0), (54, pt1 * 3 - 45, 4, 90))
        pg.draw.rect(window, (0, 0, 255), (894, pt2 * 3 - 45, 4, 90))
        sc1_dis = font.render(str(sc1), True, (127, 0, 0))
        sc1_dis_r = sc1_dis.get_rect(topleft=(0, 0))
        window.blit(sc1_dis, sc1_dis_r)
        sc2_dis = font.render(str(sc2), True, (0, 0, 127))
        sc2_dis_r = sc2_dis.get_rect(topright=(960, 0))
        window.blit(sc2_dis, sc2_dis_r)
        pg.display.update()
        time.sleep(0.1)
except Exception as e:
    msgbox.showerror("Ball Game", "An error occurred: " + str(e))
finally:
    conn.close()
