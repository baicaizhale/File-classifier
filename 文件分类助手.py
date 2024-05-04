import os
import shutil
import tkinter as tk
from tkinter import filedialog

# 定义文件类型和对应的文件夹
file_types = {
    '.doc': '文档',
    '.docx': '文档',
    '.pdf': '文档',
    '.txt': '文档',
    '.xls': '电子表格',
    '.xlsx': '电子表格',
    '.ppt': '演示文稿',
    '.pptx': '演示文稿',
    '.jpg': '图片',
    '.png': '图片',
    '.gif': '图片',
    '.mp3': '音乐',
    '.wav': '音乐',
    '.mp4': '视频',
    '.avi': '视频',
    '.mov': '视频'
}

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("文件整理器")

        # 创建 GUI 元素
        self.source_label = tk.Label(master, text="源文件夹:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10)

        self.source_entry = tk.Entry(master)
        self.source_entry.grid(row=0, column=1, padx=10, pady=10)

        self.target_label = tk.Label(master, text="目标文件夹:")
        self.target_label.grid(row=1, column=0, padx=10, pady=10)

        self.target_entry = tk.Entry(master)
        self.target_entry.grid(row=1, column=1, padx=10, pady=10)

        self.browse_button = tk.Button(master, text="浏览", command=self.browse_folders)
        self.browse_button.grid(row=2, column=0, padx=10, pady=10)

        self.organize_button = tk.Button(master, text="整理文件", command=self.organize_files)
        self.organize_button.grid(row=2, column=1, padx=10, pady=10)

    def browse_folders(self):
        self.source_entry.delete(0, tk.END)
        self.target_entry.delete(0, tk.END)

        source_folder = filedialog.askdirectory()
        target_folder = filedialog.askdirectory()

        self.source_entry.insert(0, source_folder)
        self.target_entry.insert(0, target_folder)

    def organize_files(self):
        source_folder = self.source_entry.get()
        target_folder = self.target_entry.get()

        # 创建目标文件夹
        for folder in set(file_types.values()):
            folder_path = os.path.join(target_folder, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        # 遍历源文件夹中的文件
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            if os.path.isfile(file_path):
                # 获取文件扩展名
                _, ext = os.path.splitext(filename)
                ext = ext.lower()

                # 如果文件扩展名在文件类型字典中,则移动文件
                if ext in file_types:
                    target_subfolder = os.path.join(target_folder, file_types[ext])
                    target_path = os.path.join(target_subfolder, filename)
                    shutil.move(file_path, target_path)
                    print(f'已移动 {filename} 到 {file_types[ext]}')
                else:
                    print(f'跳过 {filename} (未知文件类型)')

root = tk.Tk()
app = FileOrganizerGUI(root)
root.mainloop()
