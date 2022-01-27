from PIL import Image


def showOriginal(original):
    img = Image.open(original)
    img.show()


class DelBackground:

    def __init__(self, im, bg, difference):
        self.original = str(im)
        self.bg = str(bg)
        self.difference = int(difference)
        self.image2 = Image.open(str(im))
        self.height = self.image2.size[1]
        self.wight = self.image2.size[0]
        self.image2 = self.image2.convert("RGBA")
        self.pixels = self.image2.load()

    def isCloseToWipe(self, pix, col):
        dif = 0
        for i in range(3):
            dif += abs(pix[i] - col[i])

        return dif <= self.difference

    def delleteBackGround(self):
        for i in range(self.wight):
            for j in range(self.height):
                if (self.bg == "Black"):
                    if self.isCloseToWipe(self.pixels[i, j], (0, 0, 0)):
                        self.image2.putpixel([i, j], (0, 0, 0, 1))

                elif (self.bg == "White"):
                    if self.isCloseToWipe(self.pixels[i, j], (255, 255, 255)):
                        self.image2.putpixel([i, j], (0, 0, 0, 0))

                elif (self.bg == "Red"):
                    if self.isCloseToWipe(self.pixels[i, j], (255, 0, 0)):
                        self.image2.putpixel([i, j], (0, 0, 0, 0))

                elif (self.bg == "Blue"):
                    if self.isCloseToWipe(self.pixels[i, j], (0, 0, 255)):
                        self.image2.putpixel([i, j], (0, 0, 0, 0))

    def run(self):
        self.delleteBackGround()
        self.image2.show()
