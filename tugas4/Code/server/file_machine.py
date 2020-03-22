from dbfile import DBFile
import json
import logging
p = DBFile()

class FileMachine:
    def proses(self,data):
        try:
            if (data['aksi']=='transfer'):
                logging.warning("transfer")
                nama = data['file']
                size = data['size']
                type = data['type']
                p.create_data(nama,size,type)
                return "OK"
            elif (data['aksi']=='list'):
                logging.warning("list")
                hasil = p.list_data()
                return json.dumps(hasil)
            elif (data['aksi']=='get'):
                logging.warning("get")
                nama = data['file']
                hasil = p.get_data(nama)
                return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"

if __name__=='__main__':
    pm = PersonMachine()
    hasil = pm.proses("list")
    print(hasil)
    hasil = pm.proses("get vanbasten")
    print(hasil)