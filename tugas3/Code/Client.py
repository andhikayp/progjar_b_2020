import logging
import requests
import os
import threading

gambar = ['https://cdn-radar.jawapos.com/uploads/radarsolo/news/2019/12/20/ini-minuman-kekinian-jepang-favorit-milenial-di-solo_m_1576847915_171186.jpg',
          'https://www.ayobandung.com/images-bandung/post/articles/2019/07/03/56666/img_4656_800x533.jpg',
          'https://cdn.idntimes.com/content-images/community/2018/05/1c67b5f13c41729b3780ef6c9ecf46c0_600x400.jpg']

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'
    print(tipe)
    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        namafile = namafile.split('.', 1)[0]
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

threads = []
for i in range(3):
    t = threading.Thread(target=download_gambar,args=(gambar[i],))
    threads.append(t)
    t.start()
