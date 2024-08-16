import web
import pygame as pg
import time

port = 8080

conn = web.NetWork(port)

try:
    conn.recv()
    conn.cmd("createGame")

    pg.init()

    window = pg.display.set_mode((960, 300), pg.SCALED)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                conn.close()
                exit()
        conn.cmd("update")
        x, y, ax, ay, pt1, pt2, sc1, sc2 = map(int, conn.cmd("getData").split(';'))
        window.fill((255, 255, 255))
        pg.draw.circle(window, (0, 0, 0), (x * 3, y * 3), radius=15)
        pg.draw.rect(window, (255, 0, 0), (54, pt1 * 3 - 45, 4, 90))
        pg.draw.rect(window, (0, 0, 255), (894, pt2 * 3 - 45, 4, 90))
        pg.display.update()
        time.sleep(0.1)
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
