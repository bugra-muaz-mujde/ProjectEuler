

def get_triangle_counts(triangle_length):
    triangles = []
    for c in range(triangle_length // 2 -1, triangle_length // 3, -1):
        for b in range(c - 1, (triangle_length - c) // 2, -1):
            a = triangle_length - (c + b)
            if a**2 + b**2 == c**2:
                triangles.append([a, b, c])
    return triangles


max_triangles = 0
max_length = 0
for length in range(12, 1001):
    if max_triangles < len(get_triangle_counts(length)):
        max_triangles = len(get_triangle_counts(length))
        max_length = length

print(max_length)



