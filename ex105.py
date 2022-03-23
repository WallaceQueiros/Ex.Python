def notas(*n):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    return r

#Programa principal
resp = notas (5.5, 2.5, 1.5)
print((resp))