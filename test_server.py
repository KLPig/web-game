import web

class TestServer(web.Server):
    port = 14514
    def on_handle(self, bytes_data) -> str:
        print("Received:", bytes_data.decode())
        return f"{bytes_data.decode()} is sb"

server = TestServer()

if __name__ == "__main__":
    server.start()
