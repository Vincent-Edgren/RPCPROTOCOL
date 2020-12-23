from xmlrpc.server import SimpleXMLRPCServer

class RPC:
    def __init__(self, address):
        self._methods = ['get', 'set', 'delete', 'exists', 'keys']
        self._data = {}
        self._server = SimpleXMLRPCServer(address, allow_none=True)
        for method in self._methods:
            self._server.register_function(getattr(self, method))
        self._server.serve_forever()

    def get(self, key):
        return self._data[key]
    def set(self, key, value):
        self._data[key] = value
    def delete(self, key):
        del self._data[key]
    def exists(self, key):
        return key in self._data
    def keys(self):
        return list(self._data)

if __name__ == '__main__':
    print('Iniciando el server en el puerto 8000')
    rpc = RPC(('', 8000))