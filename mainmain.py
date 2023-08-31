def generate_html_content(file_path):
    specific_word = word_entry.get()
    df = pd.read_csv(file_path)

    url = 'https://iminain.com/%e3%80%90%e5%a4%89%e6%95%b0ver%e3%80%91%e7%b4%a0%e6%b0%b4%e3%81%af%e6%84%8f%e5%91%b3%e3%81%aa%e3%81%84%ef%bc%9f%e6%84%8f%e5%91%b3%e3%81%82%e3%82%8b%ef%bc%9f%e8%a9%95%e5%88%a4%e3%81%a8%e3%81%8a/'

    # fetch_html_templateでhtml_templateを初期化
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
    html_template = loop_and_replace_experiences(html_template)

    # 置換処理実施
    html_template = replace_placeholders(html_template, df)



    return html_template
