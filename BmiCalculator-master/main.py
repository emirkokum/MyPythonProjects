from tkinter import *

window = Tk()
window.title("Bmi Calculator")
window.minsize(width=450, height=300)
window.config(padx=15, pady=15)

weight_label = Label(text="Enter Your Weight(kg)")
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

height_label = Label(text="Enter Your Height(cm)")
height_label.pack()

height_entry = Entry()
height_entry.pack()

def calculateBmi():
    bw = weight_entry.get()
    height = height_entry.get()

    if bw == "" or height == "":
        result_label.config(text="Please enter both weight and height!")
    else:
        try:
            bmi = float(bw) / (float(height) / 100) ** 2
            result = round(bmi,2)
            if result <= 18.4:
                result_label.config(text=f"Your bmi is {result}\nYou are Underweight")
                print(f"Your bmi is {result}\nYou are Underweight")
            elif 18.5 <= result <= 24.9:
                result_label.config(text=f"Your bmi is {result}\nYou are Normal")
                print(f"Your bmi is {result}\nYou are Normal")
            elif 25 <= result <= 39.9:
                result_label.config(text=f"Your bmi is {result}\nYou are Overweight")
                print(f"Your bmi is {result}\nYou are Overweight")
            elif result >= 40:
                result_label.config(text=f"Your bmi is {result}\nYou are Obese")
                print(f"Your bmi is {result}\nYou are Obese")
        except:
            result_label.config(text="Enter a valid number")





send_button = Button(text="Calculate", padx=5, pady=5, command=calculateBmi)
send_button.place(x=175, y=100)

result_label = Label()
result_label.place(x=160, y=150)



window.mainloop()