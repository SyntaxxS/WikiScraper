import wikipedia
import os
import random
q = open("quelle.txt", "a", encoding="utf-8")
wikipedia.set_lang("de")
id = random.randint(1,99999)
for x in range(11):
    try:
        print(wikipedia.page(random.randint(1,9999)).content, file=q)
    except:
        continue
q.close()
f = open("Wörterbuch.txt", "a", encoding="utf-8")
with open("quelle.txt", "r", encoding="utf-8") as s:
    for i in s:
        for word in i.split():
            print(word.strip("""'0123456789\",.?\(\)»/\][&%$=´}{~^°`§+#*;:«""").lower(), file=f)
f.close()
q.close()
open("quelle.txt", "w").close()
os.remove("quelle.txt")
