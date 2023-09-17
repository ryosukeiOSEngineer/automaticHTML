import re
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

# 元々のHTMLの名称変更しやすいように変数化
HTML_TEMPLATE_FORMAT = 'automatic.html'


# 特定のワードの置換
def replace_XXX(html_template, specific_word):
    # 'XXX' を特定のワードで置換
    xxx_substituted_content = html_template.replace('XXX', specific_word)
    message = "置換が完了しました！"
    
    return xxx_substituted_content, message


# HTML_TEMPLATE_FORMATを読み込んでコピーを作成
with open(HTML_TEMPLATE_FORMAT, 'r', encoding='utf-8') as htmlfile:
    html_template = htmlfile.read()


# ------------csv読込 + xxx置換 + html_templateを定義----------------

df = None

# GUIでcsvファイルを選択して置換するためのデータを読み込む 
# dfをグローバル変数化 CSVファイルのデータを保持するデータフレームへ置換
def browse_file():
    global df
    global file_entry
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    print(f"Selected file path: {file_path}")
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)
    
    try: # 処理が成功したら
        df = pd.read_csv(file_path)
        result_label.config(text="CSVファイルが正常にロードされました")
    except FileNotFoundError:
        print("指定されたパスにファイルが存在しません。パスを確認してください。")
    except pd.errors.EmptyDataError:
        print("ファイルが空です。データを確認してください。")
    except Exception as e:
        print(f"データフレームのロードに失敗しました: {e}")

# ------------重複部分の削除----------------

# 3-1 削除
def deleteSection3_1(html_template, start_marker="<!-- 3-1_DELETE_START -->", end_marker="<!-- 3-1_DELETE_END -->"):
    deleted_part3_1 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    return re.sub(deleted_part3_1, '', html_template, flags=re.DOTALL)


# 3-2 削除
def deleteSection3_2(html_template, start_marker="<!-- 3-2_DELETE_START -->", end_marker="<!-- 3-2_DELETE_END -->"):
    deleted_part3_2 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    return re.sub(deleted_part3_2, '', html_template, flags=re.DOTALL)


# 5-1 削除
def deleteSection5_1(html_template, start_marker="<!-- 5-1_DELETE_START -->", end_marker="<!-- 5-1_DELETE_END -->"):
    deleted_part5_1 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    return re.sub(deleted_part5_1, '', html_template, flags=re.DOTALL)


# 6-1 削除
def deleteSection6_1(html_template, start_marker="<!-- 6-1_DELETE_START -->", end_marker="<!-- 6-1_DELETE_END -->"):
    deleted_part6_1 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    return re.sub(deleted_part6_1, '', html_template, flags=re.DOTALL)


# ------------検索部分の定義----------------


# ------------置換部分の関数定義----------------


# <!-- 1-RED -->
# 置換を定義する関数
def define_1_red(df): 
    try: # もし成功したら
        csv_data_1_red = df.loc[0, '8. 水素水のメリットを3つ教えてください']
        csv_split_list = re.split('、|。|\n', csv_data_1_red)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ' '.join(csv_list_customize)
        html_insert_1_red = f'<p>XXXは{csv_split_join}などが魅力です。</p>'
        return html_insert_1_red
    except Exception as e: # もし失敗したら
        print(f"1-REDの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_1_red(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_1_red(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 1-RED -->\s*<p>).*?(</p>)'

    updated_html_part_1_red = re.sub(pattern, f'\\1{html_insert[3:]}\\2', html_template)
    print("1-REDの置換が成功しました。")
    return updated_html_part_1_red


# <!-- 1-BLUE -->

# <!-- 1-GREEN -->

# ------------検索部分の置換するための関数定義----------------

# ------------ループ処理----------------

def delete_sections(html_template):
    html_template = deleteSection3_1(html_template)
    html_template = deleteSection3_2(html_template)
    html_template = deleteSection5_1(html_template)
    html_template = deleteSection6_1(html_template)
    return html_template

def replace_sections(html_template, df):
    html_template = replace_1_red(html_template, df)

    
    # 他の置換処理もここで行う
    return html_template

def main_function(html_template, df):
    html_template = delete_sections(html_template)
    html_template = replace_sections(html_template, df)
    return html_template



# その後の処理で更新されたテンプレートを使用する
with open('NEW ﾌｧｲﾙ.html', 'w', encoding='utf-8') as htmlfile:
    htmlfile.write(html_template)


# ------------削除、置換の処理----------------




# ------------GUI----------------


def on_generate_button_click():
    with open(HTML_TEMPLATE_FORMAT, 'r', encoding='utf-8') as htmlfile:
        html_template = htmlfile.read()

    file_path = file_entry.get()
    specific_word = word_entry.get()
    
    if not file_path or file_path == 'ファイルを選択してください':
        result_label.config(text="エラー: ファイルが選択されていません")
        return
    
    if not specific_word:
        result_label.config(text="エラー: 特定のワードが入力されていません")
        return

    # DataFrameをCSVファイルから読み込む
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        result_label.config(text=f"エラー: CSVファイルを読み込めませんでした - {e}")
        return

    # main_functionを呼び出し
    # main_functionを呼び出し、結果を受け取る
    updated_html_template = main_function(html_template, df)


    # 置換後のHTMLをテキストウィジェットに表示
    with open('NEW ﾌｧｲﾙ.html', 'r', encoding='utf-8') as htmlfile:
        html_template = htmlfile.read()

    # HTMLテンプレートをテキストウィジェットから取得
    html_template = text_widget.get("1.0", tk.END)


    # replace_XXX 関数を呼び出してテンプレートを置換
    XXX_change_html, message = replace_XXX(updated_html_template, specific_word)

    with open('NEW ﾌｧｲﾙ.html', 'w', encoding='utf-8') as outfile:
        outfile.write(XXX_change_html)

    print(message)

    # 置換後のHTMLをテキストウィジェットに表示
    with open('NEW ﾌｧｲﾙ.html', 'r', encoding='utf-8') as htmlfile:
        updated_html_template = htmlfile.read()
    
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, updated_html_template)
    result_label.config(text="HTML生成が完了しました！")


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


# その他のボタンを配置
generate_button = tk.Button(grid_frame, text="HTML生成 START", command=on_generate_button_click)
generate_button.grid(row=4, column=0, columnspan=3, pady=10)

copy_button = tk.Button(grid_frame, text="HTML コピー", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, columnspan=3, pady=10)

# 結果を表示するラベル
result_label = tk.Label(grid_frame, text="")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# テキストウィジェットとスクロールバーの設置
text_widget = tk.Text(root, wrap=tk.NONE)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll_y = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_x = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=text_widget.xview)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

text_widget.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# アプリケーションの起動時にHTMLテンプレートをテキストウィジェットにロード
with open(HTML_TEMPLATE_FORMAT, 'r', encoding='utf-8') as htmlfile:
    initial_html_template = htmlfile.read()
text_widget.insert(tk.END, initial_html_template)

root.mainloop()