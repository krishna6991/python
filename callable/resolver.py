import socket
//callable instancee
class Resolver:
    def __init__(self):
        self.__cache = {}

    def __call__(self,host):
        if host not in self.__cache:
            self.__cache[host] = socket.gethostbyname(host)

        return self.__cache[host]
    def clear(self):
        self.__cache.clear()

    def has_host(self,host):
        return host in self.__cache
