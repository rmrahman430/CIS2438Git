# Rayyan Rahman ID: 1893113

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        t = i
        for j in range(i + 1, len(numbers)):
            if numbers[t] < numbers[j]:
                t = j
        numbers[i], numbers[t] = numbers[t], numbers[i]
        for value in numbers:
            print(value, end=" ")
        print()
    return numbers


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
