import tkinter as tk
from tkinter import filedialog
import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return None

def get_user_input():
    window = tk.Tk()
    window.title('CSV 読み込みツール')
    window.geometry('600x200')

    name_label = tk.Label(window, text='変数名 ', font=('Helvetica', 20))
    name_label.pack(anchor='w')
    name_entry = tk.Entry(window, font=('Helvetica', 20))
    name_entry.insert(0, '入力してください')
    name_entry.pack(anchor='w')

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[('CSVファイル', '*.csv')])
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

    file_label = tk.Label(window, text='アンケート結果(CSV) ', font=('Helvetica', 20))
    file_label.pack(anchor='w')
    file_entry = tk.Entry(window, font=('Helvetica', 20))
    file_entry.insert(0, 'ファイルを選択してください')
    file_entry.pack(anchor='w')
    file_button = tk.Button(window, text='ファイル選択', command=browse_file)
    file_button.pack(anchor='w')

    def on_ok_click():
        file_path = file_entry.get()
        window.destroy()
        return read_csv(file_path)

    ok_button = tk.Button(window, text='OK', command=on_ok_click, font=('Helvetica', 16))
    ok_button.pack(side='left', padx=180, pady=60)
    cancel_button = tk.Button(window, text='キャンセル', command=window.destroy, font=('Helvetica', 16))
    cancel_button.pack(side='right', padx=60, pady=60)

    window.mainloop()
    return None

result = get_user_input()
print(result)
