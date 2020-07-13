# Sort a list of numbers with python
import tkinter as tk


def f(nums):
    num_split = nums.split()
    print(num_split)


root = tk.Tk()

height = 250
width = 350

root.title("Sort Numbers")

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

# background_image = tk.PhotoImage(file='land.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#2E9AFE')
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.55)

creator = tk.Label(
    root,
    font=('Futura', 15),
    text="Made by Program Explorers",
    foreground="#6E6E6E",  # Set the text color to white
    background="#04B431"  # Set the background color to black
)
creator.place(relx=0, rely=0.92, relwidth=0.6, relheight=0.06)

number_label = tk.Label(frame, text='Type the numbers below')
number_label.place(relx=0.23, rely=0.04, relwidth=0.5, relheight=0.13)

numbers = tk.Entry(frame, bg='#BDBDBD')
numbers.place(relx=0.18, rely=0.25, relwidth=0.6, relheight=0.2)

button = tk.Button(frame, text='SORT', bg='#E6E6E6', command=lambda: f(numbers.get()))
button.place(relx=0.32, rely=0.6, relwidth=0.3, relheight=0.2)

root.mainloop()
