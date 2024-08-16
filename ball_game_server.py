import web

class BallGameServer(web.Server):
    port = 8080

    def __init__(self):
        super().__init__()
        self.get_p1 = {}
        self.p1_data = {}

    def on_handle(self, bytes_data, address) -> str:
        msg = bytes_data.decode()
        if msg == "checkStart":
            for k, v in self.get_p1.items():
                print(k, v)
                if v == address or k == address:
                    return 'True'
            return 'False'
        elif msg.startswith("p2Connect@"):
            p1_add = msg.split('@')[1]
            ip, port = p1_add.split(':')
            p1_ip = (ip, int(port))
            if p1_ip in self.p1_data:
                self.get_p1[address] = p1_ip
                return "Connected"
            else:
                return "Error: No such player"
        elif msg == "createGame":
            self.p1_data[address] = [160, 50, 8, 5, 0, 0, 0, 0]
            return "Success"
        else:
            try:
                ip = address
                if ip in self.get_p1:
                    ip = self.get_p1[ip]
                datas = self.p1_data[ip]
            except KeyError:
                return "Error: No such player in game"
            if msg == "getData":
                return ';'.join(map(str, datas))
            elif msg == "update":
                x, y, ax, ay, plat1, plat2, score1, score2 = self.p1_data[ip]
                x += ax
                y += ay
                if x < 10 or x > 310:
                    if x > 0:
                        score1 += 1
                    else:
                        score2 += 1
                    x = 160
                    y = 50
                    ax = -ax
                elif x <= 20 and abs(plat1 - y) < 30:
                    x = 20
                    ax = -ax
                elif x >= 300 and abs(plat2 - y) < 30:
                    x = 300
                    ax = -ax
                if y < 10:
                    y = 10
                    ay = -ay
                elif y > 90:
                    y = 90
                    ay = -ay
                data = [x, y, ax, ay, plat1, plat2, score1, score2]
                self.p1_data[ip] = data
                return "Updated"
            elif msg.startswith("setPlat1:"):
                self.p1_data[ip][4] = int(msg.split(':')[1])
                return "Plat set"
            elif msg.startswith("setPlat2:"):
                self.p1_data[ip][5] = int(msg.split(':')[1])
                return "Plat2 set"
            else:
                return 'Invalid command'

server = BallGameServer()

if __name__ == '__main__':
    server.start()
