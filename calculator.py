#!/usr/bin/env python3
"""
简单计算器程序
支持基本四则运算和科学计算
"""

import math
import re

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        """加法"""
        return a + b

    def subtract(self, a, b):
        """减法"""
        return a - b

    def multiply(self, a, b):
        """乘法"""
        return a * b

    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

    def power(self, a, b):
        """幂运算"""
        return a ** b

    def square_root(self, a):
        """平方根"""
        if a < 0:
            raise ValueError("不能对负数开平方")
        return math.sqrt(a)

    def factorial(self, n):
        """阶乘"""
        if n < 0:
            raise ValueError("负数没有阶乘")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def sin(self, x):
        """正弦（弧度）"""
        return math.sin(x)

    def cos(self, x):
        """余弦（弧度）"""
        return math.cos(x)

    def tan(self, x):
        """正切（弧度）"""
        return math.tan(x)

    def log(self, x, base=10):
        """对数"""
        if x <= 0:
            raise ValueError("对数真数必须大于零")
        return math.log(x, base)

    def ln(self, x):
        """自然对数"""
        if x <= 0:
            raise ValueError("对数真数必须大于零")
        return math.log(x)

    def evaluate_expression(self, expression):
        """计算数学表达式"""
        try:
            # 替换数学函数
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            expression = expression.replace('pi', str(math.pi))
            expression = expression.replace('e', str(math.e))

            # 安全计算
            result = eval(expression, {"__builtins__": None, "math": math})
            return result
        except Exception as e:
            raise ValueError(f"表达式错误: {e}")

    def save_to_history(self, expression, result):
        """保存到历史记录"""
        self.history.append(f"{expression} = {result}")

    def show_history(self):
        """显示历史记录"""
        if not self.history:
            print("暂无历史记录")
        else:
            print("\n=== 计算历史 ===")
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")
            print("================\n")

    def clear_history(self):
        """清空历史记录"""
        self.history = []
        print("历史记录已清空")


def print_help():
    """打印帮助信息"""
    print("""
╔══════════════════════════════════════════╗
║           计算器使用说明                  ║
╠══════════════════════════════════════════╣
║ 基本运算:                                 ║
║   + : 加法    - : 减法                    ║
║   * : 乘法    / : 除法                    ║
║   ^ : 幂运算  % : 取模                    ║
║                                           ║
║ 科学计算:                                 ║
║   sqrt(x) : 平方根                        ║
║   sin(x), cos(x), tan(x) : 三角函数       ║
║   log(x) : 以10为底的对数                 ║
║   ln(x)  : 自然对数                       ║
║   n!     : 阶乘                           ║
║   pi     : 圆周率                         ║
║   e      : 自然常数                       ║
║                                           ║
║ 命令:                                     ║
║   history  : 查看历史记录                 ║
║   clear    : 清空历史记录                 ║
║   help     : 显示帮助                     ║
║   quit/exit: 退出程序                     ║
╚══════════════════════════════════════════╝
""")


def main():
    """主函数"""
    calc = Calculator()

    print("\n🔢 欢迎使用计算器!")
    print("输入 'help' 查看使用说明，输入 'quit' 退出\n")

    while True:
        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            # 处理命令
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("再见! 👋")
                break
            elif user_input.lower() == 'help':
                print_help()
                continue
            elif user_input.lower() == 'history':
                calc.show_history()
                continue
            elif user_input.lower() == 'clear':
                calc.clear_history()
                continue

            # 计算阶乘
            if user_input.endswith('!'):
                try:
                    n = int(user_input[:-1])
                    result = calc.factorial(n)
                    print(f"= {result}")
                    calc.save_to_history(user_input, result)
                except ValueError as e:
                    print(f"错误: {e}")
                continue

            # 计算表达式
            result = calc.evaluate_expression(user_input)
            print(f"= {result}")
            calc.save_to_history(user_input, result)

        except ValueError as e:
            print(f"错误: {e}")
        except KeyboardInterrupt:
            print("\n\n再见! 👋")
            break
        except Exception as e:
            print(f"未知错误: {e}")


if __name__ == "__main__":
    main()
