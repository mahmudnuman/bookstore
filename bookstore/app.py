from tkinter import *
import main


def get_selected_row(event):
    try:

        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)

        input_text1.delete(0, END)
        input_text1.insert(END, selected_tuple[1])

        input_text2.delete(0, END)
        input_text2.insert(END, selected_tuple[2])

        input_text3.delete(0, END)
        input_text3.insert(END, selected_tuple[3])

        input_text4.delete(0, END)
        input_text4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def empty_input():
    input_text1.delete(0, END)
    input_text2.delete(0, END)
    input_text3.delete(0, END)
    input_text4.delete(0, END)


def view_command():
    list1.delete(0, END)
    for row in main.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in main.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    main.insert(title_text.get(), author_text.get(),
                year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                 year_text.get(), isbn_text.get()))

    empty_input()
    view_command()


def delete_command():
    main.delete(selected_tuple[0])

    empty_input()
    view_command()


def update_command():
    main.update(selected_tuple[0], title_text.get(), author_text.get(),
                year_text.get(), isbn_text.get())

    empty_input()
    view_command()


window = Tk()
window.title('Century Book Store')

label1 = Label(window, text="Title")
label1.grid(row=0, column=0)


label2 = Label(window, text="Author")
label2.grid(row=0, column=2)


label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label3 = Label(window, text="ISBN")
label3.grid(row=1, column=2)

title_text = StringVar()
input_text1 = Entry(window, textvariable=title_text)
input_text1.grid(row=0, column=1)


author_text = StringVar()
input_text2 = Entry(window, textvariable=author_text)
input_text2.grid(row=0, column=3)


year_text = StringVar()
input_text3 = Entry(window, textvariable=year_text)
input_text3.grid(row=1, column=1)


isbn_text = StringVar()
input_text4 = Entry(window, textvariable=isbn_text)
input_text4.grid(row=1, column=3)


list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrol_bar = Scrollbar(window, orient="vertical")
scrol_bar.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scrol_bar.set)
scrol_bar.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)


button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search Book", width=12, command=search_command)
button2.grid(row=3, column=3)


button3 = Button(window, text="Add Book", width=12, command=add_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update Selected",
                 width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete Selected",
                 width=12, command=delete_command)

button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)


window.mainloop()
