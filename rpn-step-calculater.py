def evaluate_rpn():
    import math

    def calculate_rpn(expression):
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y,         # 乘方
            'root': lambda x, y: y ** (1 / x), # 开n次方
            'sin': lambda x: math.sin(math.radians(x)), # 正弦
            'cos': lambda x: math.cos(math.radians(x)), # 余弦
            'tan': lambda x: math.tan(math.radians(x)), # 正切
            'asin': lambda x: math.degrees(math.asin(x)), # 反正弦
            'acos': lambda x: math.degrees(math.acos(x)), # 反余弦
            'atan': lambda x: math.degrees(math.atan(x)), # 反正切
            'exp': lambda x: math.exp(x),   # 自然指数
            'log': lambda x: math.log10(x), # 常用对数
            'ln': lambda x: math.log(x),    # 自然对数
            'abs': lambda x: abs(x),        # 绝对值
            'floor': lambda x: math.floor(x), # 向下取整
            'ceil': lambda x: math.ceil(x),  # 向上取整
        }

        stack_operators = {
            'dup': lambda s: s.append(s[-1]) if s else None, # 复制栈顶
            'swap': lambda s: s.append(s.pop(-2)) if len(s) > 1 else None, # 交换栈顶两元素
            'drop': lambda s: s.pop() if s else None, # 丢弃栈顶
            'rot': lambda s: s.insert(0, s.pop()) if len(s) > 1 else None, # 旋转栈
        }

        print(f"\n解析表达式：{expression}")
        for token in expression.split():
            if token.isdigit() or token.replace('.', '', 1).isdigit():  # 是数字
                stack.append(float(token))
                print(f"压栈：{token}，当前栈状态：{stack}")
            elif token in operators:  # 是二元操作符
                if len(stack) < 2 and token not in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp', 'log', 'ln', 'abs', 'floor', 'ceil'):
                    print(f"错误：操作符 {token} 缺少操作数。")
                    return None
                if token in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'exp', 'log', 'ln', 'abs', 'floor', 'ceil'):  # 一元操作符
                    a = stack.pop()
                    print(f"弹出操作数：{a}，进行 {token} 运算")
                    result = operators[token](a)
                else:  # 二元操作符
                    b = stack.pop()
                    a = stack.pop()
                    print(f"弹出操作数：{a} 和 {b}，进行 {token} 运算")
                    result = operators[token](a, b)
                stack.append(result)
                print(f"结果 {result} 压栈，当前栈状态：{stack}")
            elif token in stack_operators:  # 栈操作符
                print(f"执行栈操作：{token}")
                stack_operators[token](stack)
                print(f"当前栈状态：{stack}")
            else:
                print(f"错误：无效的标记 {token}")
                return None

        if len(stack) == 1:
            print(f"计算完成，最终结果：{stack[0]}")
            return stack.pop()
        else:
            print("错误：表达式无效，栈中剩余多余的值。")
            return None

    while True:
        expression = input("\n请输入RPN表达式（输入 'exit' 退出）：")
        if expression.lower() == 'exit':
            print("自爆程序已启动，即将在3秒后爆炸！")
            break
        result = calculate_rpn(expression)
        if result is not None:
            print(f"最终结果：{result}")