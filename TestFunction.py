import numpy as np
import pandas as pd
import os 
from openai import OpenAI

def Test_Func(test_arg):

    # 获取用户输入
    name = input("请输入你的名字: ")

    if test_arg:
        if name:
            print(f"你好，{name}！测试成功！")
        else:
            print("你没有输入名字，请重新运行脚本并输入你的名字。")

if __name__ == "__main__":
    test_arg = True
    Test_Func(test_arg)
