def find_lis(arr):
    """
    Fungsi untuk mencari Longest Monotonically Increasing Subsequence.
    Mengembalikan panjang LIS dan daftar elemen LIS-nya.
    """
    n = len(arr)
    if n == 0:
        return 0, []

    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    lis_sequence = []
    curr = max_index
    while curr != -1:
        lis_sequence.append(arr[curr])
        curr = parent[curr]

    lis_sequence.reverse()

    return max_length, lis_sequence


def main():
    print("=" * 60)
    print(" PROGRAM LARGEST MONOTONICALLY INCREASING SUBSEQUENCE ")
    print("=" * 60)

    print("\nPilih Mode Input:")
    print("1. Gunakan array contoh default")
    print("2. Input array manual")

    pilihan = input("\nMasukkan pilihan (1/2): ").strip()

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
        arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        print(f"\nMenggunakan array default: {arr}")

    if not arr:
        print("[Warning] Array kosong!")
        return

    length, sequence = find_lis(arr)

    print("\n" + "=" * 40)
    print("HASIL ANALISIS:")
    print("=" * 40)
    print(f"Array Input                          : {arr}")
    print(f"Panjang Subsequence Maksimum (LIS)   : {length}")
    print(f"Elemen Subsequence (Monoton Naik)    : {sequence}")
    print("=" * 40)


if __name__ == "__main__":
    main()
