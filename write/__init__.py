from csv import *
from tkinter import *
import webbrowser as wb


class Third(object):
    def __init__(self):
        self.t = Tk()
        self.t.title("Website Library")
        self.t.geometry("500x250")
        self.t.configure(background="#ddaf7e")

        self.first = Label(self.t, text="Name Of BookMark and second text box URL Of bookmark", font="Calibri 15", bg="#ddaf7e")
        self.name = Label(self.t, text="Name :", font="Calibri 15", bg="#ddaf7e")
        self.url = Label(self.t, text="URL :", font="Calibri 15", bg="#ddaf7e")
        self.entry1 = Entry(self.t)
        self.entry2 = Entry(self.t)

        self.first.grid(row=0, columnspan=2)
        self.name.grid(row=1, column=0, sticky=E)
        self.url.grid(row=2, column=0, sticky=E)
        self.entry1.grid(row=1, column=1, sticky=W)
        self.entry2.grid(row=2, column=1, sticky=W)
        self.getitall = Button(self.t, text="Get It All", font="Calibri 12", command=lambda: self.getit())
        self.getitall.grid(row=3, column=1, sticky=W, padx=20)

        self.t.mainloop()

    def getit(self):
        with open("website.csv", "a", newline="") as csv:
            w = writer(csv)
            w.writerow([self.entry1.get(), self.entry2.get()])
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)


def main():
    Third()

if __name__ == '__main__':
    main()
