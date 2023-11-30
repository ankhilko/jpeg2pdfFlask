import os
import img2pdf
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


def date_turn():
    y = str(datetime.now().year).zfill(4)
    m = str(datetime.now().month).zfill(2)
    d = str(datetime.now().day).zfill(2)
    h = str(datetime.now().hour).zfill(2)
    mn = str(datetime.now().minute).zfill(2)
    s = str(datetime.now().second).zfill(2)
    ms = str(datetime.now().microsecond).zfill(4)

    return y + m + d + h + mn + s + ms


def converter_func(jpeg_path=os.getcwd(), output_path=os.getcwd(), file_name='file', format=None):
    dir_list = os.listdir(jpeg_path)
    start = 0
    if dir_list:
        for name in dir_list:
            if '.jpg' in name:
                start = 1
                break
    if start:
        file_path = f'{output_path}/{file_name}_{date_turn()}.pdf'

        if format in ['a4', 'A4']:
            layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297)))
            with open(file_path, 'wb') as file:
                file.write(img2pdf.convert([f'{jpeg_path}/{page}' for page in dir_list if page.endswith('.jpg')], layout_fun=layout))
        else:
            with open(file_path, 'wb') as file:
                file.write(img2pdf.convert([f'{jpeg_path}/{page}' for page in dir_list if page.endswith('.jpg')]))


@app.route('/')
def index():
    title = 'JPG to PDF converter'
    return render_template('hello.html', title=title)


@app.route('/about')
def about():
    names = ['John', 'Mary', 'Barry', 'Mess']
    title = 'About Online-JPG-to-PDF-Converter'
    return render_template('about.html', names=names, title=title)

