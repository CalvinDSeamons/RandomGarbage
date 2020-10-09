from tkinter import Tk, Canvas, Frame, BOTH
import argparse

class basic_frame(Frame):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        #canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0")
        #canvas.create_rectangle(150, 10, 240, 80, outline="#f50", fill="#f50")
        #canvas.create_rectangle(270, 10, 370, 80, outline="#05f", fill="#05f")
        canvas.pack(fill=BOTH, expand=1)

def main():

    print("Welcome to mapmaker-0.0")
    root = Tk()
    test = basic_frame() 
    #buttonBG = root.canvas.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
    #buttonTXT = canvas.create_text(50, 15, text="click")
    #canvas.tag_bind(buttonBG, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
    #canvas.tag_bind(buttonTXT, "<Button-1>", clicked) ## same, but for the text.
    root.mainloop()


if __name__ == '__main__':
   main()


