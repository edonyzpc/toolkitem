from blowfish import BF_zipit as bf
data = 'edony'
key = '19430314zpc'
rel = bf(data, 6, key, 12, 1, 2)

filebuf = open('out', 'r').readline().rstrip()
print filebuf
de = bf(filebuf, len(filebuf), key, 12, 0, 2)
