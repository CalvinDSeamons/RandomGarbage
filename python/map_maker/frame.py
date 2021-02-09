import tkinter as tk
import random
import argparse

def main():
    base_width=800
    base_height=400

    base_frame = tk.Tk()

    #base_frame.sizemins(base_width,base_height)

    label = tk.Label(
        text="Stupid Ugly Map Maker 0.0.1",
        fg="red",
        bg="black",
        width=base_width,
        height=20
    )

    button = tk.Button(
        text="Click me!",
        width=base_width,
        height=5,
        bg="gray",
        fg="black",
    )
    label.pack()
    #button.pack()

    base_frame.mainloop()
main()

