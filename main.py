from tkinter import *

window = Tk()
window.title("Disappearing text")
window.config(padx=50, pady=50)

text_box = Text(window)
text_box.pack()
list_of_afters = []

def start_countdown():
    def delete_text():
        text_box.delete("1.0", "end")
    dt = window.after(5000, delete_text)
    list_of_afters.append(dt)

def stop_countdown(key):
    if list_of_afters == []:
        start_countdown()
    for after in list_of_afters:
        window.after_cancel(after)
        list_of_afters.remove(after)
    start_countdown()

text_box.bind("<Key>", stop_countdown)
window.mainloop()