from bs4 import BeautifulSoup

f = open("words.txt", "r")
g = open("words.final.txt", "w")

for line in f:
    k = BeautifulSoup(line).text
    k = " ".join([x for x in k.split(" ") if len(x) > 5 and not (x.startswith("@") or x.startswith(".mas") or "http" in x or "png" in x or "jpg" in x) ])
    if len(k) > 1:
        g.write("{}\n".format(k.strip()))

f.close()
g.close()
