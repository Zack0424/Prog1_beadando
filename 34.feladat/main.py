import pandas

n = int(input("n"))
m = int(input("m"))
seats = []
seat_number = 0
for i in range(n):
    row = []
    for j in range(m):
        row.append(seat_number)
        seat_number+=1
    seats.append(row)

df = pandas.DataFrame(seats)
df.reset_index()
print(df)