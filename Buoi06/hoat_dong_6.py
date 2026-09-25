# Hoạt động 6: Đệ quy – Giai thừa, Fibonacci

# Bài tập 6.1: Giai thừa
def giai_thua_de_quy(n):
    if n <= 1:
        return 1
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

# Bài tập 6.2: Fibonacci
def fibonacci_de_quy(n):
    if n <= 1:
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


# --- CHẠY THỬ CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    print("=== HOẠT ĐỘNG 6 ===")
    print("Giai thua 5 (de quy vs lap):", giai_thua_de_quy(5), "-", giai_thua_lap(5))
    
    print("\n10 so Fibonacci dau tien:")
    for i in range(10):
        print(fibonacci_de_quy(i), end=" ")
    print()

