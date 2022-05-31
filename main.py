# -------=imports=-------
from PIL import Image
from colorit import color as cl

print("https://GitHub.com/vAPGHv/img2text")

p = 16  # pixel

isbreak = 0

ra = range

img = Image.open(input("Enter image name: "))
print(f"Standart size = {img.size}.")

x = int(round(eval(input("Please, enter width (more than 100 is not recommended): "))))
print(x)
y = int(round(eval(input("Please, enter height (more than 100 is not recommended): "))))
print(y)

img = img.resize((x, y))

imgtxt = []

gn = input(
    "Please, enter gamma name \n 1 - (=, ░, ▒, ▓)\n 2 - (L, J, 7, C, V, T, Y, U, A, X, S, O, D, P, K, M)\n 3 - (., :, =, /, r, (, l, 1, Z, 4, H, 9, W, 8, $, @)\n: ")

gm1 = ["=", "░", "▒", "▓"] * 4  # gamma
gm2 = ['L', 'J', '7', 'C', 'V', 'T', 'Y', 'U', 'A', 'X', 'S', 'O', 'D', 'P', 'K', 'M']  # 2 gamma ver
gm3 = list(".:=/r(l1Z4H9W8$@")  # 3 gamma ver

if gn == "1":
    gm = gm1
elif gn == "2":
    gm = gm2
elif gn == "3":
    gm = gm3
else:
    raise "You enter any number!"

pg = [
    ra(p),
    ra(p, p * 2),
    ra(p * 2, p * 3),
    ra(p * 3, p * 4),
    ra(p * 4, p * 5),
    ra(p * 5, p * 6),
    ra(p * 6, p * 7),
    ra(p * 7, p * 8),
    ra(p * 8, p * 9),
    ra(p * 9, p * 10),
    ra(p * 10, p * 11),
    ra(p * 11, p * 12),
    ra(p * 12, p * 13),
    ra(p * 13, p * 14),
    ra(p * 14, p * 15),
    ra(p * 15, p * 16),
]  # pixel gamma

for y in range(img.size[1]):
    for x in range(img.size[0]):

        pixc = img.getpixel((x, y))  # pixel color
        pixc2 = (pixc[0] + pixc[1] + pixc[2]) / 3  # pixel color
        for n in range(16):
            for i in pg[n]:

                if pixc2 < i:
                    imgtxt.append(gm[n])
                    print(cl(gm[n], pixc), end="")
                    isbreak = 1
                    break
                elif pixc2 >= 255:
                    imgtxt.append("@")
                    print(cl("@", pixc), end="")
                    isbreak = 1
                    break

            if isbreak:
                isbreak = 0
                break

    imgtxt.append("\n")
    print()

with open("img.txt", "w", encoding='utf-8') as f:
    f.write("".join(imgtxt))
