import re
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
# import uuid
import subprocess

def run_file_change():
    subprocess.run(["python", "file_change.py"])


# 仮のIDを発行するため
# def generate_uuid():
#     return str(uuid.uuid4())

# 元々のHTMLの名称変更しやすいように変数化
HTML_TEMPLATE_FORMAT = 'automatic3.html'


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

    # 現在のスクリプトの場所を取得
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # このパスを初期ディレクトリとして指定
    file_path = filedialog.askopenfilename(initialdir=current_directory, filetypes=[("CSV Files", "*.csv")])

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


# 3-最終のpタグ 削除
def deleteSection3_lastptag(html_template, start_marker="<!-- 3-LASTPTAG-DELETE-START -->", end_marker="<!-- 3-LASTPTAG-DELETE-END -->"):
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


# 6-2 削除    調整必須
def deleteSection6_2(html_template, start_marker="<!-- 6-2-DELETE_START -->", end_marker="<!-- 6-2-DELETE_END -->"):
    deleted_part6_2 = re.escape(start_marker) + "(.*?)" + re.escape(end_marker)
    return re.sub(deleted_part6_2, '', html_template, flags=re.DOTALL)



# ------------置換部分の関数定義----------------


# <!-- 1-RED -->
# 置換を定義する関数
def define_1_red(df): 
    try: # もし成功したら
        csv_data_1_red = df.iloc[0, 14] #'8. 水素水のメリットを3つ教えてください'
        csv_split_list = re.split('、|。|\n', csv_data_1_red)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ''.join(csv_list_customize)
        html_insert_1_red = f'<p>XXXは{csv_split_join}などが魅力です。'
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
        csv_data_1_blue = df.iloc[1, 14]  # '8. 水素水のメリットを3つ教えてください'
        csv_split_list = re.split('、|。|\n', csv_data_1_blue)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ''.join(csv_list_customize)
        html_insert_1_blue = f'<p>意味があるとされるおすすめポイントは{csv_split_join}などがあります。'
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
        csv_data_1_green = df.iloc[2:, 14].tolist()
        csv_split_list = []
        for item in csv_data_1_green:
            csv_split_list.extend(re.split('、|。|\n', str(item)))
        csv_list_customize = ['<!-- wp:list-item -->\n<li>' + item + '</li>\n<!-- /wp:list-item -->' for item in csv_split_list if item]
        csv_split_join = '\n\n'.join(csv_list_customize)
        
        html_insert_1_green = f'<ul class="is-style-check_list has-swl-pale-02-background-color has-background">{csv_split_join}</ul>'
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
        csv_data_2_red = df.iloc[0, 19] #'13. どんな人におすすめですか？3つ教えてください'
        csv_split_list = re.split('、|。|\n', csv_data_2_red)
        csv_list_customize = ['<!-- wp:list-item -->\n<li>' + item + '</li>\n<!-- /wp:list-item -->' for item in csv_split_list if item]
        csv_split_join = '\n\n'.join(csv_list_customize)
        
        html_insert_2_red = f'<ul class="is-style-check_list">{csv_split_join}</ul>'
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
        csv_data_3_tag = df.iloc[0:, 13].tolist() #'7. 前問で答えた内容を「一言」で言い表してください'
        csv_split_list = []
        for item in csv_data_3_tag:
            cleaned_item = str(item).replace(',', '').replace('、', '').replace('.', '').replace('。', '').replace('\n', '') # いらない文字を何も無しに置換して削除
            csv_split_list.append(cleaned_item) # リストから要らない文字を消したものをリストに追加
        csv_list_customize = [
            f"<li class=\"c-tabList__item\" role=\"presentation\"><button role=\"tab\" class=\"c-tabList__button\" aria-selected=\"{'true' if index == 0 else 'false'}\" aria-controls=\"tab-6deac381-{index}\" data-onclick=\"tabControl\">{item}</button></li>" 
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
            f'''<!-- wp:loos/tab-body {{"id":1,"tabId":"6deac381"}} -->\n<div id="tab-6deac381-{index}" class="c-tabBody__item" aria-hidden={{'"false"' if index == 0 else '"true"'}}><!-- wp:loos/balloon {{"balloonID":"14"}} --><div class="swell-block-balloon"><div class="c-balloon -bln-left" data-col="yellow"><!-- 3-ICON-START-{index} --><div class="c-balloon__icon -circle"><img decoding="async" loading="lazy" src="https://iminain.com/wp-content/uploads/2023/06/icon-6-150x150.png" alt="" class="c-balloon__iconImg" width="80px" height="80px"><!-- 3-ICON-END-{index} --></div><div class="c-balloon__body -speaking -border-none"><div class="c-balloon__text"><!-- 3-COMMENT-START-{index} -->\n<p>体内の活性化</p>\n<!-- /wp:loos/balloon --><!-- 3-COMMENT-END-{index} --><span class="c-balloon__shapes"><span class="c-balloon__before"></span><span class="c-balloon__after"></span></span></div></div></div></div><!-- 3-PTAG-START-{index} --><p>水素水とは、体のサビを取り除き、体内を活性化させてくれるお水で、健康や美容に効果絶大なものになります。</p><!-- 3-PTAG-END-{index} -->\n<!-- /wp:loos/tab-body -->'''
            for index in range(index_count)
        ]
        
        # すべての新しいセクションを一つの文字列に連結
        html_insert_3_comment_index = '\n\n'.join(new_template_parts_list)


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


# <!-- 3-ICON-START-{index} -->
# 置換を定義する関数
def define_3_icon_index(df,index): 
    # 性別の数値を文字列に変換
    gender_mapping = {
        '1': '男性',
        '2': '女性'
    }
    gender_value = df.iloc[index, 4]  #'2. 回答者様の性別を教えて下さい'
    gender = gender_mapping.get(str(gender_value), '不明') # 数値が1または2でない場合は'不明'とする

    age_group_value = df.iloc[index, 6]  # '3. 回答者様の年齢を教えて下さい'

    # 年齢層を40代以上と40代未満に分ける
    age_40_or_above = int(age_group_value) >= 4

    if gender == '男性':
        if age_40_or_above:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/men-2-150x150.png'
        else:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/men-1-150x150.png'
    else:
        if age_40_or_above:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/icon-6-150x150.png'
        else:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/icon-5-150x150.png'

    return image_file

    # image_fileを<!-- 3-icon-{index} -->へと置換する


# ファイルを読み込んで置換を実施する関数定義
def replace_3_icon_index(html_template, df): 
    # DataFrameの各行に対してループを行う
    for index in df.index:
        # アイコンのファイル名を取得
        image_file = define_3_icon_index(df, index)

        replace_3_comment_index = f'<div class="c-balloon__icon -circle"><img decoding="async" loading="lazy" src="{image_file}" alt="" class="c-balloon__iconImg" width="80px" height="80px">'

        # placeholder = fr'<!-- 3-ICON-START-{index} -->(.*?)<!-- 3-ICON-END-{index} -->'
        # if re.search(placeholder, html_template):
        #     print(f"Placeholder found for index {index}")
        # else:
        #     print(f"Placeholder not found for index {index}")

        html_template = re.sub(fr'<!-- 3-ICON-START-{index} -->(.*?)<!-- 3-ICON-END-{index} -->', replace_3_comment_index, html_template, flags=re.DOTALL)
        
        
    # 置換が成功したかどうかを確認
    if "<!-- 3-ICON-" in html_template:  # プレースホルダーがまだ存在するかどうかを確認
        print("置換に失敗しました。")
        return html_template

    print("3-ICONの置換が成功しました。")
    return html_template

# <!-- 3-COMMENT-START-{index} -->
# 置換を定義する関数
def define_3_comment_index(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_3_comment = row[13]  #'7. 前問で答えた内容を「一言」で言い表してください'
        cleaned_comment = re.sub('、|。|\n', '', csv_data_3_comment)  # デリミタでクリーニング
        
        pattern = f"<!-- 3-COMMENT-START-{index} --><p>(.*?)</p><!-- 3-COMMENT-END-{index} -->"
        replacement = f"<!-- 3-COMMENT-START-{index} --><p>{cleaned_comment}</p><!-- 3-COMMENT-END-{index} -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_3_comment_index(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_3_comment_index(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("3_comment_indexの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 3-PTAG-START-{index} -->
# 置換を定義する関数
def define_3_ptag_index(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_3_ptag = row[12] #'6. 水素水を全く知らない人に説明してください（客観的に）※感想ではありません'
        cleaned_3_ptag_list = csv_data_3_ptag.replace('。', '。\n').split('\n')

        # cleaned_3_ptag_listの各要素を<p></p>で囲んで連結
        cleaned_3_ptag = ''.join([f"\n\n<!-- wp:paragraph -->\n<p>{sentence}</p>\n<!-- /wp:paragraph -->" for sentence in cleaned_3_ptag_list if sentence])

        pattern = f"<!-- 3-PTAG-START-{index} -->(.*?)<!-- 3-PTAG-END-{index} -->"
        replacement = f"<!-- 3-PTAG-START-{index} -->{cleaned_3_ptag}<!-- 3-PTAG-END-{index} --></div>"
        updated_html = re.sub(pattern, replacement, updated_html, flags=re.DOTALL)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_3_ptag_index(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_3_ptag_index(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("3-PTAGの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 4-RED -->
# 置換を定義する関数
def define_4_red(df): 
    try: # もし成功したら
        csv_data_4_red = df.iloc[0, 17]  # '11. 水素水のデメリットを3つ教えてください'
        csv_split_list = re.split('、|。|\n', csv_data_4_red)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ''.join(csv_list_customize)
        html_insert_4_red = f'<p>意味ない理由として{csv_split_join}などのコメントがありました。'
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
        csv_data_4_blue = df.iloc[1:, 17].tolist()  #'11. 水素水のデメリットを3つ教えてください'
        csv_split_list = []
        for item in csv_data_4_blue:
            csv_split_list.extend(re.split('、|。|\n', str(item)))
        csv_list_customize = ['<!-- wp:list-item -->\n<li>' + item + '</li>\n<!-- /wp:list-item -->' for item in csv_split_list if item]
        csv_split_join = '\n\n'.join(csv_list_customize)
        
        html_insert_4_blue = f'<ul class="is-style-triangle_list">{csv_split_join}</ul>'
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


# <!-- 5-TEMPLATE_START -->
# 置換を定義する関数
def html_5_comment_index_generate(html_template, df):
    try:
        half_index_count = len(df) // 2

        new_template_parts_list = [
        f'''<!-- 5-TEMPLATE-{index}-START --><!-- wp:columns -->\n<div class="wp-block-columns"><!-- wp:column -->\n<div class="wp-block-column"><!-- wp:group {{"className":"is-style-bg_grid","layout":{"type":"default"}}} -->\n<div class="wp-block-group is-style-bg_grid"><!-- wp:columns {{"isStackedOnMobile":false}} -->\n<div class="wp-block-columns is-not-stacked-on-mobile"><!-- wp:column {{"width":"33.33%"}} -->\n<div class="wp-block-column" style="flex-basis:33.33%">!-- wp:image {{"id":13148,"width":"90px","height":"300px","sizeSlug":"full","linkDestination":"none"}} -->\n<figure class="wp-block-image size-full is-resized"><!-- 5-{index}-ICON-START --><img src="https://iminain.com/wp-content/uploads/2023/06/women-touka-2.png" alt="" class="wp-image-13148" style="width:90px;height:300px"/><!-- 5-{index}-ICON-END --></figure>\n<!-- /wp:image --></div>\n<!-- /wp:column -->\n\n<!-- wp:column {{"width":"66.66%"}} -->\n<div class="wp-block-column" style="flex-basis:66.66%">\n<!-- wp:paragraph -->\n<p>期間：<!-- 5-{index}-PERIOD-START -->1ヵ月未満<!-- 5-{index}-PERIOD-END --><br>満足度：<span class="swl-format-1"><!-- 5-{index}-SATISFACTION-START -->満足（意味があった）<!-- 5-{index}-SATISFACTION-END --></span></p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph {{"align":"right"}} -->\n<p class="has-text-align-right">\n<!-- 5-{index}-AGE-START -->40代<!-- 5-{index}-AGE-END -->・<!-- 5-{index}-GENDER-START -->女性<!-- 5-{index}-GENDER-END --></p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:column --></div>\n<!-- /wp:columns -->\n\n<!-- wp:paragraph --><!-- 5-COMMENT1 -->\n<p><mark style="background-color:rgba(0, 0, 0, 0);color:#6d3a00" class="has-inline-color"><!-- 5-{index}-COMMENT1-START -->肌がツヤツヤになりました。<!-- 5-{index}-COMMENT1-END --></mark></p>\n<!-- /wp:paragraph -->\n\n<!-- wp:paragraph --><!-- 5-COMMENT2 -->\n<p><mark style="background-color:rgba(0, 0, 0, 0);color:#6d3a00" class="has-inline-color"><!-- 5-{index}-COMMENT2-START -->便秘に悩まされていたので、どうしたらいいのか、色々調べていくうちに水素水に辿り着きました。飲んで1週間くらいは何もかわらなかったのですが、2週間目から、腸の調子がよくなり、便秘がなおりました。それと同時に肌荒れも改善されました。今はツヤツヤお肌をキープしてます。<!-- 5-{index}-COMMENT2-END --></mark></p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:group --></div>\n<!-- /wp:column -->\n\n<!-- wp:column -->\n<div class="wp-block-column"><!-- wp:group {{"className":"is-style-bg_grid","layout":{"type":"default"}}} -->\n<div class="wp-block-group is-style-bg_grid"><!-- wp:columns {{"isStackedOnMobile":false}} -->\n<div class="wp-block-columns is-not-stacked-on-mobile"><!-- wp:column {{"width":"33.33%"}} -->\n<div class="wp-block-column" style="flex-basis:33.33%"><!-- wp:image {{"id":13148,"width":"90px","height":"300px","sizeSlug":"full","linkDestination":"none"}} -->\n<figure class="wp-block-image size-full is-resized"><!-- 5-{index+1}-ICON-START --><img src="https://iminain.com/wp-content/uploads/2023/06/women-touka-2.png" alt="" class="wp-image-13148" style="width:90px;height:300px"/><!-- 5-{index+1}-ICON-END --></figure>\n<!-- /wp:image --></div>\n<!-- /wp:column -->\n\n<!-- wp:column {{"width":"66.66%"}} -->\n<div class="wp-block-column" style="flex-basis:66.66%"><!-- wp:paragraph -->\n<p>期間：<!-- 5-{index+1}-PERIOD-START -->3年以上<!-- 5-{index+1}-PERIOD-END --><br>満足度：<span class="swl-format-1"><!-- 5-{index+1}-SATISFACTION-START -->満足（意味があった）<!-- 5-{index}-SATISFACTION-END --></span></p>\n<!-- /wp:paragraph -->\n\n<!-- wp:paragraph {{"align":"right"}} --><p class="has-text-align-right">\n<!-- 5-{index+1}-AGE-START -->30代<!-- 5-{index+1}-AGE-END -->・<!-- 5-{index+1}-GENDER-START -->女性<!-- 5-{index+1}-GENDER-END --></p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:column --></div>\n<!-- /wp:columns -->\n\n<!-- wp:paragraph -->\n<p><mark style="background-color:rgba(0, 0, 0, 0);color:#6d3a00" class="has-inline-color"><!-- 5-{index+1}-COMMENT1-START -->今までは普通の安いミネラルウォーターを飲んでいましたが、水素水に変えてから便通がよくなりました。<!-- 5-{index+1}-COMMENT1-END --></mark></p>\n<!-- /wp:paragraph -->\n\n<!-- wp:paragraph -->\n<p><mark style="background-color:rgba(0, 0, 0, 0);color:#6d3a00" class="has-inline-color"><!-- 5-{index+1}-COMMENT2-START -->個人的には、腸活に役立っている気がします。また、便通が良くなったことで肌トラブルも少なくなった気がします。子どもも嫌がらずに水素水を飲んでくれるので、食育としても助かっている商品です。<!-- 5-{index+1}-COMMENT2-END --></mark></p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:group --></div>\n<!-- /wp:column --></div>\n<!-- /wp:columns -->'''
            for index in range(0, 2*half_index_count, 2)
        ]
        
        # すべての新しいセクションを一つの文字列に連結
        html_insert_5_comment_index = '\n\n'.join(new_template_parts_list)


        # 連結した文字列をHTMLテンプレートと置換
        updated_html_5_comment = re.sub(r'<!-- 5-TEMPLATE_START -->(.*?)<!-- 5-TEMPLATE_END -->', html_insert_5_comment_index, html_template, flags=re.DOTALL)
        
        return updated_html_5_comment
    except Exception as e: # もし失敗したら
        print(f"5_comment_indexの置換生成に失敗しました: {e}")
        return None

# ファイルを読み込んで置換を実施する関数定義
def replace_5_comment(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = html_5_comment_index_generate(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_comment_indexの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 5-ICON-START-{index} -->
# 置換を定義する関数
def define_5_icon_index(df,index): 
    # 性別の数値を文字列に変換
    gender_mapping = {
        '1': '男性',
        '2': '女性'
    }
    gender_value = df.iloc[index, 4]  # '2. 回答者様の性別を教えて下さい'
    gender = gender_mapping.get(str(gender_value), '不明') # 数値が1または2でない場合は'不明'とする

    if gender == '男性':
        image_file = 'https://iminain.com/wp-content/uploads/2023/06/men-touka-2.png'
    else:
        image_file = 'https://iminain.com/wp-content/uploads/2023/06/women-touka-2.png'

    return image_file

    # image_fileを5-icon-{index}へと置換する


# ファイルを読み込んで置換を実施する関数定義
def replace_5_icon_index(html_template, df): 
    # DataFrameの各行に対してループを行う
    for index in df.index:
        # アイコンのファイル名を取得
        image_file = define_5_icon_index(df, index)

        replace_5_comment_index = f'<img decoding="async" loading="lazy"\nsrc="{image_file}" alt=""\nclass="wp-image-13148 luminous" style="width:90px;height:300px" width="90" height="300"\ndata-luminous="{image_file}">'

        # placeholder = fr'<!-- 5-{index}-ICON-START -->(.*?)<!-- 5-{index}-ICON-END -->'
        # if re.search(placeholder, html_template):
        #     print(f"Placeholder found for index {index}")
        # else:
        #     print(f"Placeholder not found for index {index}")

        html_template = re.sub(fr'<!-- 5-{index}-ICON-START -->(.*?)<!-- 5-{index}-ICON-END -->', replace_5_comment_index, html_template, flags=re.DOTALL)
        # 置換が成功したかどうかを確認
    if "<!-- 3-ICON-" in html_template:  # プレースホルダーがまだ存在するかどうかを確認
        print("置換に失敗しました。")
        return html_template

    print("3-ICONの置換が成功しました。")
    return html_template


# <!-- 5-{index}-PERIOD-START -->
# 置換を定義する関数
def define_5_period(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_5_period = row[11]

        pattern = f"<!-- 5-{index}-PERIOD-START -->(.*?)<!-- 5-{index}-PERIOD-END -->"
        replacement = f"<!-- 5-{index}-PERIOD-START -->{csv_data_5_period}<!-- 5-{index}-PERIOD-END -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_5_period(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_5_period(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_periodの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 5-{index}-SATISFACTION-START -->
# 置換を定義する関数
def define_5_satisfaction(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_5_period = row[9]

        pattern = f"<!-- 5-{index}-SATISFACTION-START -->(.*?)<!-- 5-{index}-SATISFACTION-END -->"
        replacement = f"<!-- 5-{index}-SATISFACTION-START -->{csv_data_5_period}<!-- 5-{index}-SATISFACTION-END -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_5_satisfaction(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_5_satisfaction(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_satisfactionの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 5-{index}-AGE-START -->
# 置換を定義する関数
def define_5_age(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_5_age = row[7]

        pattern = f"<!-- 5-{index}-AGE-START -->(.*?)<!-- 5-{index}-AGE-END -->"
        replacement = f"<!-- 5-{index}-AGE-START -->{csv_data_5_age}<!-- 5-{index}-AGE-END -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_5_age(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_5_age(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_ageの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 5-{index}-GENDER-START -->
# 置換を定義する関数
def define_5_gender(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_5_gender = row[5]

        pattern = f"<!-- 5-{index}-GENDER-START -->(.*?)<!-- 5-{index}-GENDER-END -->"
        replacement = f"<!-- 5-{index}-GENDER-START -->{csv_data_5_gender}<!-- 5-{index}-GENDER-END -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_5_gender(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_5_gender(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_genderの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 5-{index}-COMMENT1-START -->
# 置換を定義する関数
def define_5_comment1(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_5_comment = row[18]  # '12. 水素水を使ったことで何か変わりましたか？'
        first_sentence = csv_data_5_comment.split('。')[0] + '。'

        pattern = f"<!-- 5-{index}-COMMENT1-START -->(.*?)<!-- 5-{index}-COMMENT1-END -->"
        replacement = f"<!-- 5-{index}-COMMENT1-START -->{first_sentence}<!-- 5-{index}-COMMENT1-END -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_5_comment1(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_5_comment1(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_comment1の置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 5-{index}-COMMENT2-START -->
# 置換を定義する関数
def define_5_comment2(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_5_comment = row[18]  # '12. 水素水を使ったことで何か変わりましたか？'
        sentences = csv_data_5_comment.split('。')[1:]
        next_sentence_list = [sentence + '。' for sentence in sentences if sentence]
        joined_sentences = ''.join(next_sentence_list)


        pattern = f"<!-- 5-{index}-COMMENT2-START -->(.*?)<!-- 5-{index}-COMMENT2-END -->"
        replacement = f"<!-- 5-{index}-COMMENT2-START -->{joined_sentences}<!-- 5-{index}-COMMENT2-END -->"
        updated_html = re.sub(pattern, replacement, updated_html)
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_5_comment2(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_5_comment2(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("5_comment2の置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す


# <!-- 6-TEMPLATE_START -->
# 置換を定義する関数
def html_6_red_template_generate(html_template, df):
    try:
        index_count = len(df)

        new_template_parts_list = [
            f'''<!-- wp:list-item -->\n<li><a href="#kouka-{index+1}"<!-- 6-{index}-RED-START -->簡単に綺麗を保てる<!-- 6-{index}-RED-END --></a></li>\n<!-- /wp:list-item -->'''
            for index in range(index_count)
        ]
        
        # すべての新しいセクションを一つの文字列に連結
        html_insert_6_red_template = '\n\n'.join(new_template_parts_list)

        # 連結した文字列をHTMLテンプレートと置換
        updated_html_6_red_template = re.sub(r'<!-- 6-RED-TEMPLATE-START -->(.*?)<!-- 6-RED-TEMPLATE-END -->', html_insert_6_red_template, html_template, flags=re.DOTALL)
        
        return updated_html_6_red_template
    except Exception as e: # もし失敗したら
        print(f"6_red_indexの置換生成に失敗しました: {e}")
        return None


# ファイルを読み込んで置換を実施する関数定義
def replace_6_red_template(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = html_6_red_template_generate(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("6_red_templateの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す



# <!-- 6-RED -->
# 置換を定義する関数
def define_6_red(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_6_red = row[16]  # '10. 前問で答えた体験談のメリットを「一言」で言い表してください'
        cleaned_comment = re.sub('、|。|\n', '', csv_data_6_red)  # デリミタでクリーニング

        pattern = f'<!-- 6-{index}-RED-START -->(.*?)<!-- 6-{index}-RED-END -->'

        replacement = f'<!-- 6-{index}-RED-START -->{cleaned_comment}<!-- 6-{index}-RED-END -->'

        updated_html = re.sub(pattern, replacement, updated_html)
        
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_6_red(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_6_red(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("6_redの置換が成功しました。")
    return html_insert


# <!-- 6-2-TEMPLATE_START -->
# 置換を定義する関数
def html_6_blue_template_generate(html_template, df):
    try:
        index_count = len(df)
        print(f"index_count: {index_count}")

        new_template_parts_list = [
            f'''<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading" id="kouka-{index+1}"><!-- 6-BLUE-H3-{index}-START -->簡単に綺麗を保てる<!-- 6-BLUE-H3-{index}-END --></h3>\n<!-- /wp:heading -->\n\n<!-- wp:loos/balloon {{"balloonID":"12"}} -->\n<p><!-- 6-BLUE-SPEECH-{index}-START -->とにかく簡単で安く、綺麗になれることです。<!-- 6-BLUE-SPEECH-{index}-END --></p>\n<!-- /wp:loos/balloon -->\n\n<!-- 6-BLUE-COMMENT-{index}-START -->色々な商品を試しましたが、体の内側からよくなり、健康を保ちながら、美しくなっていくというのは、この水素水以外は、まだ経験したことがありません。<!-- 6-BLUE-COMMENT-{index}-END -->'''
            for index in range(index_count)
        ]
        
        # すべての新しいセクションを一つの文字列に連結
        html_insert_6_blue_template = '\n\n'.join(new_template_parts_list)

        # 連結した文字列をHTMLテンプレートと置換
        updated_html_6_blue_template = re.sub(r'<!-- 6-2-TEMPLATE-START -->(.*?)<!-- 6-2-TEMPLATE-END -->', html_insert_6_blue_template, html_template, flags=re.DOTALL)
        
        return updated_html_6_blue_template
    except Exception as e: # もし失敗したら
        print(f"6_blue_indexの置換生成に失敗しました: {e}")
        return None


# ファイルを読み込んで置換を実施する関数定義
def replace_6_blue_template(html_template, df): 
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = html_6_blue_template_generate(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("6_blue_templateの置換が成功しました。")
    return html_insert # この行で更新されたHTMLテンプレートを返す



# <!-- 6-BLUE-H3-{index}-START -->
def define_6_blue_h3(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_6_blue_h3 = row[16]  # '10. 前問で答えた体験談のメリットを「一言」で言い表してください'
        cleaned_comment = re.sub('、|。|\n', '', csv_data_6_blue_h3)  # デリミタでクリーニング

        pattern = f'<!-- 6-BLUE-H3-{index}-START -->(.*?)<!-- 6-BLUE-H3-{index}-END -->'

        replacement = f'<!-- 6-BLUE-H3-{index}-START -->{cleaned_comment}<!-- 6-BLUE-H3-{index}-END -->'

        updated_html = re.sub(pattern, replacement, updated_html)
        
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_6_blue_h3(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_6_blue_h3(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("6_blue_h3の置換が成功しました。")
    return html_insert


# <!-- 6-BLUE—ICON-{index}-START -->
# 置換を定義する関数
def define_6_blue_icon(df,index): 
    # 性別の数値を文字列に変換
    gender_mapping = {
        '1': '男性',
        '2': '女性'
    }
    gender_value = df.iloc[index, 4] # 2. 回答者様の性別を教えて下さい
    gender = gender_mapping.get(str(gender_value), '不明') # 数値が1または2でない場合は'不明'とする

    age_group_value = df.iloc[index, 6] #'3. 回答者様の年齢を教えて下さい'

    # 年齢層を40代以上と40代未満に分ける
    age_40_or_above = int(age_group_value) >= 4

    if gender == '男性':
        if age_40_or_above:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/men-2-150x150.png'
        else:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/men-1-150x150.png'
    else:
        if age_40_or_above:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/icon-6-150x150.png'
        else:
            image_file = 'https://iminain.com/wp-content/uploads/2023/06/icon-5-150x150.png'

    return image_file


# ファイルを読み込んで置換を実施する関数定義
def replace_6_blue_icon(html_template, df): 
    # DataFrameの各行に対してループを行う
    for index in df.index:
        # アイコンのファイル名を取得
        image_file = define_6_blue_icon(df, index)


        replace_6_blue_icon = f'<div class="c-balloon__icon -circle"><img decoding="async" loading="lazy" src="{image_file}" alt="" class="c-balloon__iconImg" width="80px" height="80px">'

        html_template = re.sub(fr'<!-- 6-BLUE—ICON-{index}-START -->(.*?)<!-- 6-BLUE-ICON-{index}-END -->', replace_6_blue_icon, html_template, flags=re.DOTALL)
        
        
    # 置換が成功したかどうかを確認
    if "<!-- 6-BLUE—ICON-" in html_template:  # プレースホルダーがまだ存在するかどうかを確認
        print("置換に失敗しました。")
        return html_template

    print("6-BLUE—ICONの置換が成功しました。")
    return html_template



# <!-- 6-BLUE-SPEECH-{index}-START -->
def define_6_blue_speech(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_6_blue_speech = row[15]  # '9. 前問で答えたメリットを体験談を交えて詳しく教えて下さい'
        csv_split_list = re.split('。|\n', csv_data_6_blue_speech)
        first_element = csv_split_list[0]

        pattern = f'<!-- 6-BLUE-SPEECH-{index}-START -->(.*?)<!-- 6-BLUE-SPEECH-{index}-END -->'

        replacement = f'<!-- 6-BLUE-SPEECH-{index}-START -->{first_element}<!-- 6-BLUE-SPEECH-{index}-END -->'

        updated_html = re.sub(pattern, replacement, updated_html)
        
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_6_blue_speech(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_6_blue_speech(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("6_blue_speechの置換が成功しました。")
    return html_insert


# <!-- 6-BLUE-COMMENT-{index}-START -->
def define_6_blue_comment(html_template, df):
    updated_html = html_template
    for index, row in df.iterrows():
        csv_data_6_blue_comment = row[15]  # '9. 前問で答えたメリットを体験談を交えて詳しく教えて下さい'
        csv_split_list = re.split('。|\n', csv_data_6_blue_comment)
        next_elements = csv_split_list[1:]
        
        # 各要素の最後に「。」を追加
        csv_split_list = [item + '。' if not item.endswith('。') else item for item in next_elements if item.strip()]
                
        # 各要素を<p>タグで囲む
        join_list = '\n\n'.join([f'<!-- wp:paragraph -->\n<p>{item}</p>\n<!-- /wp:paragraph -->' for item in csv_split_list if item.strip()])  # if item.strip()を追加して、空白のみの要素や空の要素を無視

        pattern = f'<!-- 6-BLUE-COMMENT-{index}-START -->(.*?)<!-- 6-BLUE-COMMENT-{index}-END -->'

        replacement = f'<!-- 6-BLUE-COMMENT-{index}-START -->{join_list}<!-- 6-BLUE-COMMENT-{index}-END -->'
        updated_html = re.sub(pattern, replacement, updated_html)
        
    return updated_html


# ファイルを読み込んで置換を実施する関数定義
def replace_6_blue_comment(html_template, df):
    if df is None: # ファイルデータが読み込まれたか確認
        print("データフレームのロードに失敗しました。")
        return html_template
    
    html_insert = define_6_blue_comment(html_template, df)
    if html_insert is None:
        print("置換に失敗しました。")
        return html_template

    print("6_blue_commentの置換が成功しました。")
    return html_insert


# <!-- 7-RED -->
# 置換を定義する関数
def define_7_red(df): 
    try: # もし成功したら
        csv_data_7_red = df.iloc[0, 19]  # '13. どんな人におすすめですか？3つ教えてください'
        csv_split_list = re.split('、|。|\n', csv_data_7_red)
        csv_list_customize = ['「' + item + '」' for item in csv_split_list if item]
        csv_split_join = ''.join(csv_list_customize)
        html_insert_7_red = f'<p>特に{csv_split_join}におすすめです。'
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
        csv_data_7_blue = df.iloc[1:, 19].tolist()  # '13. どんな人におすすめですか？3つ教えてください'
        csv_split_list = []
        for item in csv_data_7_blue:
            csv_split_list.extend(re.split('、|。|\n', str(item)))
        csv_list_customize = ['<!-- wp:list-item -->\n<li>' + item + '</li>\n<!-- /wp:list-item -->' for item in csv_split_list if item]
        csv_split_join = '\n\n'.join(csv_list_customize)
        
        html_insert_7_blue = f'<ul class="is-style-check_list">{csv_split_join}</ul>'
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
        csv_data_8_red = df.iloc[0, 14]  # '8. 水素水のメリットを3つ教えてください'
        csv_split_list = re.split('、|。|\n', csv_data_8_red)
        csv_split_join = '、'.join(csv_split_list)
        html_insert_8_red = f'<p>XXXは{csv_split_join}のが魅力です。【意味ナイン】では、XXXは意味ないのか、意味あるのか調査し、評判やコメント、おすすめ代替案について紹介しています。'
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







# ------------実行処理----------------


# 削除実行処理
def delete_sections(html_template):
    html_template = deleteSection3_1(html_template)
    html_template = deleteSection3_2(html_template)
    html_template = deleteSection3_lastptag(html_template)
    html_template = deleteSection5_1(html_template)
    html_template = deleteSection6_1(html_template)
    html_template = deleteSection6_2(html_template)
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
    html_template = replace_3_comment_index(html_template, df)
    html_template = replace_3_ptag_index(html_template, df)
    html_template = replace_4_red(html_template, df)
    html_template = replace_4_blue(html_template, df)
    html_template = replace_5_comment(html_template, df)
    html_template = replace_5_icon_index(html_template, df)
    html_template = replace_5_period(html_template, df)
    html_template = replace_5_satisfaction(html_template, df)
    html_template = replace_5_comment1(html_template, df)
    html_template = replace_5_comment2(html_template, df)
    html_template = replace_5_age(html_template, df)
    html_template = replace_5_gender(html_template, df)
    html_template = replace_6_red_template(html_template, df)
    html_template = replace_6_blue_template(html_template, df)
    html_template = replace_6_red(html_template, df)
    html_template = replace_6_blue_h3(html_template, df)
    html_template = replace_6_blue_icon(html_template, df)
    html_template = replace_6_blue_speech(html_template, df)
    html_template = replace_6_blue_comment(html_template, df)
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
with open('NEW ﾌｧｲﾙWP.html', 'w', encoding='utf-8') as htmlfile:
    htmlfile.write(html_template)










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
        error_message = f"エラー: CSVファイルのｴﾝｺｰﾄﾞが違うため、読み込みに失敗しました。 - {e}"
        result_label.config(text=error_message, wraplength=200)
        return

    # main_functionを呼び出し
    # main_functionを呼び出し、結果を受け取る
    updated_html_template = main_function(html_template, df)


    # 置換後のHTMLをテキストウィジェットに表示
    with open('NEW ﾌｧｲﾙWP.html', 'r', encoding='utf-8') as htmlfile:
        html_template = htmlfile.read()

    # HTMLテンプレートをテキストウィジェットから取得
    html_template = text_widget.get("1.0", tk.END)


    # replace_XXX 関数を呼び出してテンプレートを置換
    XXX_change_html, message = replace_XXX(updated_html_template, specific_word)

    with open('NEW ﾌｧｲﾙWP.html', 'w', encoding='utf-8') as outfile:
        outfile.write(XXX_change_html)

    print(message)

    # 置換後のHTMLをテキストウィジェットに表示
    with open('NEW ﾌｧｲﾙWP.html', 'r', encoding='utf-8') as htmlfile:
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

def on_entry_click(event):
    if word_entry.get() == 'XXX':
        word_entry.delete(0, tk.END)
        word_entry.config(fg='black')

# Tkinterウィンドウを作成
root = tk.Tk()
root.title("CSV Selector")
root.geometry('600x400')

# ウィンドウを前面に持ってくる
root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)
root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

# グリッドで配置するフレーム
grid_frame = tk.Frame(root)
grid_frame.pack(pady=20)

# 空のラベルを追加して高さ設定
empty_label = tk.Label(grid_frame, height=2)  
empty_label.grid(row=0, column=0, columnspan=3)


# 特定ワードの入力フィールド
word_label = tk.Label(grid_frame, text='特定ワードを入力: ')
word_label.grid(row=1, column=0)
word_entry = tk.Entry(grid_frame, fg='grey')
word_entry.insert(0, 'XXX')
word_entry.bind('<FocusIn>', on_entry_click)
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


# モジュールを実行
generate_button = tk.Button(grid_frame, text="ファイル変換", command=run_file_change)
generate_button.grid(row=6, column=0, columnspan=3, pady=10)


# 結果を表示するラベル
result_label = tk.Label(grid_frame, text="")
result_label.grid(row=7, column=0, columnspan=3, pady=10)

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