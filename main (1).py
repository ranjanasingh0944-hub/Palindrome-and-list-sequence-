d = {
    "name":["singh","Kumari","Ranjana"],
    "roll_no":[542,456,765]
}

name = "Kumari"
if name in d["name"]:
    index = d["name"].index(name)
    roll_no = d["roll_no"][index]
else:
    roll_no = int(input("Enter roll no: "))
    d["name"].append(name)
    d["roll_no"].append(roll_no)
print("Name:", name, ", Roll No:", roll_no)
print(d)
# 2nd task
a = {"abba", "bbaa", "abbaba", "bbabb"}
for i in a:
    print(i, "is palindrome:", list(i) == list(reversed(i)))