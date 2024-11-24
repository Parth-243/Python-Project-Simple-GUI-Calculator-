from tkinter import ttk

def apply_styles():
    """Apply dark theme styles to calculator widgets"""
    style = ttk.Style()
    
    # Common button settings
    common_settings = {
        'font': ('Arial', 12, 'bold'),  # Made font bold
        'width': 5,
        'padding': 10,
        'relief': 'flat',
        'borderwidth': 0,
    }
    
    # Configure default style
    style.configure('TButton', **common_settings)
    
    # Number buttons (very dark gray)
    style.configure(
        "Number.TButton",
        **common_settings,
        background='#1A1A1A',  # Darker background
        foreground='#262525'   # White text
    )
    
    # Operation buttons (slightly lighter than numbers)
    style.configure(
        "Operation.TButton",
        **common_settings,
        background='#202020',   # Dark gray
        foreground='#FF9500'    # Orange color for operators
    )
    
    # Equals button (accent color)
    style.configure(
        "Equals.TButton",
        **common_settings,
        background='#1A1A1A',   # Dark background
        foreground='#00FF00'    # Green text
    )
    
    # Configure hover effects
    style.map('Number.TButton',
        background=[('pressed', '#000000'), ('active', '#333333')],
        foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')]
    )
    
    style.map('Operation.TButton',
        background=[('pressed', '#000000'), ('active', '#333333')],
        foreground=[('pressed', '#FFA500'), ('active', '#FFA500')]
    )
    
    style.map('Equals.TButton',
        background=[('pressed', '#000000'), ('active', '#333333')],
        foreground=[('pressed', '#00FF00'), ('active', '#00FF00')]
    )
    
    return style