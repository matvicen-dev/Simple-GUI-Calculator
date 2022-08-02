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