import shelve
import uuid

class DBFile:
    def __init__(self):
        self.data = shelve.open('mydatafile.dat')

    def create_data(self,nama=None,size_file=None,type_file=None):
        if (nama is None):
            return False
        id=str(uuid.uuid4())
        data = dict(id=id, nama_file=nama, size=size_file, type=type_file)
        self.data[id]=data
        return True

    def get_data(self,nama=None):
        for i in self.data.keys():
            try:
                if (self.data[i]['nama_file'].lower() ==nama.lower()):
                    return self.data[i]
            except:
                return False

    def delete_data(self,id=None):
        if (id is None):
            return False
        del self.data[id]

    def list_data(self):
        k = [self.data[i] for i in self.data.keys()]
        return k

if __name__=='__main__':
    p = DBFile()
    p.create_data("vanBasten","621234","png")
    p.create_data("vanPersie","621235","txt")
    p.create_data("vanNistelroy","621236","pdf")
    p.create_data("vanDerVaart","621237","doc")
    print(p.list_data())
    print(p.get_data('vanbasten'))
