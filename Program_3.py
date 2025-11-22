##
# Program 3: Long-Distance Calls
# Grant Dresser
# November 11/21/2025
##

import tkinter
import tkinter.messagebox


class LongDistance_Call:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Long-Distance Call Charges")

        # Rates
        self.DAY_RATE = 0.02      # 6:00 A.M. – 5:59 P.M.
        self.EVENING_RATE = 0.12  # 6:00 P.M. – 11:59 P.M.
        self.OFF_PEAK_RATE = 0.05 # midnight – 5:59 A.M.

        # Frames
        self.rate_frame = tkinter.Frame(self.main_window)
        self.minutes_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Radio buttons for rate category
        self.rate_var = tkinter.IntVar()
        self.rate_var.set(1)  # default Daytime

        self.day_rb = tkinter.Radiobutton(
            self.rate_frame,
            text=f"Daytime (6:00 A.M. - 5:59 P.M.) @ ${self.DAY_RATE:.2f}/min",
            variable=self.rate_var,
            value=1
        )
        self.evening_rb = tkinter.Radiobutton(
            self.rate_frame,
            text=f"Evening (6:00 P.M. - 11:59 P.M.) @ ${self.EVENING_RATE:.2f}/min",
            variable=self.rate_var,
            value=2
        )
        self.offpeak_rb = tkinter.Radiobutton(
            self.rate_frame,
            text=f"Off-Peak (Midnight - 5:59 A.M.) @ ${self.OFF_PEAK_RATE:.2f}/min",
            variable=self.rate_var,
            value=3
        )

        self.day_rb.pack(anchor="w")
        self.evening_rb.pack(anchor="w")
        self.offpeak_rb.pack(anchor="w")

        # Minutes entry
        self.minutes_label = tkinter.Label(self.minutes_frame, text="Minutes of call:")
        self.minutes_entry = tkinter.Entry(self.minutes_frame, width=10)

        self.minutes_label.pack(side="left")
        self.minutes_entry.pack(side="left")

        # Buttons
        self.calc_button = tkinter.Button(
            self.button_frame,
            text="Calculate Charge",
            command=self.calculate_charge
        )
        self.quit_button = tkinter.Button(
            self.button_frame,
            text="Quit",
            command=self.main_window.destroy
        )

        self.calc_button.pack(side="left", padx=5)
        self.quit_button.pack(side="left", padx=5)

        # Pack frames
        self.rate_frame.pack(padx=10, pady=5)
        self.minutes_frame.pack(padx=10, pady=5)
        self.button_frame.pack(padx=10, pady=5)

        tkinter.mainloop()

    def calculate_charge(self):
        try:
            minutes = float(self.minutes_entry.get())
            if minutes < 0:
                raise ValueError("Minutes must be >= 0")

            # Pick rate based on radio button
            if self.rate_var.get() == 1:
                rate = self.DAY_RATE
            elif self.rate_var.get() == 2:
                rate = self.EVENING_RATE
            else:
                rate = self.OFF_PEAK_RATE

            charge = minutes * rate

            tkinter.messagebox.showinfo(
                "Call Charge",
                f"Total charge for the call: ${charge:.2f}"
            )
        except ValueError:
            tkinter.messagebox.showerror(
                "Input Error",
                "Please enter a valid number of minutes (0 or more)."
            )


if __name__ == "__main__":
    call_gui = LongDistance_Call()
