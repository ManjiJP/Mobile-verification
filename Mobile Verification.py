from tkinter import *
from twilio.rest import Client
import random
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.n = str(self.otp())
        self.client = Client("AC3a9fff476ee0b41339a98fea968aa48c", "474618ca556270f6c658da89f0f043dd")
        self.client.messages.create(to=("+971-501477523"),
                                    from_="+15169792042",
                                    body=self.n
                                    )

    def otp(self):
        return random.randrange(1000, 10000)

    def labels(self):
        self.c = Canvas(self, bg="#f3f3d6", width=400, height=280)
        self.c.place(x=290, y=120)
        self.upper_frame = Frame(self, bg= "#4682B4", width=1500, height=130)
        self.upper_frame.place(x=0, y=0)
        self.picture = PhotoImage(file="ps2.png")
        self.k = Label(self.upper_frame, image=self.picture, bg="#4682B4").place(x=220, y=35)
        self.m = Label(self.upper_frame, text="Verify OTP", font="TimesNewRoman 38 bold", bg="#4682B4", fg="white").place(x=350, y=38)

    def Entry(self):
        self.User_Name = Text(self, font="calibri 20", borderwidth=2, wrap= WORD, width=23, height=1)
        self.User_Name.place(x=330, y=200)

    def buttons(self):
        self.submitbuttonImage = PhotoImage(file="submit button.png")
        self.submitbutton = Button(self, image=self.submitbuttonImage, command=CheckOTP(), border=0)
        self.submitbutton.place(x=440, y=330)
        self.resendotpimage = PhotoImage(file="resend.png")
        self.resendotp = Button(self, image=self.resendotpimage, command=self.ReOTP(), border=0)
        self.resendotp.place(x=420, y=430)

    def ReOTP(self):
        self.n = str(self.otp())
        self.client = Client("AC3a9fff476ee0b41339a98fea968aa48c", "474618ca556270f6c658da89f0f043dd")
        self.client.messages.create(to=("+971-501477523"),
                                    from_="+15169792042",
                                    body=self.n
                                    )

    def CheckOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end -1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo("showinfo", "Verification Successful")
                self.n = "done"
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")

        except:
            messagebox.showinfo("showinfo", "Invalid OTP")


if __name__ == "__main__":
    window = otp_verifier()
    window.labels()
    window.Entry()
    window.buttons()
    window.mainloop()
