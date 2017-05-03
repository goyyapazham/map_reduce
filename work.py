def words():
    f = open("ulysses.txt", "r")
    words = []
    for line in f:
        h = line.strip('\n').split(' ')
        words += h
    return words

def add(a,b):
    return a + b

def comp(a,b):
    return a if a > b else b

def h_freq(a,b):
    return [1 if a.lower() == x.lower() else 0 for x in b]

def frequency(word):
    w = words()
    return reduce(add, h_freq(word, w))

def h_gfreq(a,b):
    la = a.split(' ')
    la = [x.lower() for x in la]
    nums = [c for c in range(0,len(b)- len(la) + 1)]
    return [1 if la == [b[i] for i in range(x,x+len(la))] else 0 for x in nums] 

def group_frequency(phrase):
    w = words()
    return reduce(add, h_gfreq(phrase, w))

def unique():
    w = words()
    u = []
    for word in w:
        if word not in u:
            u.append(word)
    return u

def most():
    u = unique()
    return [x for x in u if reduce(comp, [frequency(x) for x in u])] 

print frequency('ulysses')
print frequency("said")

print group_frequency("all three")
print group_frequency("to find")

print most()


