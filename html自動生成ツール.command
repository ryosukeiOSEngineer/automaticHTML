#!/bin/bash

# Homebrewのインストール (もし未インストールの場合)
which brew > /dev/null || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python 3.10.8のインストール
brew install python@3.10.8 || brew upgrade python@3.10.8

# pip3とpython3のパスを正確に指定する (Homebrewでのインストールに応じて適切なバージョンを使用する)
PIP_PATH=$(brew --prefix)/opt/python@3.10.8/bin/pip3
PYTHON_PATH=$(brew --prefix)/opt/python@3.10.8/bin/python3

$PIP_PATH install -r requirements.txt
$PYTHON_PATH updatemain.py
