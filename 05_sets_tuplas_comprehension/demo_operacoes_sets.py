a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # união: {1, 2, 3, 4, 5, 6} -> todos os elementos dos dois
print(a & b)  # interseção: {3, 4} -> só os que estão nos dois
print(a - b)  # diferença: {1, 2} -> só os que estão em 'a', mas não em 'b'
print(b - a)