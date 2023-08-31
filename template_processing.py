import requests
from jinja2 import Template
import pandas as pd

def process_template(file_path, variable_name):
    # CSVデータの読み込み
    csv_data = pd.read_csv(file_path)

    # URLからHTMLを取得
    url = "https://iminain.com/%e3%80%90%e5%a4%89%e6%95%b0ver%e3%80%91%e7%b4%a0%e6%b0%b4%e3%81%af%e6%84%8f%e5%91%b3%e3%81%aa%e3%81%84%ef%bc%9f%e6%84%8f%e5%91%b3%e3%81%82%e3%82%8b%ef%bc%9f%e8%a9%95%e5%88%a4%e3%81%a8%e3%81%8a/"
    response = requests.get(url)
    html_content = response.text

    # Jinja2テンプレートとしてHTMLを読み込み
    template = Template(html_content)

    for index, row in csv_data.iterrows():
        data = {
            "name": row['name'],
            "age": row['age']
        }

        # データでテンプレートをレンダリング
        rendered_html = template.render(data)

        # レンダリングされたHTMLをファイルに保存
        with open(f'output_{index}.html', 'w') as file:
            file.write(rendered_html)

    print("HTML files generated successfully!")
