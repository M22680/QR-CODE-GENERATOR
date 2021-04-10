import tkinter
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
    img = qr.make_image(fill_color="black",
                        back_color=color).convert('RGB')
    img.save(filename+".png")
    time.sleep(5)
    img.show()
    print("jo ein qrcode wurde erstellt")

# Get the link , color and filname


def link_assignment():
    global to_save_in_qr2
    global filename
    global color
    to_save_in_qr2 = link_input.get()
    print(to_save_in_qr2)
    filename = filename_input.get()
    color = back_color_input.get()


# Assignment button       OkButton
assignment_button = tkinter.Button(app, width=20, height=1, text="ok", bg="Orange", command=lambda: [link_assignment(),
                                                                                                     create_qr_code(to_save_in_qr2, filename)])
assignment_button.place(x=72, y=160)
# enter the backgroundcolor
back_color_input = tkinter.Entry(app, bg="Pink", width=24)
back_color_input.delete(0, "end")
back_color_input.insert(0, "BackColor")
back_color_input.place(x=75, y=130)
# Input Link
link_input = tkinter.Entry(app, bg="Pink", width=24, textvariable="link")
link_input.delete(0, "end")
link_input.insert(0, "Link ")
link_input.place(x=75, y=70)
# Input Filename
filename_input = tkinter.Entry(app, bg="Pink", width=24)
filename_input.place(x=75, y=100)
filename_input.delete(0, "end")
filename_input.insert(0, "Filename")

app.mainloop()
