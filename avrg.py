def calculate_average(numbers):
    """Вычисляет среднее значение списка чисел."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    """Основная функция."""
    data = [10, 20, 30, 40, 50]
    average = calculate_average(data)
    print(f"Среднее значение: {average}")


if __name__ == "__main__":
    main()
