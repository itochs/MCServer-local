import server

test_server = server.Server()
for log in test_server.start('../minecraft_server/server-v1.19/'):
    print(log)

print("help")
for log in test_server.getHelp():
    print(log)

print("stop")
for log in test_server.stop():
    print(log)