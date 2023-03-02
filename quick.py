def quick (sequence):
    if len(sequence) < 2:
        return sequence
    else:
        pivot = sequence.pop()
        lower = []
        upper = []
        for item in sequence:
            if item < pivot:
                lower.append(item)
            else:
                upper.append(item)
    return quick(lower) + [pivot] + quick(upper)

                
def quick2(sequence):
    if len(sequence) < 2:
        return sequence
    else:
        pivo = sequence[0]
        lower = [i for i in sequence[1:] if i <= pivo]
        upper = [i for i in sequence[1:] if i > pivo]
        return quick2(lower) + [pivo] + quick2(upper)

lista = [ 5, 8, 5, 9, 2, 18, 49, 100, 70]
print(quick2(lista))
print(quick(lista))