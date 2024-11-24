# Simple GUI Calculator

A simple, user-friendly calculator application with a graphical user interface built using Python and tkinter.

## Features

- Clean and modern user interface
- Basic arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (\*)
  - Division (/)
- Additional functionality:
  - Decimal point support
  - Clear button (C)
  - Backspace button (←)
- Error handling for invalid expressions
- Responsive grid layout

## Prerequisites

- Python 3.6 or higher (Python comes with tkinter built-in)
- Windows, macOS, or Linux operating system

## Project Structure

```
calculator_app/
├── src/
│   ├── __init__.py
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── calculator.py    # Main calculator logic
│   │   └── styles.py        # UI styling configurations
│   └── utils/
│       ├── __init__.py
│       └── constants.py     # Button layout and configurations
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # Unit tests
└── run.py                   # Application entry point
```

## Installation

1. Clone the repository or download the source code:

```bash
git clone https://github.com/yourusername/calculator-app.git
# or download and extract the ZIP file
```

2. Navigate to the project directory:

```bash
cd calculator-app
```

## Running the Application

### Windows

```powershell
python run.py
```

### macOS/Linux

```bash
python3 run.py
```

## Usage Guide

1. Basic Operations:

   - Click number buttons (0-9) to input numbers
   - Click operation buttons (+, -, \*, /) for calculations
   - Press '=' to see the result
   - Use '.' for decimal numbers

2. Special Functions:

   - 'C' - Clears the entire display
   - '←' - Removes the last entered character

3. Error Handling:
   - Invalid expressions will display "Error"
   - Division by zero is handled gracefully

## Development Guide

### Adding New Features

1. Calculator Logic:

   - Modify `src/calculator/calculator.py` to add new calculation features
   - Add new button configurations in `src/utils/constants.py`

2. UI Modifications:
   - Update styles in `src/calculator/styles.py`
   - Modify grid layout in the Calculator class

### Running Tests

```bash
python -m unittest tests/test_calculator.py
```

## Troubleshooting

1. Import Errors:

   - Ensure all `__init__.py` files exist
   - Run the application from the project root directory

2. Tkinter Issues:

   - Python installation includes tkinter by default
   - For Linux users: Install python3-tk if needed:
     ```bash
     sudo apt-get install python3-tk  # Ubuntu/Debian
     sudo dnf install python3-tkinter # Fedora
     ```

3. Display Issues:
   - Check if the window size (300x400) works for your screen
   - Modify geometry in calculator.py if needed

## Contributing

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Submit a pull request

## Future Enhancements

- [ ] Scientific calculator functions
- [ ] Keyboard input support
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] History of calculations
- [ ] Theme customization
- [ ] Support for parentheses in expressions

## Acknowledgments

- Built with Python's tkinter library
- Inspired by standard calculator applications

## Contact

- Name: Parth Shrivastava
- Email: parthshrivastva24@gmail.com
- GitHub: [GitHub Profile](https://github.com/Parth-243)

## Version History

- 1.0.0 (Current)
  - Initial release
  - Basic arithmetic operations
  - Simple GUI interface
