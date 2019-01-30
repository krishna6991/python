def resolve(host):
    return socket.gethostbyname(host)

resolve('google.com')
