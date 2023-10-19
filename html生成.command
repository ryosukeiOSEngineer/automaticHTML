#!/bin/bash

# automaticHTMLディレクトリの検索
directory_path=$(find ~ -type d -name 'automaticHTML' 2>/dev/null)

# もしディレクトリが見つかったら
if [[ ! -z $directory_path ]]; then
    cd $directory_path

    # pyenvによって設定されたPythonのバージョンを取得
    current_version=$(pyenv version-name)

    # バージョンが3.10.8であるかどうかを確認
    if [ "$current_version" == "3.10.8" ]; then
        echo "現在のPythonバージョンは3.10.8です。処理を続行します。"
        
        # 依存関係のインストール
        pip install -r requirements.txt

        # Pythonスクリプトの実行
        open -a "Python Launcher" "$directory_path/TwoUpdateMain.py"
    else
        echo "Pythonバージョンが3.10.8ではありません。現在のバージョン: $current_version"
        exit 1  # エラーで終了
    fi
else
    echo "automaticHTMLディレクトリが見つかりませんでした。"
    exit 1
fi
