import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os


def convert_encoding(input_file_path, output_file_path):
    try:
        df = pd.read_csv(input_file_path, encoding='shift_jis')
        df.to_csv(output_file_path, encoding='utf-8', index=False)
        return True
    except Exception as e:
        print(e)
        return False

def on_convert_button_click():
    # 入力ファイルの選択
    input_file_path = filedialog.askopenfilename(title="Shift-JISのCSVファイルを選択", filetypes=[("CSV Files", "*.csv")])
    if not input_file_path:  # ファイルが選択されなかった場合
        return

    # 出力ファイルの名前を生成
    basename = os.path.basename(input_file_path)  # ファイル名の取得 (e.g., "sample.csv")
    name_without_extension = os.path.splitext(basename)[0]  # 拡張子を除いたファイル名 (e.g., "sample")
    new_name = f"[変換済] {name_without_extension}.csv"  # 新しいファイル名 (e.g., "sample (変換済み).csv")
    output_file_path = os.path.join(os.path.dirname(input_file_path), new_name)  # 新しいファイルのフルパスを生成

    # エンコード変換の実行
    if convert_encoding(input_file_path, output_file_path):
        messagebox.showinfo("成功", "エンコード変換が成功しました！")
    else:
        messagebox.showerror("エラー", "エンコード変換に失敗しました。")


root = tk.Tk()
root.title("エンコード変換ツール")
root.geometry('300x150')

label = tk.Label(root, text="Shift-JISのCSVファイルをUTF-8に変換")
label.pack(pady=20)

convert_button = tk.Button(root, text="ファイルを選択して変換", command=on_convert_button_click)
convert_button.pack(pady=20)

root.mainloop()
