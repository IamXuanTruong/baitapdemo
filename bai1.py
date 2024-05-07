def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # Tạo một danh sách các số nguyên
    numbers = [2, 3, 5, 7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20]
    
    # Tính tổng của chúng
    total_sum = sum(numbers)
    print("Tổng của các số là:", total_sum)

    # In ra các phần tử là số chẵn
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Các số chẵn là:", even_numbers)

    # In ra các phần tử là số nguyên tố
    prime_numbers = [num for num in numbers if is_prime(num)]
    print("Các số nguyên tố là:", prime_numbers)

    # Sắp xếp các phần tử tăng dẫn
    sorted_numbers = sorted(numbers)
    print("Các số được sắp xếp tăng dần là:", sorted_numbers)

if __name__ == "__main__":
    main()