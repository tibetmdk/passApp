from tkinter import *


class AppSettings():
    appName = 'Safe Password Creator'
    appGeometry = "800x500"


class Labels():
    program_name = Label(text='Safe Password Creator')


class Window():
    def __init__(self):
        self.window = Tk()
        Labels.program_name.pack()  # Make sure to pack the label
        self.window.title(AppSettings.appName)
        self.window.geometry(AppSettings.appGeometry)
        self.window.configure(bg='black')


class PasswordRules():
    def eight_chr_password(self):
        pass

    def twelve_chr_Password(self):
        pass


class Buttons():
    pass


# main code
if __name__ == "__main__":
    app_window = Window()
    app_window.window.mainloop()




