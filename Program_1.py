##
# Program 1: MPG Calculator
# Grant Dresser
# November 11/21/2025
##

import tkinter
import tkinter.messagebox

class MPG_Calculator:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        self.gallons_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.gallons_label = tkinter.Label(self.gallons_frame, text="Gallons of gas:")
        self.gallons_entry = tkinter.Entry(self.gallons_frame, width=10)

        self.gallons_label.pack(side="left")
        self.gallons_entry.pack(side="left")

        self.miles_label = tkinter.Label(self.miles_frame, text="Miles on full tank:")
        self.miles_entry = tkinter.Entry(self.miles_frame, width=10)

        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")

        self.calc_button = tkinter.Button(
            self.button_frame, 
            text="Calculate MPG",
            command=self.calculate_mpg
        )
        self.quit_button = tkinter.Button(
            self.button_frame,
            text="Quit",
            command=self.main_window.destroy
        )

        self.calc_button.pack(side="left", padx=5)
        self.quit_button.pack(side="left", padx=5)

        self.gallons_frame.pack(pady=5)
        self.miles_frame.pack(pady=5)
        self.button_frame.pack(pady=5)

        tkinter.mainloop()

    def calculate_mpg(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())

            if gallons <= 0:
                raise ValueError("Gallons must be higher than 0")
            mpg = miles / gallons

            tkinter.messagebox.showinfo(
                "MPG Result",
                f"Miles per gallon: {mpg:.2f}"
            )
        except ValueError:
            tkinter.messagebox.showerror(
                "Input Error",
                "Please enter valid numeric values (gallons > 0)."
            )

if __name__ == "__main__":
    mpg = MPG_Calculator()