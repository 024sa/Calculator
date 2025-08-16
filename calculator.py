class Calculator:
	def add(self, a, b):
		return a + b

	def subtract(self, a, b):
		return a - b 

	def multiply(self, a, b):
		return a * b

	def divide(self, a, b):
		if b == 0:
			raise ValueError("Cannot divide by zero.")
		return a / b

	def power(self, a, b):
		return a ** b

	def modulus(self, a, b):
		return a % b

	def sqrt(self, a):
		if a < 0:
			raise ValueError("Cannot take square root of negative number.")
		return a ** 0.5


def main():
	calc = Calculator()
	print("""
========================================
	★★  COOL CALCULATOR  ★★
	By Sam Zack
	Instagram: https://www.instagram.com/Sam_zack001
========================================
"")
	print("Select operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. Power (x^y)")
	print("6. Modulus (x % y)")
	print("7. Square Root (√x)")

	while True:
		choice = input("Enter choice (1/2/3/4/5/6/7 or q to quit): ")
		if choice.lower() == 'q':
			print("Exiting calculator.")
			break
		if choice not in ['1', '2', '3', '4', '5', '6', '7']:
			print("Invalid input. Please try again.")
			continue
		try:
			if choice == '7':
				num1 = float(input("Enter number: "))
				result = calc.sqrt(num1)
				print(f"√{num1} = {result}")
			else:
				num1 = float(input("Enter first number: "))
				num2 = float(input("Enter second number: "))
				if choice == '1':
					result = calc.add(num1, num2)
					op = '+'
				elif choice == '2':
					result = calc.subtract(num1, num2)
					op = '-'
				elif choice == '3':
					result = calc.multiply(num1, num2)
					op = '*'
				elif choice == '4':
					result = calc.divide(num1, num2)
					op = '/'
				elif choice == '5':
					result = calc.power(num1, num2)
					op = '^'
				elif choice == '6':
					result = calc.modulus(num1, num2)
					op = '%'
				print(f"{num1} {op} {num2} = {result}")
			except Exception as e:
				print(f"Error: {e}")

# GUI Implementation
import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
	def __init__(self, master):
		self.master = master
		master.title("Cool Calculator by Sam Zack")
		self.calc = Calculator()
		# Stylish heading with Instagram link
		heading = tk.Label(master, text="★★ COOL CALCULATOR ★★", fg="#6C63FF", bg="#F3F3F3", font=("Arial Black", 18, "bold"))
		heading.grid(row=0, column=0, columnspan=4, pady=(10,0))
		subheading = tk.Label(master, text="By Sam Zack", fg="#333", bg="#F3F3F3", font=("Arial", 12, "italic"))
		subheading.grid(row=1, column=0, columnspan=4)
		link = tk.Label(master, text="Instagram: @Sam_zack001", fg="#405DE6", bg="#F3F3F3", cursor="hand2", font=("Arial", 11, "underline"))
		link.grid(row=2, column=0, columnspan=4, pady=(0,10))
		link.bind("<Button-1>", lambda e: self.open_link())
		master.configure(bg="#F3F3F3")
		self.entry = tk.Entry(master, width=30, borderwidth=5, font=("Arial", 16))
		self.entry.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
		self.create_buttons()
		self.current = ""
		self.operator = None
		self.first_num = None

	def open_link(self):
		import webbrowser
		webbrowser.open_new("https://www.instagram.com/Sam_zack001")

	def create_buttons(self):
		buttons = [
			('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
			('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
			('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
			('0', 7, 0), ('.', 7, 1), ('%', 7, 2), ('+', 7, 3),
			('C', 8, 0), ('^', 8, 1), ('√', 8, 2), ('=', 8, 3)
		]
		for (text, row, col) in buttons:
			tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 14),
				bg="#E4E8FF", fg="#222", activebackground="#B2B7FF",
				command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=2, pady=2)

	def on_button_click(self, char):
		if char in '0123456789.':
			self.entry.insert(tk.END, char)
		elif char in '+-*/%^':
			self.first_num = self.get_entry_value()
			self.operator = char
			self.entry.delete(0, tk.END)
		elif char == '√':
			try:
				num = self.get_entry_value()
				result = self.calc.sqrt(num)
				self.entry.delete(0, tk.END)
				self.entry.insert(0, str(result))
			except Exception as e:
				messagebox.showerror("Error", str(e))
		elif char == 'C':
			self.entry.delete(0, tk.END)
			self.first_num = None
			self.operator = None
		elif char == '=':
			try:
				second_num = self.get_entry_value()
				result = None
				if self.operator == '+':
					result = self.calc.add(self.first_num, second_num)
				elif self.operator == '-':
					result = self.calc.subtract(self.first_num, second_num)
				elif self.operator == '*':
					result = self.calc.multiply(self.first_num, second_num)
				elif self.operator == '/':
					result = self.calc.divide(self.first_num, second_num)
				elif self.operator == '^':
					result = self.calc.power(self.first_num, second_num)
				elif self.operator == '%':
					result = self.calc.modulus(self.first_num, second_num)
				self.entry.delete(0, tk.END)
				self.entry.insert(0, str(result))
				self.first_num = None
				self.operator = None
			except Exception as e:
				messagebox.showerror("Error", str(e))

	def get_entry_value(self):
		try:
			return float(self.entry.get())
		except ValueError:
			raise ValueError("Invalid input")

def run_gui():
	root = tk.Tk()
	gui = CalculatorGUI(root)
	root.mainloop()

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1 and sys.argv[1] == '--gui':
		run_gui()
	else:
		main()