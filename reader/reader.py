import os
from reader.compressed import bzipped, zipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': zipped.opener,
}

class Reader:
    def __init__(self,filename):
        extension = os.path.splittext(filename)[1]
        self.f = opener(filename, 'rt')
        self.f = open(self.filename, 'rt')
    def close(self):
        self.f.close()
    def read(self):
        return self.f.read()
