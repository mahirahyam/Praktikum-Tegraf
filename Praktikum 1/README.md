## Penjelasan Kode

---

### **1. Pendefinisian Fungsi `find_lis(arr)`**

Section ini berisi logika utama *Dynamic Programming* untuk mencari panjang LIS dan merekonstruksi urutan elemennya.

```python
def find_lis(arr):
    """
    Fungsi untuk mencari Longest Monotonically Increasing Subsequence.
    Mengembalikan panjang LIS dan daftar elemen LIS-nya.
    """
    n = len(arr)
    if n == 0:
        return 0, []

```

* **`n = len(arr)`**: Menghitung jumlah elemen dalam array input.
* **`if n == 0`**: *Edge case handler* untuk menangani kondisi jika array yang dimasukkan kosong.

---

### **2. Inisialisasi Struktur Data DP**

```python
    # dp[i] menyimpan panjang LIS yang berakhir di elemen arr[i]
    dp = [1] * n
    # parent[i] menyimpan indeks elemen sebelumnya untuk mereduksi jalur LIS
    parent = [-1] * n

```

* **`dp = [1] * n`**: Membuat list `dp` berukuran `n` dengan nilai awal `1`. Setiap elemen minimal memiliki panjang LIS `1` (yaitu dirinya sendiri).
* **`parent = [-1] * n`**: Membuat list `parent` dengan nilai awal `-1`. List ini dipakai untuk meacak (*backtrack*) indeks elemen sebelum `i` dalam urutan LIS.

---

### **3. Proses Dynamic Programming (Iterasi & Transisi)**

```python
    # Proses Dynamic Programming
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

```

* **`for i in range(1, n)`**: Loop luar untuk memeriksa setiap elemen mulai dari indeks ke-1 hingga akhir.
* **`for j in range(0, i)`**: Loop dalam untuk membandingkan elemen `arr[i]` dengan semua elemen sebelumnya `arr[j]`.
* **`if arr[j] < arr[i] and dp[j] + 1 > dp[i]`**: Syarat kondisi LIS:
1. `arr[j] < arr[i]`: Memastikan nilai elemen monoton naik (semakin besar).
2. `dp[j] + 1 > dp[i]`: Memastikan jika mengambil elemen `arr[j]` sebelum `arr[i]` akan menghasilkan LIS yang lebih panjang dari nilai `dp[i]` saat ini.


* **`dp[i] = dp[j] + 1`**: Memperbarui panjang LIS pada indeks `i`.
* **`parent[i] = j`**: Menyimpan indeks `j` sebagai elemen pendahulu dari `i`.

---

### **4. Pengambilan Hasil & Rekonstruksi Jalur (*Backtracking*)**

```python
    # Cari nilai maksimum di dp dan indeks akhirnya
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Rekonstruksi subsequence dari indeks akhir ke awal
    lis_sequence = []
    curr = max_index
    while curr != -1:
        lis_sequence.append(arr[curr])
        curr = parent[curr]

    # Balik urutan karena rekonstruksi dilakukan dari belakang
    lis_sequence.reverse()

    return max_length, lis_sequence

```

* **`max_length = max(dp)`**: Mengambil nilai tertinggi dari list `dp` sebagai panjang LIS maksimum.
* **`max_index = dp.index(max_length)`**: Mencari posisi indeks tempat LIS maksimum tersebut berakhir.
* **`while curr != -1`**: Melakukan perulangan mundur dari `max_index` memanfaatkan indeks pada list `parent` hingga mencapai titik awal (`-1`).
* **`lis_sequence.reverse()`**: Membalik susunan list karena penelusuran *backtracking* bergerak dari elemen belakang ke depan.

---

### **5. Fungsi Utama `main()` dan Antarmuka Interaktif**

```python
def main():
    print("=" * 60)
    print(" PROGRAM LARGEST MONOTONICALLY INCREASING SUBSEQUENCE ")
    print("=" * 60)

    # Fitur fleksibilitas: Pilihan opsi input angka
    print("\nPilih Mode Input:")
    print("1. Gunakan array contoh default")
    print("2. Input array manual")

    pilihan = input("\nMasukkan pilihan (1/2): ").strip()

```

* Menyediakan tampilan menu CLI di terminal agar pengguna bisa memilih antara data pengujian bawaan (*default*) atau memasukkan angka sendiri.

---

### **6. Penanganan Input & Validasi Data**

```python
    if pilihan == "2":
        try:
            input_str = input(
                "Masukkan deretan angka (pisahkan dengan spasi): "
            )
            arr = list(map(int, input_str.strip().split()))
        except ValueError:
            print("[Error] Input harus berupa angka-angka yang dipisah spasi!")
            return
    else:
        # Contoh dataset default
        arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        print(f"\nMenggunakan array default: {arr}")

    if not arr:
        print("[Warning] Array kosong!")
        return

```

* **`input_str.strip().split()`**: Memecah string input pengguna berdasarkan spasi.
* **`map(int, ...)`**: Mengonversi setiap elemen teks menjadi tipe data integer.
* **`try-except ValueError`**: Mencegah program *crash* jika pengguna memasukkan karakter non-angka.

---

### **7. Pemanggilan Fungsi & Pencetakan Output**

```python
    # Jalankan algoritma
    length, sequence = find_lis(arr)

    # Tampilkan Hasil Output
    print("\n" + "=" * 40)
    print("HASIL ANALISIS:")
    print("=" * 40)
    print(f"Array Input                          : {arr}")
    print(f"Panjang Subsequence Maksimum (LIS)   : {length}")
    print(f"Elemen Subsequence (Monoton Naik)    : {sequence}")
    print("=" * 40)


if __name__ == "__main__":
    main()

```

* **`length, sequence = find_lis(arr)`**: Memanggil fungsi `find_lis` dan menyimpan hasilnya ke dalam variabel `length` dan `sequence`.
* **`if __name__ == "__main__":`**: Memastikan fungsi `main()` hanya dieksekusi jika file skrip dijalankan secara langsung.

---
## Dokumentasi
