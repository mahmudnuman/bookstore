from tkinter import *
from main import Database

database = Database()


class Window(object):

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)

            self.input_text1.delete(0, END)
            self.input_text1.insert(END,  self.selected_tuple[1])

            self.input_text2.delete(0, END)
            self.input_text2.insert(END,  self.selected_tuple[2])

            self.input_text3.delete(0, END)
            self.input_text3.insert(END,  self.selected_tuple[3])

            self.input_text4.delete(0, END)
            self.input_text4.insert(END,  self.selected_tuple[4])
        except IndexError:
            pass

    def empty_input(self):
        self.input_text1.delete(0, END)
        self.input_text2.delete(0, END)
        self.input_text3.delete(0, END)
        self.input_text4.delete(0, END)

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(),  self.author_text.get(),  self.year_text.get(),  self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(),  self.author_text.get(),
                        self.year_text.get(),  self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(),  self.isbn_text.get()))

        Window.empty_input(self)
        Window.view_command(self)

    def delete_command(self):
        database.delete(self.selected_tuple[0])

        Window.empty_input(self)
        Window.view_command(self)

    def update_command(self):
        database.update(self.selected_tuple[0],  self.title_text.get(),  self.author_text.get(),
                        self.year_text.get(), self.isbn_text.get())

        Window.empty_input(self)
        Window.view_command(self)

    def __init__(self, window):

        self.window = window
        self.window.title('Century Book Store')

        label1 = Label(window, text="Title")
        label1.grid(row=0, column=0)

        label2 = Label(window, text="Author")
        label2.grid(row=0, column=2)

        label3 = Label(window, text="Year")
        label3.grid(row=1, column=0)

        label3 = Label(window, text="ISBN")
        label3.grid(row=1, column=2)

        self.title_text = StringVar()
        self.input_text1 = Entry(window, textvariable=self.title_text)
        self.input_text1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.input_text2 = Entry(window, textvariable=self.author_text)
        self.input_text2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.input_text3 = Entry(window, textvariable=self.year_text)
        self.input_text3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.input_text4 = Entry(window, textvariable=self.isbn_text)
        self.input_text4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.scrol_bar = Scrollbar(window)
        self.scrol_bar.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.scrol_bar.set)
        self.scrol_bar.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self. get_selected_row)

        button1 = Button(window, text="View All",
                         width=12, command=self.view_command)
        button1.grid(row=2, column=3)

        button2 = Button(window, text="Search Book",
                         width=12, command=self.search_command)
        button2.grid(row=3, column=3)

        button3 = Button(window, text="Add Book",
                         width=12, command=self.add_command)
        button3.grid(row=4, column=3)

        button4 = Button(window, text="Update Selected",
                         width=12, command=self.update_command)
        button4.grid(row=5, column=3)

        button5 = Button(window, text="Delete Selected",
                         width=12, command=self.delete_command)

        button5.grid(row=6, column=3)

        button6 = Button(window, text="Close", width=12,
                         command=window.destroy)
        button6.grid(row=7, column=3)


window = Tk()
Window(window)
window.mainloop()
