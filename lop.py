
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
   for element in row:
        print(element, end="#")
print()


for letter in "abc":
    for number in range(3):
        print(letter + str(number), end="# ")


ab="MANIK"

for i in (ab):
    for j in (ab):    
        print(f'[{j}]',end="")
    print()
							


mb = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

for i in mb:
    for j in i:    
        print(j,end=" ")
    print()