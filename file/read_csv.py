import csv

# newline="" protects us from incorrect interpretation of the newline character on different platforms
with open("contacts.csv", newline="") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(",".join(row))

# More convenient way
# DictReader treats the first line as header but we can assign it too
with open("contacts.csv", newline="") as f:
    reader = csv.DictReader(f, fieldnames=["name", "phone"])
    for row in reader:
        print(row)

# Save data to CSV
with open("exported_contacts.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")

    writer.writerow(["a", "1"])
    writer.writerow(["b", "2"])
    writer.writerow(["c", "3"])

