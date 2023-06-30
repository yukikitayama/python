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

# Use quotechar and quoting to be able to export special characters
with open("special_characters.csv", "w", newline="") as f:
    writer = csv.writer(
        f,
        delimiter=",",
        quotechar="\"",
        quoting=csv.QUOTE_MINIMAL
    )

    writer.writerow(["id", "column", "number"])
    writer.writerow(["1", "Yuki's", "10"])
    writer.writerow(["2", "\"Hello\"", "20"])
    writer.writerow(["3", "a, b, and c", "30"])

with open("dict_writer.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, ["id", "number"])
    writer.writeheader()
    writer.writerow({"id": "1", "number": 10})
    writer.writerow({"id": "2", "number": 20})
