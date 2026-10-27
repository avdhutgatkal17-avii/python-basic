# Count Frequency of Each Digit

def countFrequency(n: int) -> list:
    freq = [0] * 10

    for digit in str(n):
        freq[int(digit)] += 1

    return freq
