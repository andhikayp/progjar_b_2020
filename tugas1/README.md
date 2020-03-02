Andhika Yoga Perdana <br> 05111740000101 <br>

## Tugas 1
### Jalankan program server.py di 3 port yang berbeda (31000, 31001, 31002) 
* Bukti
    Saat server berjalan<br>
    ![Kondisi Awal](foto/3port.JPG)

    Client mengirimkan pesan ke port 31000<br>
    ![Port 31000](foto/31000.JPG)

    Client mengirimkan pesan ke port 31001<br>
    ![Port 31001](foto/31001.JPG)

    Client mengirimkan pesan ke port 31002<br>
    ![Port 31002](foto/31002.JPG)


### Jalankan program client.py untuk konek ke server yang jalan pada poin sebelumnya dan mengirimkan string “JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA” 
* Bukti
    client mengirimkan pesan<br>
    ![Client](foto/31000.JPG)

    server menerima pesan dari clien<br>
    ![Server](foto/3port.JPG)
    

### Jalankan program server.py di 3 port yang berbeda di 2 komputer yang berbeda dan jalankan program client.py untuk konek ke server pada poin sebelumnya, kirimkan string yang sama
* Bukti
    server dijalankan di komputer lain (IP : 10.151.253.11 ). <br>
    client dijalankan di komputer saya dengan IP 10.151.252.209. <br>
    client mengirimkan string "JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA"<br>
    ![Dua komputer yang berbeda : Server](foto/server_safhira.jpg)<br> Server <br>
    ![Dua komputer yang berbeda : Client](foto/client_andhika.JPG)<br> Client <br>

### MODIFIKASILAH program client.py dan server.py agar dapat MENTRANSFER file dari client ke server (letakkan program modifikasi di direktori tugas1a)
* Bukti
    client mengirim file ke server<br>
    ![Client](foto/1a_client.JPG)

    server menerima file<br>
    ![Server](foto/1a_server.JPG)

    bukti file yang dikirimkan<br>
    ![Bukti](foto/1a_hasil.JPG)

### MODIFIKASILAH program server.py agar dapat mengirimkan MENTRANSFER FILE yang di request oleh client (letakkan program modifikasi di direktori tugas1b) 
* Bukti
    client request file ke server<br>
    ![Client](foto/1b_client.JPG)

    server mengirimkan file <br>
    ![Server](foto/1b_server.JPG)

    bukti file yang dikirimkan<br>
    ![Bukti](foto/1b_hasil.JPG)
