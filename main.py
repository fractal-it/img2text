from PIL import Image

img = Image.open(input("Enter image name: "))
print(f"Standart size = {img.size}.")

x = int(input("Please, enter width (more than 100 is not recommended): "))
y = int(input("Please, enter height (more than 100 is not recommended): "))

img = img.resize((x, y))

pm1 = list(" ░▒▓")
pm2 = list("LJ7CVTYUAXSODPKM")
pm3 = list(".:=/r(l1Z4H9W8$@")
pm4 = list(" ꇺඞ@")

pn = int(input(
    f"Please, select palette \n 1 - {pm1}\n 2 - {pm2}\n 3 - {pm3}\n 4 - {pm4}\n: "
))

selected_p = [pm1, pm2, pm3, pm4][pn-1]
nc = len(selected_p) - 1

colors = list(set(round(round(i/(255/nc))*(255/nc)) for i in range(255)))
colors.sort()
p_dict = {}

for n, col in enumerate(colors):
    p_dict.update({col: selected_p[n]})

imgtxt = []

for y in range(img.size[1]):
    l = []
    for x in range(img.size[0]):
        gray_col = round(sum((img.getpixel((x,y))))/3)
        ito_col = round(round(gray_col/(255/nc))*(255/nc))
        l.append(p_dict.get(ito_col))
    imgtxt.append("".join(l)+"\n")

with open("img.txt", "w", encoding='utf-8') as f:
    f.write("".join(imgtxt))
