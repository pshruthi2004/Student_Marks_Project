import csv
FILE="students.csv"

def menu():
    while True:
        print("\n1.View Students\n2.Exit")
        ch=input("Enter choice: ")
        if ch=="1":
            with open(FILE,newline="") as f:
                for row in csv.reader(f):
                    print(row)
        elif ch=="2":
            break
        else:
            print("Invalid choice")
