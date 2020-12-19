  
rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan", "Phil", "Eman", "Alex", "Nicholas"], ["Christian", "Josh", "Matt", "Francesco"], ["Patrick", "Nico", "Trevayne"]]
last_initials = ["A", "B", "B", "D", "D", "G", "G", "J", "K", "L", "P", "S", "T", "T", "V", "W"]


for row in rows:
    for index, name in enumerate(row):
        row[index] = name + " " + last_initials[index]
        last_initials

print(rows)