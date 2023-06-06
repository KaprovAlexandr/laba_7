def proc1():
    from PIL import Image

    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)


def proc2():
    from PIL import Image

    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))

    new_img.save("resized_sobaken.jpg")

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("image_flipsobaken_top.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("image_flip_sobaken.jpg")


def proc3():
    from PIL import Image,ImageFilter

    filenames = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.SHARPEN)
            new_img.show()
            new_img.save("new_" + file)


def proc4():
    from  PIL import  Image

    img= Image.open('sobaken.jpg')
    watermark = Image.open('watermark.png')

    img.paste(watermark, (1,2), watermark)
    img.save("water-sobaken.png")

proc1(),proc2(),proc3(),proc4()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
