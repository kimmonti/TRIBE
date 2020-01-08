backwards = ['oscreem', 'ueq', 'la', 'óncodificaci', 'ñaense', 'eshabilidad', 'eld', 'losig', '21', 'osusam', 'la', 'óncodificaci', 'moco', 'nau', 'taherramien', 'rapa', 'armostr', 'moco']

correct=[]
for word in backwards:
    correct.append(word[2:] + word[0:2])

print (" ".join(correct))
