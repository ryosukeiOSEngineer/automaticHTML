#!/bin/bash

# Homebrewのインストール
which brew > /dev/null || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# pyenvのインストール
brew install pyenv || echo "pyenv is already installed."

# Python 3.10.8のインストール
pyenv versions | grep 3.10.8 || pyenv install 3.10.8

# ディレクトリ固有のPythonバージョンの設定
cd /Users/coinlocker/Desktop/automaticHTML
pyenv local 3.10.8

# 依存関係のインストール
pip install -r requirements.txt

# Pythonスクリプトの実行
python updatemain.py


