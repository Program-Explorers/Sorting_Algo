# Sort a list of numbers with python
import tkinter as tk


def f(nums):
    num_split = nums.split()
    n = len(num_split)

    for i in range(n):
        if not num_split[i].isdigit():
            output['text'] = 'Numbers only'
        break

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if float(num_split[j]) > float(num_split[j + 1]):
                num_split[j], num_split[j + 1] = float(num_split[j + 1]), float(num_split[j])
                already_sorted = False

        if already_sorted:
            break

    for i in range(n):
        try:
            int_num = int(num_split[i])
            if num_split[i] == int_num:
                num_split[i] = int_num

        except ValueError:
            output['text'] = 'Numbers only'
            break

        else:
            output['text'] = num_split


root = tk.Tk()

height = 250
width = 350

root.title("Sort Numbers")

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='numbers.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#2E9AFE')
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.55)

creator = tk.Label(
    root,
    font=('Futura', 15),
    text="Made by Program Explorers",
    foreground="#6E6E6E",  # Set the text color to white
    background="#5D8AC5"  # Set the background color to black
)
creator.place(relx=0, rely=0.92, relwidth=0.6, relheight=0.06)

number_label = tk.Label(frame, text='Type the numbers below')
number_label.place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.13)

numbers = tk.Entry(frame, bg='#BDBDBD')
numbers.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.2)

button = tk.Button(frame, text='SORT', bg='#E6E6E6', command=lambda: f(numbers.get()))
button.place(relx=0.34, rely=0.6, relwidth=0.3, relheight=0.2)

lower_frame = tk.Frame(root, bg='#2E9AFE')
lower_frame.place(relx=0.13, rely=0.65, relwidth=0.75, relheight=0.15)

output = tk.Label(lower_frame)
output.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.8)

root.mainloop()
