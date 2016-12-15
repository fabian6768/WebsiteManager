from csv import *
from tkinter import *
from tkinter import messagebox
import webbrowser as wb

a=1

class Second(object):
    def __init__(self):
        self.t = Tk()
        self.t.title("Website Library")
        self.t.geometry("500x350")
        self.t.configure(background="#ddaf7e")

        self.book = []
        self.urls = []
        self.button = []
        self.i = 0
        self.j = 0

        with open("website.csv", newline="") as csv:
            self.csvf = reader(csv)

            for row in self.csvf:
                self.book.append(row[0])
                self.urls.append(row[1])


        for name in self.book:
            self.button.append(Button(self.t, text=name, font="Verdana 15", width=16))
            self.button[self.i].pack(pady=2)
            self.i += 1

        self.i = 0

        for url in self.urls:
            self.button[self.i].configure(command=lambda url=url: self.openwww(url))
            self.i += 1

        self.t.mainloop()

    def openwww(self, url):
        wb.open(url)

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


class WebsiteManager(object):
    def __init__(self):
        """Creating The First Window That Holds Buttons"""
        self.r = Tk()
        self.r.title("Website Library 123")
        self.r.geometry("500x250")
        self.r.configure(background="#ddaf7e")

        '''Configuring So that the First Window holds buttons'''

        self.title = Label(self.r, text="Website Library", bg="#ddaf7e", font="Calibri 26").pack()
        self.divider = Label(self.r, text=" "*100, bg="#ddaf7e").pack()
        self.saved = Button(self.r, text="View Saved Websites", font="Verdana 15", command=lambda: self.newwind(1)).pack(pady=10)
        self.addnew = Button(self.r, text="Add New Websites", font="Verdana 15", command=lambda: self.newwind(2)).pack(pady=10)
        self.r.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.r.mainloop()

    def on_closing(self):
        global a
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.r.destroy()
            a = 0

    def newwind(self, option):

        if option == 1:
            self.r.destroy()
            Second()
        elif option == 2:
            self.r.destroy()
            Third()


def main():
    while a == 1:
        WebsiteManager()


if __name__ == "__main__":
    main()
