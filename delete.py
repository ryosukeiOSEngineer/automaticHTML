from bs4 import BeautifulSoup

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


# ６-青 クラスの2番目以降を削除
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

