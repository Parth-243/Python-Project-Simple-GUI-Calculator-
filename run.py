import tkinter as tk
from src.calculator.calculator import Calculator

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()