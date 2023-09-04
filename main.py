import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import requests
from bs4 import BeautifulSoup


# HTMLテンプレートの取得
def fetch_html_template(url, specific_word):
    response = requests.get(url)
    if response.status_code != 200:
        return "特定のサイトを読み込むことができませんでした。"
    html_template = response.text
    return html_template.replace('XXX', specific_word)


# 特定のワードの置換
def replace_specific_word(html_template, specific_word):
    return html_template.replace('XXX', specific_word)


#------------------------------------------------------------

# *******************削除部分の関数定義*********************

# ３-赤 2〜4目のボタンタグを削除
def remove_3_red_buttons(html_template):
    soup = BeautifulSoup(html_template, 'html.parser')

    # 削除したいボタンの内容
    buttons_to_remove = [
        "健康には欠かせない水",
        "アンチエイジング効果がある",
        "どんなことにも効果がある水"
    ]

    # 一致するボタンを削除
    for button_text in buttons_to_remove:
        button = soup.find('button', string=button_text)
        if button:
            button.decompose()

    return str(soup)


# 3-赤 6-赤 2〜４アイコンと吹き出し部分削除
def remove_3_and_6_elements(html_content, indices):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all('div', class_='c-balloon -bln-left')
    for index in sorted(indices, reverse=True):
        elements[index].decompose()
    return str(soup)


# ３-赤の2〜４目タグに付属してるものを削除
def remove_3_to_red_tabs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 削除したいIDのリスト
    ids_to_remove = ['tab-6deac381-1', 'tab-6deac381-2', 'tab-6deac381-3']

    for div_id in ids_to_remove:
        div_to_remove = soup.find('div', id=div_id)
        if div_to_remove:
            div_to_remove.decompose() # 削除

    return str(soup)


# 5-2枚目以降の削除
def remove_5_2_after_divs(html_content):
    """
    'swell-block-balloon'クラスを持つ<div>要素の中で、最初の要素以外をすべて削除する関数。
    
    Args:
    - html_content (str): 処理対象のHTMLコンテンツ。

    Returns:
    - str: 処理後のHTMLコンテンツ。
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # クラス名'swell-block-balloon'を持つすべての<div>要素を選択
    divs_to_remove = soup.find_all('div', class_='swell-block-balloon')

    # 2つ目以降の要素を削除
    for div_to_remove in divs_to_remove[1:]:
        div_to_remove.decompose() # 削除

    return str(soup)


# 5の2つ目のpタグ除去
def remove_5_2_after_p():
    """
    'html_template5_p' に含まれる特定の内容を持つ <p> タグを削除する関数。

    Returns:
    - str: 処理後のHTMLコンテンツ。
    """
    html_template5_p = '''<p><mark style="background-color:rgba(0, 0, 0, 0);color:#6d3a00" class="has-inline-color">便秘に悩まされていたので、どうしたらいいのか、色々調べていくうちに水素水に辿り着きました。飲んで1週間くらいは何もかわらなかったのですが、2週間目から、腸の調子がよくなり、便秘がなおりました。それと同時に肌荒れも改善されました。今はツヤツヤお肌をキープしてます。</mark></p>'''
    soup = BeautifulSoup(html_template5_p, 'html.parser')

    # 削除したい内容と一致するpタグを取得
    target_content = '便秘に悩まされていたので、どうしたらいいのか、色々調べていくうちに水素水に辿り着きました。飲んで1週間くらいは何もかわらなかったのですが、2週間目から、腸の調子がよくなり、便秘がなおりました。それと同時に肌荒れも改善されました。今はツヤツヤお肌をキープしてます。'
    target_p = soup.find('p', string=target_content)

    # タグを削除
    if target_p:
        target_p.decompose()

    return str(soup)


# 6-<h3>タグの2〜4までを削除
def remove_6_blue_h3():
    """
    'html_template6_h3' に含まれる特定のID属性を持つ <h3> タグを削除する関数。

    Returns:
    - str: 処理後のHTMLコンテンツ。
    """
    html_template6_h3 = '''<h3 class="wp-block-heading" id="kouka-1">何かのテキスト</h3>
                <h3 class="wp-block-heading" id="kouka-2">家族みんなで楽しめる</h3>
                <h3 class="wp-block-heading" id="kouka-3">飲むだけでアンチエイジングできる</h3>
                <h3 class="wp-block-heading" id="kouka-4">ダイエットにオススメ</h3>
                <h3 class="wp-block-heading" id="kouka-5">その他のテキスト</h3>'''
    soup = BeautifulSoup(html_template6_h3, 'html.parser')

    # 削除したいid属性をリストに格納
    ids_to_remove = ['kouka-2', 'kouka-3', 'kouka-4']

    # id属性で検索して削除
    for id_to_remove in ids_to_remove:
        tag_to_remove = soup.find('h3', id=id_to_remove)
        if tag_to_remove:
            tag_to_remove.decompose()

    return str(soup)


# ６-青 'swell-block-balloon'クラスの2番目以降を削除
def remove_6_to_blue_divs(html_content):
    """
    'swell-block-balloon'クラスを持つ<div>要素の中で、最初の要素以外をすべて削除する関数。
    
    Args:
    - html_content (str): 処理対象のHTMLコンテンツ。

    Returns:
    - str: 処理後のHTMLコンテンツ。
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # クラス名'swell-block-balloon'を持つすべての<div>要素を選択
    divs_to_remove = soup.find_all('div', class_='swell-block-balloon')

    # 2つ目以降の要素を削除
    for div_to_remove in divs_to_remove[1:]:
        div_to_remove.decompose() # 削除

    return str(soup)


# 6-青のpタグ削除
def remove_6_to_blue_p():
    """
    'html_template6_p' に含まれる特定のテキストを持つ <p> タグを削除する関数。

    Returns:
    - str: 処理後のHTMLコンテンツ。
    """
    html_template6_p = '''<p>こんなに簡単に綺麗になれるとは思いませんでした。</p>
                <p>色んな商品が売ってますが、水素水は、2週間くらい飲みつづければ、効果が期待できる素晴らしい商品です。</p>
                <p>私は美容のために愛飲していますが、パパは健康維持の一環として飲んでいます。</p>
                <p>ちなみに、子どもは学力向上のために飲んでいます。</p>
                <p>それぞれ飲む目的は違いますが、一緒に続けられるので購入がしやすいです。</p>
                <p>即効性はないのですが飲み続けていくうちに、夕方になると気になっていたむくみに改善が見られたり、肌にハリつやが戻るようになってきました、値段は高いですがそれだけの効果は実感できます。</p>
                <p>飲んでみた感想は飲みやすくて水のように飲めました。</p>
                <p>癖もないので飲みやすく、継続して続けることができました。</p>
                <p>もともと便秘薬もちで自分の体型に自信がなかったのですが、便秘に悩まなくなり、体重も少しずつ落ちていったので使って良かったです。</p>'''
    soup = BeautifulSoup(html_template6_p, 'html.parser')
    
    # 削除したいテキストを含む<p>タグを検索
    tags_to_remove = soup.find_all('p', string=['こんなに簡単に綺麗になれるとは思いませんでした。',
                                            '色んな商品が売ってますが、水素水は、2週間くらい飲みつづければ、効果が期待できる素晴らしい商品です。',
                                            '私は美容のために愛飲していますが、パパは健康維持の一環として飲んでいます。',
                                            'ちなみに、子どもは学力向上のために飲んでいます。',
                                            'それぞれ飲む目的は違いますが、一緒に続けられるので購入がしやすいです。',
                                            '即効性はないのですが飲み続けていくうちに、夕方になると気になっていたむくみに改善が見られたり、肌にハリつやが戻るようになってきました、値段は高いですがそれだけの効果は実感できます。',
                                            '飲んでみた感想は飲みやすくて水のように飲めました。',
                                            '癖もないので飲みやすく、継続して続けることができました。',
                                            'もともと便秘薬もちで自分の体型に自信がなかったのですが、便秘に悩まなくなり、体重も少しずつ落ちていったので使って良かったです。'])

    # 見つかったタグを削除
    for tag in tags_to_remove:
        tag.decompose()



# １から８を関数定義していく***********************


# **置換される場所の定義と置換フォーマット作成**
# １-赤
def get_merits1(df):
    merits_string = df['8. 水素水のメリットを3つ教えてください'].iloc[0]
    merits_list = merits_string.split('、') # カンマ部分を無くして文字列を分ける
    merits_formatted = '「' + '」「'.join(merits_list) + '」'# 「」で囲んで結合
    merits_html = f'<p>XXXは{merits_formatted}などが魅力です。</p>' # 新しく置換するもの
    return merits_html


# １-青
def get_merits2(df):
    merits_string = df['8. 水素水のメリットを3つ教えてください'].iloc[1]
    merits_list = merits_string.split('、') # カンマ部分を無くして文字列を分ける
    merits_formatted = '「' + '」「'.join(merits_list) + '」'# 「」で囲んで結合
    merits_html = f'<p>意味があるとされるおすすめポイントは{merits_formatted}などがあります。</p>' # 新しく置換するもの
    return merits_html


# １-緑
def get_merits3(df):
    merits_list = df['8. 水素水のメリットを3つ教えてください'].iloc[2:].tolist()
    merits_formatted = '\n'.join([f'<li>{merit}</li>' for merit in merits_list])
    merits_html = f'<ul class="is-style-check_list has-swl-pale-02-background-color has-background">\n{merits_formatted}\n</ul>'
    return merits_html


# ２-赤 merit_lst
def merit_lst(df):
    merits_string = df['13. どんな人におすすめですか？3つ教えてください'].iloc[0]
    merits_list = merits_string.split('、') # カンマを無くして文字列を分ける
    return merits_list


# ３-赤 タグ
def get_one_word_description(df):
    description_string = df.loc[0, '7. 前問で答えた内容を「一言」で言い表してください'].rstrip('。')
    description_html = f'<h3 class="wp-block-heading" id="kouka-1">{description_string}</h3>'
    return description_html


# ３-赤 コメント
def one_word_comments(df):
    comments_string = df.loc[0, '7. 前問で答えた内容を「一言」で言い表してください'].rstrip('。')
    comments_html = f'<div class="c-balloon__text"><p>{comments_string}</p><span class="c-balloon__shapes"><span class="c-balloon__before"></span><span class="c-balloon__after"></span></span></div>'
    return comments_html


# ３-赤 
def replace_p_content(html_template, df):
    # CSVからのデータを取得
    long_comment = df.loc[0, '6. 水素水を全く知らない人に説明してください（客観的に）※感想ではありません']
    
    # 「。」で改行してリストに変換
    long_comment_list = long_comment.replace('。', '。\n').split('\n')
    
    # リストの内容を一つの文字列に結合
    new_content = ''.join([f'<p>{sentence}</p>' for sentence in long_comment_list if sentence])
    
    # 例として、特定の内容を持つ<p>タグを探して置換
    old_content = '<p>水素水とは、体のサビを取り除き、体内を活性化させてくれるお水で、健康や美容に効果絶大なものになります。</p>'
    return html_template.replace(old_content, new_content)


# イラストを性別、年代で判定して置換
def one_word_comments_illustration(df, index):
    # 性別の数値を文字列に変換
    gender_mapping = {
        '1': '男性',
        '2': '女性'
    }
    gender_value = df.loc[index, '2. 回答者様の性別を教えて下さい']
    gender = gender_mapping.get(str(gender_value), '不明') # 数値が1または2でない場合は'不明'とする

    # 年齢層の数値を文字列に変換
    age_group_mapping = {
        '2': '20代',
        '3': '30代',
        '4': '40代',
        '5': '50代',
        '6': '60代',
        '7': '70代',
        '8': '80代'
    }
    age_group_value = df.loc[index, '3. 回答者様の年齢を教えて下さい']
    age_group = age_group_mapping.get(str(age_group_value), '不明') # 数値が2～8の範囲外の場合は'不明'とする

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


# ４-赤 Demerits
def get_demerits(df):
    demerits_string = df['11. 水素水のデメリットを3つ教えてください'].iloc[0] # 上から一番目を表示
    demerits_list = demerits_string.split('、') # カンマ部分を無くして文字列を分ける
    demerits_formatted = '「' + '」「'.join(demerits_list) + '」'# 「」で囲んで結合
    demerits_html = f'<p>意味があるとされるおすすめポイントは{demerits_formatted}などがあります。</p>' # 新しく置換するもの
    return demerits_html


# ４-青 demerits_lst
def demerit_lst(df):
    demerits_string = df['11. 水素水のデメリットを3つ教えてください'].iloc[1:] # インデックス[1]から全てを取得
    demerits_string = ''.join(demerits_string) # 文字列に結合
    demerits_list = demerits_string.replace('、', '').replace('。', '').split() # 「、」「。」を消して単語を区切る
    demerits_html = '<ul class="is-style-triangle_list">' + '\n'.join([f'<li>{item}</li>' for item in demerits_list]) + '</ul>' # 箇条書きにする
    return demerits_html


# ５ 指定されたHTML部分を特定する関数
def find_target_block(html_template):
    soup = BeautifulSoup(html_template, 'html.parser')
    target_div = soup.find('div', {'style': 'flex-basis:66.66%'})
    return target_div


# ５ 特定したHTML部分を置換する関数
def replace_target_block(target_div, data_row):
    # 満足度の部分を置換
    target_div.find('p').find('span').string = data_row['4. 満足度を教えてください。']
    
    # 年齢と性別の部分を置換
    target_div.find_all('p')[1].string = f"{data_row['3. 回答者様の年齢を教えて下さい']}・{data_row['2. 回答者様の性別を教えて下さい']}"
    
    # 期間の部分を置換
    target_p = target_div.find('p')
    current_text = target_p.decode_contents()  # HTMLの内容を取得
    period = data_row['5. 使用・利用期間を教えてください']
    new_text = f"期間：{period}<br>" + current_text.split('<br>')[1]
    target_p.clear()  # 現在の内容を削除
    target_p.append(new_text)  # 新しい内容を追加
    
    return target_div


# ５ 性別でイラストを置換する処理
def target_block_illustration(df, index):
    '''
    性別でイラストを置換する処理
    '''
    gender_mapping = {
        '1': '男性',
        '2': '女性'
        }
    gender_value = df.loc[index, '2. 回答者様の性別を教えて下さい']
    gender = gender_mapping.get(str(gender_value), '不明') # 数値が1または2でない場合は'不明'とする
    if gender == '男性':
        image_file = '口コミ男性アイコン.webp'
    else:
        image_file = '口コミ女性アイコン.webp'
    return image_file


# ５ pタグ  １行目「。」で改行
def target_experiences(df):
    '''
    pタグの置換する場所特定とﾌｫｰﾏｯﾄ設定
    '''
    target_experiences_string = df.loc[0, '7. 前問で答えた内容を「一言」で言い表してください']
    target_experiences_string_with_newline = target_experiences_string.replace('。', '。\n')
    target_experiences_html = f'<mark style="background-color:rgba(0, 0, 0, 0);color:#6d3a00" class="has-inline-color">{target_experiences_string_with_newline}</mark>'
    return target_experiences_html


# ５ 置換処理
def integrate_new_div(html_template, new_div, image_file, target_experiences_html):
    soup = BeautifulSoup(html_template, 'html.parser')
    
    # 既存のdivを特定して置換
    target_div = soup.find('div', {'style': 'flex-basis:66.66%'})
    target_div.replace_with(new_div)
    
    # 既存のイラストを特定して置換
    target_img = soup.find('img', {'class': 'wp-image-13148'})
    target_img['src'] = image_file  # 仮定：image_fileは新しい画像のURL
    
    # 既存のmarkタグを特定して置換
    target_mark = soup.find('mark', {'class': 'has-inline-color'})
    target_mark.replace_with(BeautifulSoup(target_experiences_html, 'html.parser'))
    
    return str(soup)


# ６-赤
def get_experiences_lst(df):
    experiences_lst = df['10. 前問で答えた体験談のメリットを「一言」で言い表してください'].iloc[0:].tolist()
    experiences_formatted = '\n'.join([f'<li><a href="#kouka-{index+1}" automate_uuid="some-uuid-{index+1}" data-nodal="">{merit}</a></li>' for index, merit in enumerate(experiences_lst)])
    experiences_html = f'<ul class="is-style-good_list">\n{experiences_formatted}\n</ul>'
    return experiences_html


# ６-h3
def get_h3_html_from_df(df, index):
    content = df.loc[index, '10. 前問で答えた体験談のメリットを「一言」で言い表してください']
    h3_html = f'<h3 class="wp-block-heading" id="kouka-1">{content}</h3>'
    return h3_html


# ６-アイコン選定
def get_image_file_from_df(df, index):
    # アイコンの選定
    age_group_value = df.loc[index, '3. 回答者様の年齢を教えて下さい']
    gender = df.loc[index, '2. 回答者様の性別を教えて下さい']
    age_40_or_above = int(age_group_value) >= 4
    if gender == '男性':
        image_file = 'タブ男性2アイコン.webp' if age_40_or_above else 'タブ男性アイコン.webp'
    else:
        image_file = 'タブ女性2アイコン.webp' if age_40_or_above else 'タブ女性アイコン.webp'
    
    # HTMLテンプレの場所特定とフォーマット
    new_img_tag = f'<img decoding="async" loading="lazy" src="https://iminain.com/wp-content/uploads/2023/06/{image_file}" alt="" class="c-balloon__iconImg" width="80px" height="80px">'
    
    return new_img_tag


# ６ ｺﾒﾝﾄ 
def get_6_comment(df, index):
    content = df.loc[index, '9. 前問で答えたメリットを体験談を交えて詳しく教えて下さい']
    sentences = content.split('。')
    first_ptag = f'<p>{sentences[0]}。</p>'
    p_html = f'<div class="c-balloon__text">{first_ptag}<span class="c-balloon__shapes"><span class="c-balloon__before"></span><span class="c-balloon__after"></span></span></div>'
    return p_html


# ６ 本文 2つ目から利用「。」で改行
def get_6_text(df, index):
    content = df.loc[index, '9. 前問で答えたメリットを体験談を交えて詳しく教えて下さい']
    sentences = content.split('。')
    p2_html_list = []  # 置換する文を保存するリスト
    for sentence in sentences[1:]:  # 最初の文をスキップ
        p2_html_list.append(f'<p>{sentence}。</p><br>')  # 新しく置換するもの
    p2_html = "".join(p2_html_list)  # リストを文字列に連結
    return p2_html


# ７-赤 recommend
def get_recommends(df):
    recommends_string = df['13. どんな人におすすめですか？3つ教えてください'].iloc[0] # 上から一番目を表示
    recommends_list = recommends_string.split('、') # カンマ部分を無くして文字列を分ける
    recommends_formatted = '「' + '」「'.join(recommends_list) + '」'# 「」で囲んで結合
    recommends_html = f'<p>意味があるとされるおすすめポイントは{recommends_formatted}などがあります。</p>' # 新しく置換するもの
    return recommends_html


# ７-青 recommend_lst
def recommends_lst(df):
    recommends_string = df['13. どんな人におすすめですか？3つ教えてください'].iloc[1]  # インデックス[1]から取得
    recommends_list = recommends_string.replace('。', '').split('、')  # 「、」「。」を消して単語を区切る
    recommends_html = '<ul class="is-style-check_list">\n' + '\n'.join([f'<li>{item}</li>' for item in recommends_list]) + '\n</ul>'
    return recommends_html


# ８-赤
def get_merits4(df):
    merits_string = df['8. 水素水のメリットを3つ教えてください'].iloc[0]
    merits_list = merits_string.split('、') # カンマ部分を無くして文字列を分ける
    merits_formatted = '「' + '」「'.join(merits_list) + '」'# 「」で囲んで結合
    merits_html = f'<p>XXXは安い、綺麗になる、健康的になるのが魅力です。【意味ナイン】では、XXXは意味ないのか、意味あるのか調査し、評判やコメント、おすすめ代替案について紹介しています。</p>' # 新しく置換するもの
    return merits_html


# -------------------------------------------------------------

# *****************検索部分の定義******************

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


# ３-1個目のタブ生成関数
# タブを生成した後にループ処理を行うため、ここに記載
def generate_tabs_from_csv(df, html_template):
    # タブのヘッダー部分を生成
    tab_headers = generate_tab_headers(df)
    
    # タブの内容部分を生成
    tab_contents = generate_tab_contents(df, html_template)
    
    # タブのヘッダーと内容を結合
    tabs_html = '<ul class="c-tabList" role="tablist">' + tab_headers + '</ul>' + tab_contents
    
    return tabs_html


# ----------------------------------------------------------
# ループ処理の関数


# ３ ループ処理
# タブのヘッダー部分を生成をループ処理
def generate_tab_headers(df):
    num_rows = len(df)
    tab_headers = []
    for i in range(num_rows):
        description = get_one_word_description(df)
        tab_headers.append(f'<li class="c-tabList__item" role="presentation"><button role="tab" class="c-tabList__button" aria-selected="false" aria-controls="tab-6deac381-{i}" data-onclick="tabControl">{description}</button></li>')
    return ''.join(tab_headers)


# ３ ループ処理
# タブの内容部分を生成するループ処理
def generate_tab_contents(df, html_template):
    num_rows = len(df)
    tab_contents = []
    for i in range(num_rows):
        content = replace_p_content(html_template, df.loc[i])
        image_file = one_word_comments_illustration(df, i)
        content = content.replace('<img src="placeholder_image.webp">', f'<img src="{image_file}">')
        comment_content = one_word_comments(df)
        content += comment_content
        tab_contents.append(content)
    return ''.join(tab_contents)


# ５ ループ処理
def process_all_rows(df, html_template):
    for index, row in df.iterrows():
        # 指定されたHTML部分を特定する関数処理
        target_div = find_target_block(html_template)
        # 特定したHTML部分を置換する関数処理
        new_div = replace_target_block(target_div, row)
        
        # イラストの置換
        image_file = target_block_illustration(df, index)
        
        # pタグの置換
        target_experiences_html = target_experiences(df)
        
        # html_templateにnew_divを統合する処理
        html_template = integrate_new_div(html_template, new_div, image_file, target_experiences_html)

    return html_template  # 更新されたhtml_templateを返す



# ６-青 h3 + ｲﾗｽﾄ + pﾀｸﾞ1行目 + pﾀｸﾞ2行目のﾙｰﾌﾟ
def generate_full_html(df, html_template):
    full_html = ""
    for index, row in df.iterrows():  # indexとrowを明示的に取得
        h3_html = get_h3_html_from_df(row)  # rowを渡す
        image_file = get_image_file_from_df(row)  # rowを渡す
        comment = get_6_comment(row)  # rowを渡す
        text = get_6_text(row)  # rowを渡す
        full_html += f"{h3_html}\n{image_file}\n{comment}\n{text}\n"
    
    if "{content}" in html_template:  # プレースホルダーが存在するか確認
        final_html = html_template.format(content=full_html)
    else:
        final_html = html_template + full_html  # プレースホルダーがない場合は、単に追加
    
    return final_html




# ----------------------------------------------------------

# 置換処理実施
def link_generator(ec_site, xxx):
    functions = {
        'amazon': amazon_search,
        'rakuten': rakuten_search,
        'google': google_search,
        'cinii': cinii_search,
        'jstage': jstage_search,
        'IRDB': IRDB_search,
    }
    
    if ec_site not in functions:
        raise ValueError(f"{ec_site} は、なにかしらの理由で表示できません。")

    return functions[ec_site](xxx)

# 置換処理実施
def replace_placeholders(html_template, df):
    def replace_merit_list(merits):
        return '\n'.join([f'<li>{merit}</li>' for merit in merits])
    
    placeholders_mapping = {
        # １-赤
        '<p>XXXは「安い」「綺麗になる」「健康的になる」などが魅力です。</p>': (get_merits1, {}),
        
        # １-青
        '<p>意味があるとされるおすすめポイントは「美肌になれる」「飲みやすい」「誰でも飲める」などがあります。</p>': (get_merits2, {}),
        

        # １-緑
        '<ul class="is-style-check_list has-swl-pale-02-background-color has-background">\n<li>活性酵素を除去してくれる</li>\n<li>変な味はしないので一般的な飲料として飲める</li>\n<li>アンチエイジング効果がある</li>\n<li>ダイエット効果がある</li>\n<li>美肌効果がある</li>\n<li>便秘が解消される</li>\n</ul>': (get_merits3, {}),
        
        # ２-赤
        '<ul class="is-style-check_list">': (merit_lst, {'post_process': replace_merit_list}),
        
        # ３-赤 タブ
        '<button role="tab" class="c-tabList__button" aria-selected="true" aria-controls="tab-6deac381-0" data-onclick="tabControl">体内の活性化</button>': (get_one_word_description, {'wrapper': '<button role="tab" class="c-tabList__button" aria-selected="true" aria-controls="tab-6deac381-0" data-onclick="tabControl">{}</button>'}),
        
        # ４-青
        '<ul class="is-style-triangle_list">\n<li>価格が高い</li>\n</ul>': (demerit_lst, {}),
        
        # ４-赤
        '<p>意味ない理由として「怪しい」「個人差がありすぎる」「理解するまで時間がかかる」などのコメントがありました。</p>':(get_demerits, {}),
        
        # ６-赤
        '<ul class="is-style-good_list">\n<li><a href="#kouka-1" automate_uuid="d3495264-e1e1-4675-84cb-c872e762cc7d" data-nodal="">簡単に綺麗を保てる</a></li>\n<li><a href="#kouka-2" automate_uuid="3087e4ad-8612-461b-a0fc-6ff92220ce85" data-nodal="">家族みんなで楽しめる</a></li>\n<li><a href="#kouka-3" automate_uuid="9740b60d-80c7-4676-8755-257f3bae9e4a" data-nodal="">飲むだけでアンチエイジングできる</a></li>\n<li><a href="#kouka-4" automate_uuid="a246317f-35a5-40a4-95fe-3819e40e41f0" data-nodal="">ダイエットにオススメ</a></li>\n</ul>': (get_experiences_lst, {}),
        
        # ７-赤
        '<p>特に「便秘気味な人」「手軽に美を手に入れたい人」「安さを求める人」におすすめです。</p>':(get_recommends, {}),

        # ７-青
        '<ul class="is-style-check_list">\n<li>家族みんなで健康に取り組みたい人</li>\n<li>アンチエイジングに興味のある人</li>\n<li>健康志向の人</li>\n<li>健康に値段がかけられる人</li>\n<li>アンチエイジング効果を求めている人</li>\n<li>お水に値段がかけられる人</li>\n<li>ダイエットしたい人</li>\n<li>健康に気を使っている人</li>\n<li>便秘の人</li>\n</ul>':(recommends_lst, {}),

        # ８-赤
        '<p>XXXは安い、綺麗になる、健康的になるのが魅力です。【意味ナイン】では、XXXは意味ないのか、意味あるのか調査し、評判やコメント、おすすめ代替案について紹介しています。</p>':(get_merits2, {}),

    }

    
    for placeholder, (func, args) in placeholders_mapping.items():
        # 関数の存在の確認
        if not callable(func):
            raise ValueError(f"Function {func} is not callable or not defined.")

        # プレースホルダの存在の確認
        if placeholder not in html_template:
            raise ValueError(f"Placeholder {placeholder} not found in the template.")

        # 関数の実行中のエラー
        try:
            html_content = func(df, **args)
            # ここで置換処理を行う
            html_template = html_template.replace(placeholder, html_content)
        except Exception as e:
            raise RuntimeError(f"Error executing function {func}: {str(e)}")

        # 'args'の適切なキーの確認
        if 'post_process' in args and not callable(args['post_process']):
            raise ValueError(f"'post_process' in args is not callable.")
        
    return html_template





# メイン関数の前にやらないとcsvﾌｧｲﾙを読み込めない
def browse_file():
    '''
    GUIでcsvファイルを選択して置換するためのデータを読み込む 
    '''
    file_path = filedialog.askopenfilename(filetypes=[('CSVファイル', '*.csv')])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)



#----------------------------------------------------------

# メイン関数*********************

# csvファイルの読み込み
def generate_html_content(file_path):
    specific_word = word_entry.get()
    df = pd.read_csv(file_path)

    url = 'https://iminain.com/%e3%80%90%e5%a4%89%e6%95%b0ver%e3%80%91%e7%b4%a0%e6%b0%b4%e3%81%af%e6%84%8f%e5%91%b3%e3%81%aa%e3%81%84%ef%bc%9f%e6%84%8f%e5%91%b3%e3%81%82%e3%82%8b%ef%bc%9f%e8%a9%95%e5%88%a4%e3%81%a8%e3%81%8a/'

    # fetch_html_templateでhtml_templateを初期化 
    # URLから取得したHTMLから変数「xxx」に代入されたもの一番最初の部分
    html_template = fetch_html_template(url, specific_word)
    if not html_template:
        return "URLからHTMLを取得できませんでした"

    # メイン関数に削除を処理する関数を反映
    html_template = remove_3_red_buttons(html_template)

    # strip_3_and_6_elementsのクラスの削除するインデックス
    indices_to_strip = [1, 2, 3, 5, 6, 7] 
    # 3-赤 2〜4目のボタンタグを削除
    html_template = remove_3_and_6_elements(html_template, indices_to_strip)

    # 3-赤の2〜4目タグに付属してるものを削除
    html_template = remove_3_to_red_tabs(html_template)

    # 5-2枚目以降の削除
    html_template = remove_5_2_after_divs(html_template)

    # 5の2つ目のpタグ除去
    html_template = remove_5_2_after_p(html_template)

    # 6-<h3>タグの2〜4までを削除
    html_template = remove_6_blue_h3(html_template)

    # 6-青 クラスの2番目以降を削除
    html_template = remove_6_to_blue_divs(html_template)

    # 6-青のpタグ削除
    html_template = remove_6_to_blue_p(html_template)


    # メイン関数にループ処理を反映
    html_template = process_all_rows(html_template)
    html_template = generate_full_html(html_template)
        # メイン関数にループ処理を反映
    html_template = process_all_rows(html_template)
    
    # generate_full_html関数でさらにhtml_templateがどのように変更されるかを確認
    html_template = generate_full_html(df, html_template)

    # タブのHTMLを生成
    tabs_html = generate_tabs_from_csv(df, html_template)

    # 生成したタブのHTMLをhtml_templateに追加（チェーン処理）
    html_template += tabs_html

    # 置換処理実施
    html_template = replace_placeholders(html_template, df)



    return html_template

# 新しい関数
def on_generate_button_click():
    file_path = file_entry.get()
    specific_word = word_entry.get()
    
    if not file_path or file_path == 'ファイルを選択してください':
        result_label.config(text="エラー: ファイルが選択されていません")
        return
    
    if not specific_word:
        result_label.config(text="エラー: 特定のワードが入力されていません")
        return

    try:
        html_content = generate_html_content(file_path)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, html_content)
    except Exception as e:
        result_label.config(text=f"エラー: {e}")



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
# text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll_y = ttk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=text_widget.xview)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

text_widget.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

root.mainloop()