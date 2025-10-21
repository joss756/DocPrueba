import tkinter as tk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")
        self.root.geometry("300x400")  # Tamaño de la ventana
        self.calc = Calculator()
        self.expression = ""  # Almacena la expresión actual

        # Display (etiqueta para mostrar la expresión y resultado)
        self.display = tk.Label(root, text="", font=("Arial", 20), bg="lightgray", anchor="e", padx=10, pady=10)
        self.display.pack(fill=tk.X, padx=10, pady=10)

        # Marco para los botones
        button_frame = tk.Frame(root)
        button_frame.pack()

        # Botones: números y operaciones
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)  # Limpiar en la fila inferior
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Arial", 18), width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.config(text="")
        elif char == '=':
            try:
                result = self.calc.chained_operation(self.expression)
                self.display.config(text=str(result))
                self.expression = str(result)  # Permite continuar con el resultado
            except Exception as e:
                self.display.config(text="Error")
                self.expression = ""
        else:
            self.expression += char
            self.display.config(text=self.expression)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()