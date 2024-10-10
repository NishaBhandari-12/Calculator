from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Set background color to black
        self.root.configure(bg='black')
        
        # Entry widget to display the result, with black background and white text
        self.e = Entry(root, width=35, borderwidth=5, bg="black", fg="white")
        self.e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Store the first number and the operation
        self.first_number = None
        self.math = None
        
        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        # Number buttons with black background and white text
        button_1 = Button(self.root, text="1", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(1))
        button_2 = Button(self.root, text="2", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(2))
        button_3 = Button(self.root, text="3", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(3))
        button_4 = Button(self.root, text="4", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(4))
        button_5 = Button(self.root, text="5", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(5))
        button_6 = Button(self.root, text="6", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(6))
        button_7 = Button(self.root, text="7", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(7))
        button_8 = Button(self.root, text="8", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(8))
        button_9 = Button(self.root, text="9", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(9))
        button_0 = Button(self.root, text="0", padx=40, pady=20, bg="black", fg="white", command=lambda: self.button_click(0))

        # Operation buttons
        button_add = Button(self.root, text="+", padx=39, pady=20, bg="black", fg="white", command=self.button_add)
        button_equal = Button(self.root, text="=", padx=91, pady=20, bg="black", fg="white", command=self.button_equal)
        button_clear = Button(self.root, text="Clear", padx=79, pady=20, bg="black", fg="white", command=self.button_clear)

        button_subtract = Button(self.root, text="-", padx=41, pady=20, bg="black", fg="white", command=self.button_subtract)
        button_multiply = Button(self.root, text="*", padx=40, pady=20, bg="black", fg="white", command=self.button_multiply)
        button_divide = Button(self.root, text="/", padx=41, pady=20, bg="black", fg="white", command=self.button_divide)

        # Put the buttons on the screen
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)

        button_0.grid(row=4, column=0)

        button_clear.grid(row=4, column=1, columnspan=2)
        button_add.grid(row=5, column=0)
        button_equal.grid(row=5, column=1, columnspan=2)

        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=6, column=1)
        button_divide.grid(row=6, column=2)

    # Button click function to display numbers
    def button_click(self, number):
        current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))

    # Clear the display
    def button_clear(self):
        self.e.delete(0, END)

    # Store the first number and the operation
    def button_add(self):
        self.first_number = float(self.e.get())
        self.math = "addition"
        self.e.delete(0, END)

    def button_subtract(self):
        self.first_number = float(self.e.get())
        self.math = "subtraction"
        self.e.delete(0, END)

    def button_multiply(self):
        self.first_number = float(self.e.get())
        self.math = "multiplication"
        self.e.delete(0, END)

    def button_divide(self):
        self.first_number = float(self.e.get())
        self.math = "division"
        self.e.delete(0, END)

    # Calculate the result
    def button_equal(self):
        second_number = float(self.e.get())
        self.e.delete(0, END)
        
        if self.math == "addition":
            self.e.insert(0, self.first_number + second_number)
        elif self.math == "subtraction":
            self.e.insert(0, self.first_number - second_number)
        elif self.math == "multiplication":
            self.e.insert(0, self.first_number * second_number)
        elif self.math == "division":
            if second_number != 0:
                self.e.insert(0, self.first_number / second_number)
            else:
                self.e.insert(0, "Error")  # Handle division by zero

# Create the main window and an instance of the Calculator class
root = Tk()
calculator = Calculator(root)

# Run the main loop
root.mainloop()
