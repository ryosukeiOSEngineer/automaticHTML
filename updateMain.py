import re
import csv
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk
from tkinter import filedialog, ttk




# これ以後のコードで、適切なファイルパスを`file_path`変数にセットして`read_csv`関数を呼び出して使用


# ------------GUI----------------

def browse_file():
    '''
    GUIでcsvファイルを選択して置換するためのデータを読み込む 
    '''
    file_path = filedialog.askopenfilename(filetypes=[('CSVファイル', '*.csv')])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)


def on_generate_button_click():
    file_path = file_entry.get()
    specific_word = word_entry.get()
    
    if not file_path or file_path == 'ファイルを選択してください':
        result_label.config(text="エラー: ファイルが選択されていません")
        return
    
    if not specific_word:
        result_label.config(text="エラー: 特定のワードが入力されていません")
        return

    with open('automatic.html', 'r', encoding='utf-8') as htmlfile:
        html_template = htmlfile.read()
    updated_content = html_template.replace('XXX', specific_word)
    
    # 置換したHTMLをテキストウィジェットに表示
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, updated_content)
    result_label.config(text="HTMLが生成されました")


def copy_to_clipboard():
    text_widget.tag_add(tk.SEL, "1.0", tk.END)
    selected_text = text_widget.get(tk.SEL_FIRST, tk.END)
    text_widget.clipboard_clear()
    text_widget.clipboard_append(selected_text)
    text_widget.tag_remove(tk.SEL, "1.0", tk.END)

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("CSV Selector")
root.geometry('600x400')

# グリッドで配置するフレーム
grid_frame = tk.Frame(root)
grid_frame.pack()

# 空のラベルを追加して高さ設定
empty_label = tk.Label(grid_frame, height=2)  
empty_label.grid(row=0, column=0, columnspan=3)

# 特定ワードの入力フィールド
word_label = tk.Label(grid_frame, text='特定ワードを入力: ')
word_label.grid(row=1, column=0)
word_entry = tk.Entry(grid_frame)
word_entry.insert(0, 'xxx')
word_entry.grid(row=1, column=1)

# ファイル選択エントリとボタン
file_label = tk.Label(grid_frame, text='アンケート結果(CSV) ')
file_label.grid(row=2, column=0)
file_entry = tk.Entry(grid_frame)
file_entry.insert(0, 'ファイルを選択してください')
file_entry.grid(row=2, column=1)
file_button = tk.Button(grid_frame, text='ファイル選択', command=browse_file)
file_button.grid(row=2, column=2)

# パックで配置するフレーム
pack_frame = tk.Frame(root)
pack_frame.pack()

# ボタンを配置（HTMLを生成して表示する）
button_frame = tk.Frame(pack_frame)  # 新しいフレームを作成してボタンをその中に配置
button_frame.pack()

generate_button = ttk.Button(button_frame, text="HTML生成 START", command=on_generate_button_click)

generate_button.pack(side=tk.LEFT, padx=15, pady=30)  # side=tk.LEFTで左側に配置

copy_button = ttk.Button(button_frame, text="HTML COPY", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=15, pady=30)  # side=tk.LEFTで左側に配置

# 結果を表示するラベル
result_label = tk.Label(root, text="")
result_label.pack()

# テキストウィジェットとスクロールバーの設置
text_widget = tk.Text(root, wrap=tk.NONE)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=text_widget.xview)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

text_widget.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

root.mainloop()


# csvファイルを読み込み
def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)  

# 特定のワードの置換
def replace_specific_word():
    specific_word = word_entry.get()
    with open('automatic.html', 'r', encoding='utf-8') as htmlfile:
        html_template = htmlfile.read()
    updated_content = html_template.replace('XXX', specific_word)
    with open('updated_automatic.html', 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(updated_content)
    result_label.config(text="置換が完了しました！")



# ------------重複部分の削除----------------

# 3-1 削除
def deleteSection3_1(html_template, start_marker="<!-- 3-1_DELETE_START -->", end_marker="<!-- 3-1_DELETE_END -->"):
    pattern = re.escape(start_marker) + ".*?" + re.escape(end_marker)
    return re.sub(pattern, '', html_template, flags=re.DOTALL)


# 3-2 削除
def deleteSection3_2(html_template, start_marker="<!-- 3-2_DELETE_START -->", end_marker="<!-- 3-2_DELETE_END -->"):
    pattern = re.escape(start_marker) + ".*?" + re.escape(end_marker)
    return re.sub(pattern, '', html_template, flags=re.DOTALL)


# 5-1 削除
def deleteSection5_1(html_template, start_marker="<!-- 5-1_DELETE_START -->", end_marker="<!-- 5-1_DELETE_END -->"):
    pattern = re.escape(start_marker) + ".*?" + re.escape(end_marker)
    return re.sub(pattern, '', html_template, flags=re.DOTALL)


# 6-1 削除
def deleteSection6_1(html_template, start_marker="<!-- 6-1_DELETE_START -->", end_marker="<!-- 6-1_DELETE_END -->"):
    pattern = re.escape(start_marker) + ".*?" + re.escape(end_marker)
    return re.sub(pattern, '', html_template, flags=re.DOTALL)


# ------------置換部分----------------


# テンプレートのコピー
def copy_template(html_content, start_marker, end_marker):
    start_index = html_content.find(start_marker)
    end_index = html_content.find(end_marker) + len(end_marker)
    return html_content[start_index:end_index]

# 内容の置換
def replace_content(template_section, csv_row):
    return template_section.replace("<!-- CONTENT_HERE -->", csv_row[0]) # csv_row[0] を適切な列データに置き換えてください

# 新しいセクションの挿入
def insert_new_section(html_content, template_section, new_sections):
    return html_content.replace(template_section, ''.join(new_sections))

# テンプレートの削除
def remove_template(html_content, template_section):
    return html_content.replace(template_section, "")


# 1. CSVファイルを読み込む
with open('path/to/your/csvfile.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data = row[YOUR_COLUMN_INDEX]  # YOUR_COLUMN_INDEXを列のインデックスに置き換える

# 2. データを「、」または「。」で分割
items = re.split('、|。', data)

# 3. 新しい <li> 要素を作成し、すべてを <ul> タグでラップ
ul_content = '<ul class="is-style-check_list">\n'
for item in items:
    if item:  # 余分な空の項目を避ける
        ul_content += f'    <li>{item}</li>\n'
ul_content += '</ul>'



html_content = html_content.replace('<!-- REPLACE_UL_LIST -->', ul_content, 1)

# 5. 新しいHTMLファイルを保存
with open('path/to/your/new_htmlfile.html', 'w', encoding='utf-8') as new_htmlfile:
    new_htmlfile.write(html_content)



