import web

class WorldServer(web.Server):
    port = 5555

    def __init__(self):
        super().__init__()
        self.player = {}
        self.ply_count = 0
        self.pos = {}
        self.names = {}

    def on_handle(self, bytes_data, address) -> str:
        msg = bytes_data.decode('utf-8')
        if msg == 'countPlayer':
            return str(self.ply_count)
        elif msg.startswith('joinPlayer:'):
            self.player[address] = self.ply_count
            self.ply_count += 1
            self.pos[address] = (0, 0)
            self.names[address] = msg.split(':')[1]
            return 'Joined, ID: ' + str(self.ply_count - 1)
        elif msg.startswith('movePlayer:'):
            _, ax, ay = msg.split(':')
            self.pos[address] = (int(ax) + x, int(ay) + y)
            return 'Moved to ' + str(self.pos[address])
        elif msg.startswith('queryPlayer:'):
            return ':'.join(map(str, self.pos[address])) + ':' + self.names[address]
