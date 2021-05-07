from chair import Chair

# # FUNCTIONS

count = 0
best_seat_taking = []
best_seat_taking_count = 0
def show():
    for i in range(n * m):
        if i in range(n,n*m+1,n):
            print()
        print(f'{chairs[i].show:>3}', end=" ")
    print()

def toggle_side(number,check=False):
    for i in range(number - n, number + n + 1, n):
        if i in chair_numbers:
            if not check:
                chairs[i].seatClosed()
            else:
                chairs[i].test_sitable = False
def check_seats(first=False):
    global count, best_seat_taking, best_seat_taking_count
    count = 0
    for i in chairs:
        if i.sitable and i.test_sitable:
            if i.number not in range(0, i.number + 1, n):
                toggle_side(i.number - 1, check=True)
            if i.number not in range(n-1, i.number + 1, n):
                toggle_side(i.number + 1, check=True)
            toggle_side(i.number,check=True)
            count+=1
            if first ==True:
                best_seat_taking.append(1)
                best_seat_taking_count+=1
        elif first==True:
            best_seat_taking.append(0)
    if not first:
        print("Maximum ülési lehetőség: ",count)
    for i in chairs:
        i.test_sitable = True



def toggle(number):
    if number in chair_numbers:
        if chairs[number].sitable:
            if number not in range(0,number+1,n):
                toggle_side(number-1)
            if number not in range(n-1,number+1,n):
                toggle_side(number+1)
            toggle_side(number)
            chairs[number].seatTaken()
            chairs[number].show = "#"
            return True
        else:
            print("Erre a helyre nem lehet ülni")

# # CREATING the nxm grid
while True:
    try:
        n = int(input("n: "))
        m = int(input("m: "))
        if n < 1 or m < 1: raise ValueError
    except ValueError:
        print("Nem megfelelő értékeket adott meg!")
    else:
        break

chairs = [Chair(i) for i in range(n*m)]
chair_numbers = [i.number for i in chairs]
check_seats(first=True)
show()
our_count = 0
while True:
    check_seats()
    if count == 0:
        break
    try:
        x = input("Adja meg a választott ülőhelyet: ")
        if x == "#":
            break
        x = int(x)
    except ValueError:
        print("Csak számokat írjon!")
    else:
        if toggle(x):
            show()
            our_count +=1

message = "Nem szabadítottunk fel helyet / Nem foglalt el minden helyet"
difference = best_seat_taking_count - our_count
with open("best_case.txt", "w")as best_case:
    for i in range(m*n):
        if i in range(n, n * m + 1, n):
            best_case.write("\n")
        best_case.write(str(best_seat_taking[i]))
    best_case.write("\n\n")
    best_case.write(message if difference <= 0 else f"Ennyi helyet szabadíthattunk volna fel, gépi foglalás esetén: {difference}")

with open("our_selection.txt", "w") as our_case:
    for i in range(m*n):
        if i in range(n, n * m + 1, n):
            our_case.write("\n")
        our_case.write("1" if chairs[i].taken else "0")

print("A két fájl sikeresen elkészítve!")















