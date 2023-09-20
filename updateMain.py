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


# 6-1 削除    調整必須
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
# 置換を定義する関数
def define_1_blue(df): 
    try: # もし成功したら
        csv_data_1_blue = df.loc[1, '8. 水素水のメリットを3つ教えてください']
        csv_split_list = re.split('、|。|\n', csv_data_1_blue)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ' '.join(csv_list_customize)
        html_insert_1_blue = f'<p>意味があるとされるおすすめポイントは{csv_split_join}などがあります。</p>'
        return html_insert_1_blue
    except Exception as e: # もし失敗したら
        print(f"1-REDの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_1_blue(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_1_blue(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 1-BLUE -->\s*<p>).*?(</p>)'

    updated_html_part_1_blue = re.sub(pattern, f'\\1{html_insert[3:]}\\2', html_template)
    print("1-BLUEの置換が成功しました。")
    return updated_html_part_1_blue


# <!-- 1-GREEN -->
# 置換を定義する関数
def define_1_green(df): 
    try: # もし成功したら
        csv_data_1_green = df.loc[2:, '8. 水素水のメリットを3つ教えてください'].tolist()
        csv_split_list = []
        for item in csv_data_1_green:
            csv_split_list.extend(re.split('、|。|\n', str(item)))
        csv_list_customize = ['<li>' + item + '</li>' for item in csv_split_list if item]
        csv_split_join = '\n\n\n\n'.join(csv_list_customize)
        
        html_insert_1_green = f'<ul class="is-style-check_list has-swl-pale-02-background-color has-background">\n{csv_split_join}\n</ul>'
        return html_insert_1_green
    except Exception as e: # もし失敗したら
        print(f"1-GREENの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_1_green(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_1_green(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 1-GREEN -->\s*<ul class="is-style-check_list has-swl-pale-02-background-color has-background">).*?(</ul>)'

    updated_html_part_1_green = re.sub(pattern, html_insert, html_template, flags=re.DOTALL)

    print("1-GREENの置換が成功しました。")
    return updated_html_part_1_green


# <!-- 2-RED -->
# 置換を定義する関数
def define_2_red(df): 
    try: # もし成功したら
        csv_data_2_red = df.loc[0, '13. どんな人におすすめですか？3つ教えてください']
        csv_split_list = re.split('、|。|\n', csv_data_2_red)
        csv_list_customize = ['<li>' + item + '</li>' for item in csv_split_list if item]
        csv_split_join = '\n\n\n\n'.join(csv_list_customize)
        
        html_insert_2_red = f'<ul class="is-style-check_list">\n{csv_split_join}\n</ul>'
        return html_insert_2_red
    except Exception as e: # もし失敗したら
        print(f"2-REDの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_2_red(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_2_red(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 2-RED -->\s*<ul class="is-style-check_list">).*?(</ul>)'

    updated_html_part_2_red = re.sub(pattern, html_insert, html_template, flags=re.DOTALL)

    print("2-REDの置換が成功しました。")
    return updated_html_part_2_red


# <<!-- 3-TAG -->
# 置換を定義する関数
def define_3_tag(df): 
    try: # もし成功したら
        csv_data_3_tag = df.loc[0:, '7. 前問で答えた内容を「一言」で言い表してください'].tolist()
        csv_split_list = []
        for item in csv_data_3_tag:
            cleaned_item = str(item).replace(',', '').replace('、', '').replace('.', '').replace('。', '').replace('\n', '') # いらない文字を何も無しに置換して削除
            csv_split_list.append(cleaned_item) # リストから要らない文字を消したものをリストに追加
        csv_list_customize = [
            f'<li class="c-tabList__item" role="presentation"><button role="tab" class="c-tabList__button" aria-selected={"true" if index == 0 else "false"} aria-controls="tab-6deac381-{index}" data-onclick="tabControl">{item}</button></li>' 
            for index, item in enumerate(csv_split_list) if item
        ]

        html_insert_3_tag = '<ul class="c-tabList" role="tablist">' + ''.join(csv_list_customize) + '</ul>'

        return html_insert_3_tag
    except Exception as e: # もし失敗したら
        print(f"3-TAGの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_3_tag(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_3_tag(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 3-TAG -->\s*<ul class="c-tabList" role="tablist">).*?(</ul>)'

    updated_html_part_3_tag = re.sub(pattern, html_insert, html_template, flags=re.DOTALL)

    print("3-TAGの置換が成功しました。")
    return updated_html_part_3_tag


# <!-- 3-TEMPLATE_START -->
# 置換を定義する関数
def html_3_comment_index_generate(html_template, df):
    try:
        index_count = len(df)

        new_template_parts_list = [
            f'''<!-- 3-{index}-REPLACE_START --><div id="tab-6deac381-{index}" class="c-tabBody__item" aria-hidden="false"><div class="swell-block-balloon"><div class="c-balloon -bln-left" data-col="yellow"><!-- 3-icon-{index} --><div class="c-balloon__icon -circle"><img decoding="async" loading="lazy" src="https://iminain.com/wp-content/uploads/2023/06/icon-6-150x150.png" alt="" class="c-balloon__iconImg" width="80px" height="80px"></div><div class="c-balloon__body -speaking -border-none"><!-- 3-comment-{index} --><div class="c-balloon__text">\n<p>体内の活性化</p>\n<span class="c-balloon__shapes"><span class="c-balloon__before"></span><span class="c-balloon__after"></span></span></div></div></div></div>\n\n<!-- 3-P-TAG-{index} -->\n<p>水素水とは、体のサビを取り除き、体内を活性化させてくれるお水で、健康や美容に効果絶大なものになります。</p><!-- 3-{index}-REPLACE_END -->\n'''
            for index in range(index_count)
        ]
        
        # すべての新しいセクションを一つの文字列に連結
        html_insert_3_comment_index = ''.join(new_template_parts_list)


        # 連結した文字列をHTMLテンプレートと置換
        updated_html_3_comment = re.sub(r'<!-- 3-TEMPLATE_START -->(.*?)<!-- 3-TEMPLATE_END -->', html_insert_3_comment_index, html_template, flags=re.DOTALL)
        
        return updated_html_3_comment
    except Exception as e: # もし失敗したら
        print(f"3_comment_indexの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_3_comment(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = html_3_comment_index_generate(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("3_comment_indexの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 3-icon-{index} -->
# 置換を定義する関数
def define_3_icon_index(df,index): 
    # 性別の数値を文字列に変換
    gender_mapping = {
        '1': '男性',
        '2': '女性'
    }
    gender_value = df.loc[index, '2. 回答者様の性別を教えて下さい']
    gender = gender_mapping.get(str(gender_value), '不明') # 数値が1または2でない場合は'不明'とする

    age_group_value = df.loc[index, '3. 回答者様の年齢を教えて下さい']

    # 年齢層を40代以上と40代未満に分ける
    age_40_or_above = int(age_group_value) >= 4

    if gender == '男性':
        if age_40_or_above:
            image_file = 'タブ男性2アイコン.webp'
        else:
            image_file = 'タブ男性アイコン.webp'
    else:
        if age_40_or_above:
            image_file = 'タブ女性2アイコン.webp'
        else:
            image_file = 'タブ女性アイコン.webp'

    return image_file

    # image_fileを<!-- 3-icon-{index} -->へと置換する

# ファイルを読み込んで置換を実施する関数定義
def replace_3_icon_index(html_template, df): 
    # DataFrameの各行に対してループを行う
    for index in df.index:
        # アイコンのファイル名を取得
        image_file = define_3_icon_index(df, index)

        # HTMLテンプレート内の適切なマークアップをアイコンのHTMLタグに置き換える
        placeholder_3_icon = f'<!-- 3-icon-{index} -->'
        img_tag = f'<img src="{image_file}">'
        html_template = html_template.replace(placeholder_3_icon, img_tag)
    # 置換が成功したかどうかを確認
    if "<!-- 3-icon-" in html_template:  # プレースホルダーがまだ存在するかどうかを確認
        print("置換に失敗しました。")
        return html_template

    print("2-REDの置換が成功しました。")
    return html_template


# <!-- 4-RED -->
# 置換を定義する関数
def define_4_red(df): 
    try: # もし成功したら
        csv_data_4_red = df.loc[0, '11. 水素水のデメリットを3つ教えてください']
        csv_split_list = re.split('、|。|\n', csv_data_4_red)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ' '.join(csv_list_customize)
        html_insert_4_red = f'<p>意味ない理由として{csv_split_join}などのコメントがありました。</p>'
        return html_insert_4_red
    except Exception as e: # もし失敗したら
        print(f"4-REDの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_4_red(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_4_red(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 4-RED -->\s*<p>).*?(</p>)'

    updated_html_part_4_red = re.sub(pattern, f'\\1{html_insert[3:]}\\2', html_template)
    print("4-REDの置換が成功しました。")
    return updated_html_part_4_red


# <!-- 4-BLUE -->
# 置換を定義する関数
def define_4_blue(df): 
    try: # もし成功したら
        csv_data_4_blue = df.loc[1:, '11. 水素水のデメリットを3つ教えてください'].tolist()
        csv_split_list = []
        for item in csv_data_4_blue:
            csv_split_list.extend(re.split('、|。|\n', str(item)))
        csv_list_customize = ['<li>' + item + '</li>' for item in csv_split_list if item]
        csv_split_join = '\n\n\n\n'.join(csv_list_customize)
        
        html_insert_4_blue = f'<ul class="is-style-triangle_list">\n{csv_split_join}\n</ul>'
        return html_insert_4_blue
    except Exception as e: # もし失敗したら
        print(f"4-BLUEの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_4_blue(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_4_blue(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 4-BLUE -->\s*<ul class="is-style-triangle_list">).*?(</ul>)'

    updated_html_part_4_blue = re.sub(pattern, html_insert, html_template, flags=re.DOTALL)

    print("4-BLUEの置換が成功しました。")
    return updated_html_part_4_blue


# <!-- 7-RED -->
# 置換を定義する関数
def define_7_red(df): 
    try: # もし成功したら
        csv_data_7_red = df.loc[0, '13. どんな人におすすめですか？3つ教えてください']
        csv_split_list = re.split('、|。|\n', csv_data_7_red)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ' '.join(csv_list_customize)
        html_insert_7_red = f'<p>特に{csv_split_join}におすすめです。</p>'
        return html_insert_7_red
    except Exception as e: # もし失敗したら
        print(f"7-REDの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_7_red(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_7_red(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 7-RED -->\s*<p>).*?(</p>)'

    updated_html_part_7_red = re.sub(pattern, f'\\1{html_insert[3:]}\\2', html_template)
    print("7-REDの置換が成功しました。")
    return updated_html_part_7_red

# <!-- 7-BLUE -->
# 置換を定義する関数
def define_7_blue(df): 
    try: # もし成功したら
        csv_data_7_blue = df.loc[1:, '13. どんな人におすすめですか？3つ教えてください'].tolist()
        csv_split_list = []
        for item in csv_data_7_blue:
            csv_split_list.extend(re.split('、|。|\n', str(item)))
        csv_list_customize = ['<li>' + item + '</li>' for item in csv_split_list if item]
        csv_split_join = '\n\n\n\n'.join(csv_list_customize)
        
        html_insert_7_blue = f'<ul class="is-style-check_list">\n{csv_split_join}\n</ul>'
        return html_insert_7_blue
    except Exception as e: # もし失敗したら
        print(f"7-BLUEの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_7_blue(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_7_blue(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 7-BLUE -->\s*<ul class="is-style-check_list">).*?(</ul>)'

    updated_html_part_7_blue = re.sub(pattern, html_insert, html_template, flags=re.DOTALL)

    print("7-BLUEの置換が成功しました。")
    return updated_html_part_7_blue


# <!-- 8-RED -->
# 置換を定義する関数
def define_8_red(df): 
    try: # もし成功したら
        csv_data_8_red = df.loc[0, '8. 水素水のメリットを3つ教えてください']
        csv_split_list = re.split('、|。|\n', csv_data_8_red)
        csv_split_join = '、'.join(csv_split_list)
        html_insert_8_red = f'<p>XXXは{csv_split_join}のが魅力です。【意味ナイン】では、XXXは意味ないのか、意味あるのか調査し、評判やコメント、おすすめ代替案について紹介しています。</p>'
        return html_insert_8_red
    except Exception as e: # もし失敗したら
        print(f"8-REDの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_8_red(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_8_red(df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template
    
    # コメントタグの直後の p タグを置換する正規表現パターン
    pattern = r'(<!-- 8-RED -->\s*<p>).*?(</p>)'

    updated_html_part_8_red = re.sub(pattern, f'\\1{html_insert[3:]}\\2', html_template)
    print("8-REDの置換が成功しました。")
    return updated_html_part_8_red




# ------------ループ処理----------------


# 削除実行処理
def delete_sections(html_template):
    html_template = deleteSection3_1(html_template)
    html_template = deleteSection3_2(html_template)
    # html_template = deleteSection5_1(html_template)
    html_template = deleteSection6_1(html_template)
    return html_template

# 置換実行処理
def replace_sections(html_template, df):
    html_template = replace_1_red(html_template, df)
    html_template = replace_1_blue(html_template, df)
    html_template = replace_1_green(html_template, df)
    html_template = replace_2_red(html_template, df)
    html_template = replace_3_tag(html_template, df)
    html_template = replace_3_comment(html_template, df)
    html_template = replace_3_icon_index(html_template, df)
    html_template = replace_4_red(html_template, df)
    html_template = replace_4_blue(html_template, df)
    html_template = replace_7_red(html_template, df)
    html_template = replace_7_blue(html_template, df)
    html_template = replace_8_red(html_template, df)
    # 他の置換処理もここで行う
    return html_template


# 全ての処理を実行
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
    result_label.config(text="コピーされました！")

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