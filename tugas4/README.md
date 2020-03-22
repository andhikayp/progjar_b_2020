Andhika Yoga Perdana <br> 05111740000101 <br>

## Tugas 4
### Meletakkan File
* Bukti
    Saat client berjalan<br>
    ![Kondisi Awal](foto/transfer_client.JPG)
    ![Kondisi Awal](foto/transfer_client1.JPG)
    ![Kondisi Awal](foto/transfer_client2.JPG)

    Saat server berjalan<br>
    ![Port 31000](foto/transfer_server.JPG)

    Hasilnya<br>
    ![Port 31001](foto/transfer_hasil.JPG)


### Mengambil File 
* Bukti
    Saat client berjalan<br>
    ![Kondisi Awal](foto/get_client.JPG)
    ![Kondisi Awal](foto/get_client1.JPG)
    ![Kondisi Awal](foto/get_client2.JPG)

    Saat server berjalan<br>
    ![Port 31000](foto/get_server.JPG)

    Hasilnya<br>
    ![Port 31001](foto/get_hasil.JPG)
    

### Melihat List File
* Client meminta request data file apa saja yang tersimpan pada server
* Server mengirimkan list file yang tersimpan ke client yang berformat JSON
* client menampilkan list file menggunakan dataframe agar mudah dilihat
* Setiap proses yang terjadi pada server tercatat pada log

### Ketentuan Membaca Format
* Format yang digunakan setiap request data adalah dalam bentuk JSON
* Default format json yang digunakan : json.dumps(dict(aksi="transfer", file=message, size=size, type=file_extension))
    
### Daftar Fitur 
* Meletakkan file dari client ke server
    * Komputer client dapat melihat file apa aja yang bisa dikirim ke server
    * Client dapat mengetikkan file apa yang akan disimpan di server
    * Semua tipe ekstensi file dengan berbagai macam ukuran dapat dikirimkan ke server
    * Ada pesan pemberitahuan jika file berhasil dikirimkan atau tidak
    * File yang dikirimkan ke server akan disimpan ke dalam server
    * Identitas file berupa random id, nama file, filesize, dan tipe ekstensi juga disimpan dalam file "mydatafile.dat" di server
    * Setiap proses yang terjadi pada server tercatat pada log
* Melihat list file di server dan menampilkannya pada client
    * Client meminta request data file apa saja yang tersimpan pada server
    * Server mengirimkan list file yang tersimpan ke client yang berformat JSON
    * client menampilkan list file menggunakan dataframe agar mudah dilihat
    * Setiap proses yang terjadi pada server tercatat pada log
* Mengambil file dari server ke client
    * Client mengetikkan file apa yang ingin didapatkan
    * Client mengirimkan request berformat JSON tersebut ke server 
    * Server mengecek apakah file yang diinginkan terdapat pada database server
    * File akan dikirimkan ke client apabila file tersimpan pada database server. Jika file tidak tersimpan di database server maka file tidak akan dikirimkan
    * Client dapat mengetahui status pengirimkan file apakah berhasil atau tidak
    * Setiap proses yang terjadi pada server tercatat pada log
    
    
### Cara Melakukan Request 
* 
   
### Respon yang Didapat
* 
