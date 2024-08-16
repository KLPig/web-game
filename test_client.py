import web

port = int(input("Port: "))

conn = web.NetWork(port)

print('Input end to exit.')
print('Received:', conn.recv().decode('utf-8'))

while True:
    word = input("Enter command: ")
    if word == "end":
        break
    print("Sent:", word)
    conn.send(word.encode('utf-8'))
    response = conn.recv()
    print("Received:", response.decode('utf-8'))
    if response.decode().startswith("Error"):
        break

conn.close()

input("Press enter to continue...")
