import tkinter
import qrcode
import time
# Basic Code for tk
app = tkinter.Tk()
app.title("QR Code Generator")
app.maxsize(width=500, height=500)
app.minsize(width=500, height=500)
#  This def creates, saves and shows a qrCode 
def create_qr_code(to_save_in_qr, filename):
    qr= qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4,)
    qr.add_data(to_save_in_qr)
    qr.make(fit=True)
    img= qr.make_image(fill_color="black", back_color= "white" ).convert('RGB') 
    img.save(filename)
    img.show()
    print("jo ein qrcode wurde erstellt")

# Get the link and the filename from the input field 
def link_zuweisung():
    global to_save_in_qr2
    global filename
    to_save_in_qr2= link_input.get()
    print(to_save_in_qr2)
    filename= filename_input.get()

# Assignment button       OkButton 
der_assignment_button= tkinter.Button(app, width=20,height=1, text="ok", bg="Orange", command=  
lambda:[link_zuweisung(), 
create_qr_code(to_save_in_qr2, filename)])
der_assignment_button.place(x=172, y=286)
# Input Link 
link_input= tkinter.Entry(app, bg="Pink", width=24, textvariable="link")
link_input.delete(0, "end")
link_input.insert(0, "Link hier!")
link_input.place(x=175, y=230)
# Input Filename
filename_input= tkinter.Entry(app, bg="Pink", width=24)
filename_input.place(x=175, y=260)
filename_input.delete(0, "end")
filename_input.insert(0, "filename! Bitte mit Endung")

app.mainloop()
