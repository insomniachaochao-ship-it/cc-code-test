#!/usr/bin/env python3
"""
GUI 计算器程序
使用 tkinter 构建
"""

import tkinter as tk
from tkinter import messagebox
import math

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("计算器")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        self.current_input = ""
        self.result = None
        self.new_input = True

        self.create_widgets()

    def create_widgets(self):
        # 显示区域
        self.display_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.display_frame.pack(fill=tk.X, padx=10, pady=10)

        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            self.display_frame,
            textvariable=self.display_var,
            font=("Arial", 32, "bold"),
            bg="#1a1a1a",
            fg="#ffffff",
            anchor="e",
            padx=20,
            pady=20
        )
        self.display.pack(fill=tk.X)

        # 表达式显示
        self.expression_var = tk.StringVar(value="")
        self.expression_label = tk.Label(
            self.display_frame,
            textvariable=self.expression_var,
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#888888",
            anchor="e",
            padx=20
        )
        self.expression_label.pack(fill=tk.X)

        # 按钮区域
        self.buttons_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 按钮布局
        buttons = [
            ("C", 0, 0, "#ff6b6b"), ("⌫", 0, 1, "#ffa502"), ("%", 0, 2, "#747d8c"), ("/", 0, 3, "#7bed9f"),
            ("7", 1, 0, "#4a4a4a"), ("8", 1, 1, "#4a4a4a"), ("9", 1, 2, "#4a4a4a"), ("*", 1, 3, "#7bed9f"),
            ("4", 2, 0, "#4a4a4a"), ("5", 2, 1, "#4a4a4a"), ("6", 2, 2, "#4a4a4a"), ("-", 2, 3, "#7bed9f"),
            ("1", 3, 0, "#4a4a4a"), ("2", 3, 1, "#4a4a4a"), ("3", 3, 2, "#4a4a4a"), ("+", 3, 3, "#7bed9f"),
            ("±", 4, 0, "#4a4a4a"), ("0", 4, 1, "#4a4a4a"), (".", 4, 2, "#4a4a4a"), ("=", 4, 3, "#2ed573"),
            ("√", 5, 0, "#70a1ff"), ("^", 5, 1, "#70a1ff"), ("(", 5, 2, "#70a1ff"), (")", 5, 3, "#70a1ff"),
        ]

        for (text, row, col, color) in buttons:
            self.create_button(text, row, col, color)

    def create_button(self, text, row, col, color):
        btn = tk.Button(
            self.buttons_frame,
            text=text,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="#ffffff",
            activebackground="#555555",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            cursor="hand2"
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        btn.bind("<Button-1>", lambda e, t=text: self.on_button_click(t))

        self.buttons_frame.grid_columnconfigure(col, weight=1)
        self.buttons_frame.grid_rowconfigure(row, weight=1)

    def on_button_click(self, text):
        try:
            if text == "C":
                self.clear()
            elif text == "⌫":
                self.backspace()
            elif text == "=":
                self.calculate()
            elif text == "±":
                self.toggle_sign()
            elif text == "%":
                self.percentage()
            elif text == "√":
                self.square_root()
            elif text == "^":
                self.append_input("**")
            else:
                self.append_input(text)
        except Exception as e:
            self.display_var.set("错误")
            self.new_input = True

    def append_input(self, text):
        if self.new_input and text in "0123456789":
            self.current_input = text
            self.new_input = False
        else:
            self.current_input += text
            self.new_input = False
        self.display_var.set(self.current_input)

    def clear(self):
        self.current_input = ""
        self.display_var.set("0")
        self.expression_var.set("")
        self.new_input = True

    def backspace(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.display_var.set(self.current_input if self.current_input else "0")

    def toggle_sign(self):
        if self.current_input:
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.display_var.set(self.current_input)

    def percentage(self):
        try:
            result = float(self.current_input) / 100
            self.current_input = str(result)
            self.display_var.set(self.current_input)
        except:
            pass

    def square_root(self):
        try:
            result = math.sqrt(float(self.current_input))
            self.expression_var.set(f"√({self.current_input})")
            self.current_input = str(result)
            self.display_var.set(self.current_input)
            self.new_input = True
        except:
            self.display_var.set("错误")
            self.new_input = True

    def calculate(self):
        try:
            expression = self.current_input
            # 安全计算
            result = eval(expression, {"__builtins__": None, "math": math})
            self.expression_var.set(f"{expression} =")
            self.current_input = str(result)
            self.display_var.set(self.current_input)
            self.new_input = True
        except ZeroDivisionError:
            self.display_var.set("不能除以零")
            self.new_input = True
        except Exception as e:
            self.display_var.set("错误")
            self.new_input = True

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
