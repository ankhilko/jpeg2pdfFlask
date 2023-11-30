
def convert_j2p():
    import jpg2pdf
    with jpg2pdf.create('me.pdf') as new_pdf:
        new_pdf.add('me.jpg')


def conv_p_j(png_img):
    from PIL import Image
    new_img = Image.open(png_img)
    new_img.save('me.jpg')


if __name__ == '__main__':
    convert_j2p()

