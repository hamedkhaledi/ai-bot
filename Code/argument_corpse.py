new = []
with open("../Data/auto_correct/argument_corpse.txt") as f:
    words = f.read().split('\n')
    words.remove('')
    for w in words:
        if ' ' in w:
            new += w.split()
        else:
            new.append(w)

new = list(set(new))
