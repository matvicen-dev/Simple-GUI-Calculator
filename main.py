import tkinter as tk

calculation = ""

def addToCalculation(symbol):
	global calculation
	calculation += str(symbol)
	textResult.delete(1.0, "end")
	textResult.insert(1.0, calculation)

def evaluateCalculation():
	global calculation
	try:
		calculation = str(eval(calculation))
		textResult.delete(1.0, "end")
		textResult.insert(1.0, calculation)
	except:
		clearField()
		textResult.insert(1.0, "Error")

def clearField():
	global calculation
	calculation = ""
	textResult.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")
textResult = tk.Text(root, height=2, width=16, font=("Arial", 24))
textResult.grid(columnspan=5)

button_1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), width=5, font=("Arial", 14))
button_1.grid(row=2, column=1)

button_2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), width=5, font=("Arial", 14))
button_2.grid(row=2, column=2)

button_3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), width=5, font=("Arial", 14))
button_3.grid(row=2, column=3)

button_4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), width=5, font=("Arial", 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), width=5, font=("Arial", 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), width=5, font=("Arial", 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), width=5, font=("Arial", 14))
button_7.grid(row=4, column=1)

button_8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), width=5, font=("Arial", 14))
button_8.grid(row=4, column=2)

button_9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), width=5, font=("Arial", 14))
button_9.grid(row=4, column=3)

button_0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), width=5, font=("Arial", 14))
button_0.grid(row=5, column=2)

button_plus = tk.Button(root, text="+", command=lambda: addToCalculation("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)

button_minus = tk.Button(root, text="-", command=lambda: addToCalculation("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)

button_multiplication = tk.Button(root, text="*", command=lambda: addToCalculation("*"), width=5, font=("Arial", 14))
button_multiplication.grid(row=4, column=4)

button_division = tk.Button(root, text="/", command=lambda: addToCalculation("/"), width=5, font=("Arial", 14))
button_division.grid(row=5, column=4)
