import tkinter
from typing import Text
import qrcode
import time
# Basic Code for tk
app = tkinter.Tk()
app.title("QR Code Generator")
app.maxsize(width=300, height=300)
app.minsize(width=300, height=300)
#  This def creates, saves and shows a qrCode


def create_qr_code(to_save_in_qr, filename):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=30, border=2,)
    qr.add_data(to_save_in_qr)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color,
                        back_color=back_color).convert('RGB')
    img.save(filename+".png")
    time.sleep(5)
    img.show()
# Get the link , color and filname


def assignment():
    global to_save_in_qr2
    global filename
    global back_color
    global color
    to_save_in_qr2 = link_input.get()
    filename = filename_input.get()
    color = color_input.get()
    back_color = back_color_input.get()


# Assignment button       OkButton
assignment_button = tkinter.Button(app, width=20, height=1, text="ok", bg="Orange", command=lambda: [assignment(),
                                                                                                     create_qr_code(to_save_in_qr2, filename)])
assignment_button.place(x=72, y=160)
#  color
color_input = tkinter.Entry(app, bg="Pink", width=24)
color_input.place(x=75, y=90)
color_input.delete(0, "end")
color_input.insert(0, "black")
# Text color
text_color = tkinter.Label(app, text="Color")
text_color.place(x=40, y=90)
#  backgroundcolor
back_color_input = tkinter.Entry(app, bg="Pink", width=24)
back_color_input.place(x=75, y=110)
back_color_input.delete(0, "end")
back_color_input.insert(0, "white")
# Text BackColor
text_back_color = tkinter.Label(app, text="Back_Color")
text_back_color.place(x=10, y=110)
# Input Link
link_input = tkinter.Entry(app, bg="Pink", width=24, textvariable="link")
link_input.place(x=75, y=70)
# Text Link
text_link = tkinter.Label(app, text="Link")
text_link.place(x=45, y=70)
# Input Filename
filename_input = tkinter.Entry(app, bg="Pink", width=24)
filename_input.place(x=75, y=130)
# Text filename
text_filename = tkinter.Label(app, text="Filename")
text_filename.place(x=17, y=130)

app.mainloop()
