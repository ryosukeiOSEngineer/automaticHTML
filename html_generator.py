# htmlの生成
# ライブラリのインポート
import pandas as pd

# CSVファイルの読み込み
def read_csv(file_path):
    return pd.read_csv(file_path)

# 特定の情報をCSVから取得するための関数を定義
def get_recommendations(df):
    return df['13. どんな人におすすめですか？3つ教えてください'].iloc[0].split('、')

def get_advantages(df):
    return df['8. 水素水のメリットを3つ教えてください'].iloc[0].split('、')

def get_check_list_items(df):
    return df['11. 水素水のデメリットを3つ教えてください'].iloc[0].split('、')


# ここからHTMLの生成
def generate_html(file_path):
    df = read_csv(file_path)
    
    # 定義した関数を代入
    recommendations = get_recommendations(df)
    advantages = get_advantages(df)
    check_list_items = get_check_list_items(df)
    
    
    html_content = '<html><head></head><body>'
    html_content += '<h1>水素水の詳細</h1>'
    html_content += '<h2>おすすめする人</h2>'
    html_content += '<ul>'
    for recommendation in recommendations:
        html_content += f'<li>{recommendation}</li>'
    html_content += '</ul>'
    
    html_content += '<h2>メリット</h2>'
    html_content += '<ul>'
    for advantage in advantages:
        html_content += f'<li>{advantage}</li>'
    html_content += '</ul>'
    
    html_content += '<h2>デメリット</h2>'
    html_content += '<ul>'
    for check_list_item in check_list_items:
        html_content += f'<li>{check_list_item}</li>'
    html_content += '</ul>'
    
    # 5つ目と6つ目の内容追加
    one_word_explanation = df['7. 前問で答えた内容を「一言」で言い表してください'].iloc[0]
    explanation = df['6. 水素水を全く知らない人に説明してください（客観的に）※感想ではありません'].iloc[0].replace('。', '。<br/>')
    
    html_content += f'<button role="tab" class="c-tabList__button" aria-selected="true" aria-controls="tab-6deac381-0" data-onclick="tabControl">体内の活性化</button>'
    html_content += f'<p>{one_word_explanation}</p>'
    html_content += f'<p>{explanation}</p>'
    
    # 7つ目の内容追加
    demerits = '、'.join(get_check_list_items(df))
    html_content += f'<p>意味ない理由として「{demerits}」などのコメントがありました。</p>'
    
    html_content += '</body></html>'
    
    with open('output.html', 'w') as file:
        file.write(html_content)

    return html_content

file_path = 'path/to/your/csvfile.csv'
html_content = generate_html(file_path)
print(html_content)
