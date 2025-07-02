vowels = ('a', 'e', 'i', 'o', 'i', 'u')
print(vowels.index('e'))         # → 1
print(vowels.index('i'))         # → 2
print(vowels.index( 'i',3))   # → 4  (looks in positions 3,4,5)
# If not found:
# vowels.index('x')  # raises ValueError
