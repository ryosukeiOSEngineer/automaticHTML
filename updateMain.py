import re
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd


# ------------csv読込 + xxx置換 + html_templateを定義----------------

# csvファイルを読み込み
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df


# 特定のワードの置換
def replace_specific_word(html_template, specific_word):
    return html_template.replace('XXX', specific_word), "置換が完了しました！"


# html_templateを定義
with open('automatic.html', 'r', encoding='utf-8') as htmlfile:
    html_template = htmlfile.read()





# ------------重複部分の削除----------------

# 3-1 削除
def deleteSection3_1(html_template, start_marker="<!-- 3-1_DELETE_START -->", end_marker="<!-- 3-1_DELETE_END -->"):
    deleted_part3_1 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    match = re.search(deleted_part3_1, html_template, flags=re.DOTALL) # 削除部分（deleted_part3_1）がHTMLファイル（html_template）から探す
    if match:
        print("削除部分:")
        # print(match.group(1))
    return re.sub(deleted_part3_1, '', html_template, flags=re.DOTALL)


# 3-2 削除
def deleteSection3_2(html_template, start_marker="<!-- 3-2_DELETE_START -->", end_marker="<!-- 3-2_DELETE_END -->"):
    deleted_part3_2 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    match = re.search(deleted_part3_2, html_template, flags=re.DOTALL) # 削除部分（deleted_part3_2）がHTMLファイル（html_template）から探す
    if match:
        print("削除部分:")
        # print(match.group(1))
    return re.sub(deleted_part3_2, '', html_template, flags=re.DOTALL)


# 5-1 削除
def deleteSection5_1(html_template, start_marker="<!-- 5-1_DELETE_START -->", end_marker="<!-- 5-1_DELETE_END -->"):
    deleted_part5_1 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    match = re.search(deleted_part5_1, html_template, flags=re.DOTALL) # 削除部分（deleted_part5_1）がHTMLファイル（html_template）から探す
    if match:
        print("削除部分:")
        # print(match.group(1))
    return re.sub(deleted_part5_1, '', html_template, flags=re.DOTALL)


# 6-1 削除
def deleteSection6_1(html_template, start_marker="<!-- 6-1_DELETE_START -->", end_marker="<!-- 6-1_DELETE_END -->"):
    deleted_part6_1 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    match = re.search(deleted_part6_1, html_template, flags=re.DOTALL) # 削除部分（deleted_part6_1）がHTMLファイル（html_template）から探す
    if match:
        print("削除部分:")
        # print(match.group(1))
    return re.sub(deleted_part6_1, '', html_template, flags=re.DOTALL)






# ------------検索部分の定義----------------

# アマゾン
def amazon_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    base_url = '<a href="https://www.amazon.co.jp/s?k={}" rel="nofollow" class="broken_link" automate_uuid="380281b6-9831-458d-8c58-fd88155abd2f" data-nodal="">サイトを見る</a>'
    return base_url.format(xxx)

# 楽天
def rakuten_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    base_url = f'<a rel="nofollow" href="https://search.rakuten.co.jp/search/mall/{xxx}/" automate_uuid="0d65ad2e-2c1f-42fa-bd6b-770a5da511fd" data-nodal="">サイトを見る</a>'
    return base_url

# Yahoo!
def yahoo_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    suffix = "&sc_i=shp_pc__searchBox&area=11"
    base_url = f'<a href="https://shopping.yahoo.co.jp/search?first=1&tab_ex=commerce&fr=shp-prop&mcr=16ce063bd8359bdabe7e46ba148bf218&ts=1666874543&sretry=1&p={xxx}{suffix}" rel="nofollow" automate_uuid="17295db3-ed57-461e-8da9-cf114fb960d0" data-nodal="">サイトを見る</a>'
    return base_url

# google
def google_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    base_url = f'<a href="https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q={xxx}&btnG=" automate_uuid="b3b85ab3-87b3-4b18-be11-957952436ce1" data-nodal="">論文を見る</a>'
    return base_url

# cinii
def cinii_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    base_url = f'<a href="https://ci.nii.ac.jp/search?q={xxx}" automate_uuid="10ade5da-f2ac-460a-bfda-6c521f1e3fe2" data-nodal="">論文を見る</a>'
    return base_url

# jstage
def jstage_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    base_url = f'<a href="https://www.jstage.jst.go.jp/result/global/-char/ja?globalSearchKey={xxx}" automate_uuid="d7c9d5f5-b6ec-40f4-a5c2-0f7cd4046d72" data-nodal="">論文を見る</a>'
    return base_url

# IRDB
def IRDB_search(xxx):
    xxx = xxx.replace(" ", "+")  # スペースを+に置換
    base_url = f'<a href="https://irdb.nii.ac.jp/search?kywd={xxx}&op=%E6%A4%9C%E7%B4%A2&fulltextflg=All&title=&description=&creator=&creatoraf=&creatorid=&publisher=&journal=&pubdate=&open_volume=&open_issue=&open_spage=&open_epage=&doi=&id=&typeid=&versiontypeid=&fundaf=&diaf=&dino=&kikanid=&items_per_page=20&sort=ss_record%2Bdesc" automate_uuid="6b415cab-69da-48cd-96b6-0dc3fbf3a825" data-nodal="">論文を見る</a>'
    return base_url



# ------------置換部分の関数定義----------------


# <!-- 1-RED -->
def replace_1_red(df):
    csv_data_1_red = df.loc[0, '8. 水素水のメリットを3つ教えてください']
    csv_split_list = re.split('、|。', csv_data_1_red)
    csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
    csv_split_join = ' '.join(csv_list_customize)
    html_insert_1_red = f'<p>XXXは{csv_split_join}などが魅力です。</p>'
    return html_insert_1_red

df = pd.read_csv(file_path)

print(replace_1_red(df))

# <!-- 1-BLUE -->


# <!-- 1-GREEN -->












# ------------検索部分の置換するための関数定義----------------













# ------------ループ処理----------------

# ループ処理のテンプレートのコピー
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


# # 1. CSVファイルを読み込む
# with open('path/to/your/csvfile.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         data = row[YOUR_COLUMN_INDEX]  # YOUR_COLUMN_INDEXを列のインデックスに置き換える

# # 2. データを「、」または「。」で分割
# items = re.split('、|。', data)

# # 3. 新しい <li> 要素を作成し、すべてを <ul> タグでラップ
# ul_content = '<ul class="is-style-check_list">\n'
# for item in items:
#     if item:  # 余分な空の項目を避ける
#         ul_content += f'    <li>{item}</li>\n'
# ul_content += '</ul>'



# ------------削除、置換の処理----------------

# 削除処理の実行
html_template = deleteSection3_1(html_template)
html_template = deleteSection3_2(html_template)
html_template = deleteSection5_1(html_template)
html_template = deleteSection6_1(html_template)


# 置換処理の実行











# 検索部分の置換処理の実行












# 更新された内容を新しいファイルに保存する
# updated_automatic.htmlに集約させるイメージ
with open('updated_automatic.html', 'w', encoding='utf-8') as htmlfile:
    htmlfile.write(html_template)


# ------------GUI----------------

def browse_file():
    '''
    GUIでcsvファイルを選択して置換するためのデータを読み込む 
    '''
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
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
    xxx_substituted_content = replace_specific_word(html_template, specific_word)
    
    # 置換したHTMLをテキストウィジェットに表示
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, xxx_substituted_content)
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

