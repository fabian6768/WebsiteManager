from csv import *
from tkinter import *
import webbrowser as wb

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


def main():
    Second()


if __name__ == '__main__':
    main()
