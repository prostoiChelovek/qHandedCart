from .Path import Path

path = Path.parse([
    (0, 0), (1, 1),
    (2, 3), (4, 6)
    ])

for s in path:
    print(s)
