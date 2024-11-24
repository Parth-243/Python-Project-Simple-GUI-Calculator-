import tkinter as tk
from tkinter import ttk
from ..utils.constants import BUTTON_LAYOUT, COLORS
from .styles import apply_styles

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Configure dark theme for the root window
        self.root.configure(bg=COLORS['BACKGROUND'])
        
        # Apply styles
        self.style = apply_styles()
        
        # Variable to store current expression
        self.expression = ""
        
        # Create UI elements
        self._create_display()
        self._create_buttons()
        self._configure_grid()
    
    def _create_display(self):
        """Create the calculator display"""
        # Frame for display
        display_frame = tk.Frame(
            self.root,
            bg=COLORS['BACKGROUND'],
            pady=10
        )
        display_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        self.entry = tk.Entry(
            display_frame,
            width=25,
            font=('Arial', 16, 'bold'),  # Made font bold
            justify='right',
            bd=0,
            bg=COLORS['DISPLAY_BG'],
            fg=COLORS['TEXT'],
            insertbackground=COLORS['TEXT']
        )
        self.entry.pack(padx=10, pady=5, ipady=8)
        
        # Add border effect
        border_frame = tk.Frame(
            display_frame,
            bg=COLORS['BORDER'],
            height=2
        )
        border_frame.pack(fill='x', padx=10, pady=(0, 5))
    
    def _create_buttons(self):
        """Create and place all calculator buttons"""
        button_frame = tk.Frame(self.root, bg=COLORS['BACKGROUND'])
        button_frame.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)
        
        for button in BUTTON_LAYOUT:
            if len(button) == 4:  # Buttons that span multiple columns
                text, row, col, colspan = button
                btn = self._create_styled_button(button_frame, text)
                btn.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=2, pady=2)
            else:  # Regular buttons
                text, row, col = button
                btn = self._create_styled_button(button_frame, text)
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
    
    def _create_styled_button(self, parent, text):
        """Create a styled button based on its type"""
        if text == '=':
            style = 'Equals.TButton'
        elif text in ['+', '-', '*', '/', 'C', '←']:
            style = 'Operation.TButton'
        else:
            style = 'Number.TButton'
            
        btn = ttk.Button(
            parent,
            text=text,
            style=style
        )
        
        # Bind button clicks
        if text == '=':
            btn.config(command=self.calculate)
        elif text == 'C':
            btn.config(command=self.clear)
        elif text == '←':
            btn.config(command=self.backspace)
        else:
            btn.config(command=lambda t=text: self.add_to_expression(t))
            
        return btn
    
    def _configure_grid(self):
        """Configure grid weights for responsive layout"""
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def add_to_expression(self, value):
        """Add the pressed button value to the expression"""
        self.expression += str(value)
        self.update_display()
    
    def calculate(self):
        """Calculate the result of the expression"""
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except:
            self.expression = "Error"
        finally:
            self.update_display()
    
    def clear(self):
        """Clear the display"""
        self.expression = ""
        self.update_display()
    
    def backspace(self):
        """Remove the last character"""
        self.expression = self.expression[:-1]
        self.update_display()
    
    def update_display(self):
        """Update the entry field with current expression"""
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)