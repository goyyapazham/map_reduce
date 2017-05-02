def words():
    with open("ulysses.txt", "r").read().strip().split("\n") as lines:
        words = []
        for line in lines:
            words += line.split(" ")

def frequency(word):
    words = words()

