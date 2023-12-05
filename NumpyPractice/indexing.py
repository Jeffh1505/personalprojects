import numpy



dimensions = input().strip().split(' ')
rows, cols = map(int, dimensions)

input_lines = []
for _ in range(rows):
    line = input().strip()
    input_lines.append(line)

# Splitting lines into individual elements and creating a NumPy array
arr = numpy.array([list(map(int, line.split())) for line in input_lines])

print(arr)