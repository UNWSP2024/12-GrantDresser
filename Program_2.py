##
# Program 2: Joe's Automotive
# Grant Dresser
# November 11/21/2025
##

import tkinter


class Joes_Automotive:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")

        # Service prices
        self.OIL_CHANGE = 30.00
        self.LUBE_JOB = 20.00
        self.RADIATOR_FLUSH = 40.00
        self.TRANSMISSION_FLUID = 100.00
        self.INSPECTION = 35.00
        self.MUFFLER = 200.00
        self.TIRE_ROTATION = 20.00

        # IntVars for checkbuttons
        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.radiator_var = tkinter.IntVar()
        self.transmission_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_var = tkinter.IntVar()
        self.tire_var = tkinter.IntVar()

        # Frames
        self.services_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Checkbuttons
        self.oil_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Oil Change - ${self.OIL_CHANGE:.2f}",
            variable=self.oil_var
        )
        self.lube_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Lube Job - ${self.LUBE_JOB:.2f}",
            variable=self.lube_var
        )
        self.radiator_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Radiator Flush - ${self.RADIATOR_FLUSH:.2f}",
            variable=self.radiator_var
        )
        self.transmission_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Transmission Fluid - ${self.TRANSMISSION_FLUID:.2f}",
            variable=self.transmission_var
        )
        self.inspection_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Inspection - ${self.INSPECTION:.2f}",
            variable=self.inspection_var
        )
        self.muffler_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Muffler Replacement - ${self.MUFFLER:.2f}",
            variable=self.muffler_var
        )
        self.tire_cb = tkinter.Checkbutton(
            self.services_frame,
            text=f"Tire Rotation - ${self.TIRE_ROTATION:.2f}",
            variable=self.tire_var
        )

        # Pack checkbuttons
        self.oil_cb.pack(anchor="w")
        self.lube_cb.pack(anchor="w")
        self.radiator_cb.pack(anchor="w")
        self.transmission_cb.pack(anchor="w")
        self.inspection_cb.pack(anchor="w")
        self.muffler_cb.pack(anchor="w")
        self.tire_cb.pack(anchor="w")

        # Total label
        self.total_label_text = tkinter.Label(self.total_frame, text="Total Charges: ")
        self.total_var = tkinter.StringVar()
        self.total_var.set("$0.00")
        self.total_value_label = tkinter.Label(self.total_frame, textvariable=self.total_var)

        self.total_label_text.pack(side="left")
        self.total_value_label.pack(side="left")

        # Buttons
        self.calc_button = tkinter.Button(
            self.button_frame,
            text="Calculate Total",
            command=self.calculate_total
        )
        self.quit_button = tkinter.Button(
            self.button_frame,
            text="Quit",
            command=self.main_window.destroy
        )

        self.calc_button.pack(side="left", padx=5)
        self.quit_button.pack(side="left", padx=5)

        # Pack frames
        self.services_frame.pack(padx=10, pady=10)
        self.total_frame.pack(pady=5)
        self.button_frame.pack(pady=5)

        tkinter.mainloop()

    def calculate_total(self):
        total = 0.0

        if self.oil_var.get() == 1:
            total += self.OIL_CHANGE
        if self.lube_var.get() == 1:
            total += self.LUBE_JOB
        if self.radiator_var.get() == 1:
            total += self.RADIATOR_FLUSH
        if self.transmission_var.get() == 1:
            total += self.TRANSMISSION_FLUID
        if self.inspection_var.get() == 1:
            total += self.INSPECTION
        if self.muffler_var.get() == 1:
            total += self.MUFFLER
        if self.tire_var.get() == 1:
            total += self.TIRE_ROTATION

        self.total_var.set(f"${total:.2f}")


if __name__ == "__main__":
    joes_gui = Joes_Automotive()