def transformar_string(archivo):
    string = ""
    for y in archivo:
        for x in y:
            if x != '\n' and x != '' and x != ' ':
                string += x
    return string

def comparador(string_1, string_2):
    counter = 0
    tot = 0
    if len(string_1) <= len(string_2):
        tot = len(string_1)
        for y in range(len(string_1)):
            if string_1[y] ==string_2[y]:
                counter += 1
    else:
        tot = len(string_2)
        for y in range(len(string_2)):
            if string_1[y] == string_2[y]:
                counter += 1
    return counter*100.0/tot

nombres = ["AY274119.txt", "AY278488.2.txt", "MN908947.txt", "MN988668.txt", "MN988669.txt"]
 
a = open(nombres[0], "r")
a.readline()
b = open(nombres[1], "r")
b.readline()
c = open(nombres[2], "r")
c.readline()
d = open(nombres[3], "r")
d.readline()
e = open(nombres[4], "r")
e.readline()

string_a = transformar_string(a)
string_b = transformar_string(b)
string_c = transformar_string(c)
string_d = transformar_string(d)
string_e = transformar_string(e)

string = [string_a, string_b, string_c, string_d, string_e]


for x in nombres:
    print("           ", x, end = "")
print()
for y in range(len(nombres)):
    if y == 1:
        print(nombres[y], end = " ")
    else:
        print(nombres[y], end = "   ")
    for x in range(len(nombres)):
        print(round(comparador(string[y],string[x]),2),"                  ", end = "")
    print()
    


