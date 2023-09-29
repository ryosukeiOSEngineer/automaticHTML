#!/bin/bash

# Homebrewのインストール
which brew > /dev/null || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# pyenvのインストール
brew install pyenv || echo "pyenv is already installed."

# Python 3.10.8のインストール
pyenv versions | grep 3.10.8 || pyenv install 3.10.8

# automaticHTMLディレクトリの検索
directory_path=$(find ~ -type d -name 'automaticHTML' 2>/dev/null)

# もしディレクトリが見つかったら
if [[ ! -z $directory_path ]]; then
    # ディレクトリ固有のPythonバージョンの設定
    cd $directory_path
    pyenv local 3.10.8

    # pyenvによって設定されたPythonのバージョンを取得
    current_version=$(pyenv version-name)

    # バージョンが3.10.8であるかどうかを確認
    if [ "$current_version" == "3.10.8" ]; then
        echo "現在のPythonバージョンは3.10.8です。処理を続行します。"
        
        # 依存関係のインストール
        pip install -r requirements.txt

        # Pythonスクリプトの実行
        open -a "Python Launcher" "$directory_path/updateMain.py"
    else
        echo "Pythonバージョンが3.10.8ではありません。現在のバージョン: $current_version"
        exit 1  # エラーで終了
    fi
else
    echo "automaticHTMLディレクトリが見つかりませんでした。"
    exit 1
fi
