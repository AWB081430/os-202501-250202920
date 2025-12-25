
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Awwab Maftuhi 
- **NIM**   : 250202920  
- **Kelas** : 1 IKRB

---

## Tujuan 
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum

   - Bahasa pemrograman **bebas** (Python / C / Java / lainnya).  
   - Program berbasis **terminal**, tidak memerlukan GUI.  
   - Fokus penilaian pada **logika algoritma deteksi deadlock**, bukan kompleksitas bahasa.

   Struktur folder (sesuaikan dengan template repo):

   ```
      praktikum/week11-deadlock-detection/
      ├─ code/
      │  ├─ deadlock_detection.*
      │  └─ dataset_deadlock.csv
      ├─ screenshots/
      │  └─ hasil_deteksi.png
      └─ laporan.md
   ```

1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Pengerjaan Praktikum

1. **Menyiapkan Dataset (CSV)**


   |Proses|Allocation|Request|  
   | :---: | :---: | :---: |
   |P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R4 |
   | P4 | R4 | R5 |
   | P5 | R5 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**
   ![alt text](<screenshots/deadlock detection.png>)

3. **Eksekusi & Validasi**

   Secara logis, jika kita menelusuri data:

   P1 butuh R2 (dipegang P2)

   P2 butuh R3 (dipegang P3)

   P3 butuh R4 (dipegang P4)

   P4 butuh R5 (dipegang P5)

   P5 butuh R1 (dipegang P1) -> Kembali ke awal (Siklus terbentuk)

   Validasi: Karena setiap resource hanya memiliki satu unit (single instance) dan terjadi siklus P1→P2→P3→P4→P5→P1, maka sistem 100% berada dalam kondisi deadlock.

4. **Analisis Hasil** 

   | Proses | Resource Held (Allocation) | Resource Wanted (Request) | Status | Alasan Logis |
   | :--- | :--- | :--- | :--- | :--- |
   | P1 | R1 | R2 | **DEADLOCK** | Menunggu R2 yang sedang dikunci oleh P2 |
   | P2 | R2 | R3 | **DEADLOCK** | Menunggu R3 yang sedang dikunci oleh P3 |
   | P3 | R3 | R4 | **DEADLOCK** | Menunggu R4 yang sedang dikunci oleh P4 |
   | P4 | R4 | R5 | **DEADLOCK** | Menunggu R5 yang sedang dikunci oleh P5 |
   | P5 | R5 | R1 | **DEADLOCK** | Menunggu R1 yang sedang dikunci oleh P1 |

   _Mengapa Deadlock Terjadi?_

   Berdasarkan hasil eksekusi, deadlock terjadi karena dataset memenuhi Empat Kondisi Coffman:

   Mutual Exclusion: Setiap resource (R1-R5) diasumsikan hanya bisa digunakan oleh satu proses.

   Hold and Wait: Setiap proses memegang satu resource (contoh: P1 memegang R1) sambil meminta resource lain (R2).

   No Preemption: Resource tidak bisa dilepas paksa dari proses yang sedang memegangnya.

   Circular Wait: Terjadi rantai menunggu yang melingkar antara P1 sampai P5.

   Kesimpulan: Sistem tidak akan pernah bisa menyelesaikan tugasnya karena setiap proses menunggu sumber daya yang tidak akan pernah dilepaskan oleh proses lainnya.
---

## Kesimpulan
   1. Validasi Kondisi Circular Wait melalui Algoritma: Praktikum ini membuktikan bahwa deadlock terjadi akibat adanya rantai ketergantungan sumber daya yang melingkar (Circular Wait). Melalui algoritma deteksi siklus pada Resource Allocation Graph (RAG), program berhasil mengidentifikasi bahwa P1 hingga P5 saling mengunci satu sama lain, sehingga tidak ada proses yang dapat berpindah ke status "Selesai".

   2. Penerapan Teori Single-Instance Resource: Dataset yang digunakan mensimulasikan sumber daya tipe single-instance (satu unit per resource). Hasil eksekusi menunjukkan bahwa dalam kondisi ini, kemunculan satu siklus saja sudah cukup untuk memastikan sistem berada dalam kondisi deadlock. Hal ini memvalidasi teori bahwa tanpa adanya unit sumber daya tambahan, sistem tidak memiliki fleksibilitas untuk keluar dari antrean tunggu.

   3. Pentingnya Intervensi dalam Manajemen Sumber Daya: Hasil analisis menunjukkan bahwa sistem yang mengalami deadlock tidak dapat pulih dengan sendirinya tanpa intervensi eksternal (seperti penghentian paksa proses atau pelepasan sumber daya secara paksa). Hal ini menekankan pentingnya strategi Deadlock Prevention atau Avoidance dalam perancangan sistem operasi untuk menjaga stabilitas performa perangkat lunak.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*? 

   **Jawaban:** 

    > Ketiganya adalah strategi menangani deadlock, namun dilakukan di tahap yang berbeda:

   * Deadlock Prevention (Pencegahan):

      Metode: Memastikan bahwa minimal satu dari empat syarat Coffman (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) tidak pernah terpenuhi.

      Kapan: Dilakukan saat desain sistem atau sebelum proses berjalan.

      Contoh: Memaksa proses meminta semua sumber daya di awal (menghilangkan Hold and Wait).

   * Deadlock Avoidance (Penghindaran):

      Metode: Sistem secara dinamis memeriksa setiap permintaan sumber daya. Jika permintaan tersebut berpotensi membawa sistem ke "Safe State" (kondisi aman), maka diizinkan. Jika tidak (masuk "Unsafe State"), maka ditunda.

      Kapan: Dilakukan setiap kali ada permintaan sumber daya baru (runtime).

      Contoh: Algoritma Banker.

   * Deadlock Detection (Deteksi):

      Metode: Membiarkan deadlock terjadi, namun secara berkala sistem menjalankan algoritma untuk memeriksa apakah ada siklus ketergantungan. Jika ditemukan, sistem melakukan pemulihan (recovery).

      Kapan: Dilakukan secara periodik saat sistem sedang berjalan.

2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  

**Jawaban:**

Meskipun ada cara untuk mencegah atau menghindari, deteksi tetap krusial karena:

* Efisiensi Sumber Daya: Metode prevention dan avoidance sering kali sangat ketat sehingga utilisasi sumber daya menjadi rendah (banyak sumber daya menganggur padahal bisa dipakai). Deteksi memungkinkan penggunaan sumber daya yang lebih maksimal.

* Kompleksitas Rendah: Mencegah semua kondisi deadlock sangat sulit diimplementasikan pada sistem modern yang memiliki ribuan proses dan sumber daya.

* Kasus Tak Terduga: Beberapa jenis sumber daya tidak mendukung pencegahan (misalnya printer yang memang harus eksklusif). Deteksi bertindak sebagai jaring pengaman terakhir jika mekanisme lain gagal.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?

**Jawaban:**

   > Kelebihan:

   * Utilisasi Tinggi: Tidak membatasi proses secara ketat di awal, sehingga sumber daya bisa dipakai secara lebih fleksibel.

   * Sederhana di Awal: Sistem tidak perlu melakukan perhitungan rumit (seperti Algoritma Banker) setiap kali ada permintaan kecil, sehingga performa rutin lebih lancar.

   > Kekurangan:

   * Biaya Pemulihan (Recovery Cost): Jika terdeteksi deadlock, sistem harus mematikan proses atau melakukan rollback. Ini bisa menyebabkan hilangnya data atau pekerjaan yang sedang berjalan.

   * Overhead Algoritma: Menjalankan algoritma deteksi (seperti mencari siklus pada graf) secara terus-menerus bisa memakan waktu CPU.

   * Waktu Tunggu: Proses mungkin sudah macet (stuck) cukup lama sebelum algoritma deteksi dijalankan oleh sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
> Mengalami sakit di tengah cuaca yang kurang menentu/cuaca ekstrem. 
- Bagaimana cara Anda mengatasinya?  
> Menjaga pola hidup dan senantiasa berdoa.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
