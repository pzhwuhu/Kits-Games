import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

response_index = 0

def on_closing():
    messagebox.showinfo("嘻嘻", "小姐姐，不同意是关闭不了的哦")

def on_yes():
    messagebox.showinfo("😘", "爱你！么么哒")
    root.destroy()

def on_no():
    global response_index  # 使用全局变量
    responses = ["保大", "家务活我干", "工资全给你", "包包随便买", "只爱你一个"]
    
    # 获取当前响应
    response = responses[response_index]
    messagebox.showinfo("回应", response)
    
    # 更新索引，循环到下一个响应 
    response_index = (response_index + 1) % len(responses)     
 
# 创建主窗口
root = tk.Tk()
root.title("爱慕你的小哥哥")

# 设置窗口大小
root.geometry("500x280")  # 设置默认窗口大小

# 设置背景颜色
root.configure(bg="#FFE4E1")  # 使用浅粉色作为背景颜色

# 使用 grid 布局管理器
root.grid_columnconfigure(0, weight=4)  # 左边文字和按钮区域（80%）
root.grid_columnconfigure(1, weight=1)  # 右边图片区域（20%）

# 添加文字标签
label1 = tk.Label(root, text="小姐姐，我观察你很久了~", bg="#FFE4E1", font=("微软雅黑", 16)) 
label1.grid(row=0, column=0, sticky="n", pady=(30, 10), padx=(8,0))  # 文字居中

label2 = tk.Label(root, text="做我女朋友好不好？", bg="#FFE4E1", font=("仿宋", 24, "bold"))
label2.grid(row=1, column=0, sticky="n", pady=(10, 20), padx=(8,0))  # 文字居中

# 添加按钮
button_frame = tk.Frame(root, bg="#FFE4E1")
button_frame.grid(row=2, column=0, sticky="n", pady=(30, 20))  # 按钮居中

yes_button = tk.Button(button_frame, text="好~", command=on_yes, bg="#2ad2f1", fg="white",font = ("微软雅黑",18))
yes_button.pack(side=tk.LEFT, padx=20)

no_button = tk.Button(button_frame, text="不好~", command=on_no, bg="#2ad2f1", fg="white", font = ("微软雅黑",18))
no_button.pack(side=tk.LEFT, padx=20)

# 加载并显示图片
try:
    image1 = Image.open("D:/Projects/myTools/fun/你的名字4.jpg")  # 替换为你的第一张图片路径
    image1 = image1.resize((130, 100), Image.Resampling.LANCZOS)  # 调整图片大小
    photo1 = ImageTk.PhotoImage(image1)
    image_label1 = tk.Label(root, image=photo1, bg="#FFE4E1")
    image_label1.grid(row=0, column=1, rowspan=2, sticky="n", pady=(20, 10))  # 图片居中

    image2 = Image.open("D:/Projects/myTools/fun/魔女宅急便2.jpg")  # 替换为你的第二张图片路径
    image2 = image2.resize((130, 100), Image.Resampling.LANCZOS)  # 调整图片大小
    photo2 = ImageTk.PhotoImage(image2)
    image_label2 = tk.Label(root, image=photo2, bg="#FFE4E1")
    image_label2.grid(row=2, column=1, sticky="n", pady=(10, 20))  # 图片居中
except Exception as e:
    print("图片加载失败:", e)

# 处理窗口关闭事件
root.protocol("WM_DELETE_WINDOW", on_closing)

# 运行主循环
root.mainloop()