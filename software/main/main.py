from .path import Path

path = Path.parse([
    (0, 0), (1, 1), (2, 3)
    ])

print(next(path))

#for s in path:
    #print(s)
