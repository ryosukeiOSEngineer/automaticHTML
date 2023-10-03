#!/bin/bash

# Homebrewのインストール
which brew > /dev/null || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# pyenvのインストール
brew install pyenv || echo "pyenv is already installed."

# Python 3.10.8のインストール
pyenv versions | grep 3.10.8 || pyenv install 3.10.8

# automaticHTMLディレクトリの検索とPythonバージョンの設定
directory_path=$(find ~ -type d -name 'automaticHTML' 2>/dev/null)
if [[ ! -z $directory_path ]]; then
    cd $directory_path
    pyenv local 3.10.8
else
    echo "automaticHTMLディレクトリが見つかりませんでした。"
    exit 1
fi
