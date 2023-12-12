
def convert_j2p(png_img):
    import jpg2pdf
    with jpg2pdf.create(f'{png_img[:-3]}pdf') as new_pdf:
        new_pdf.add(png_img)


def conv_p_j(png_img):
    from PIL import Image
    new_img = Image.open(png_img)
    new_img.save(f'{png_img[:-3]}jpg')


if __name__ == '__main__':

    pass

