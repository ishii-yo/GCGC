# GCGCの使い方

## 本ツールについて

- JavaのGCログ解析ツール[apple/GCGC](https://github.com/apple/GCGC)をフォークしたもの
- 基本的な分析はGCGCの通り
- GCログの準備において、DrSumに格納しているデータを取り出せるようにしている

## 使い方

### 環境構築

venvを使う場合は仮想環境を作成する

```cmd
python -m venv .venv
.venv/scripts/activate
```

パッケージインストール

```cmd
pip install -r requirements.txt
```

DrSumからGCログのデータを取得する場合は、DrSumのコマンドラインツール等が使える環境が必要

`ea_py3`での取得も利用可能

### 使用

1.起動

```cmd
cd src/notebooks
jupyter notebook
```

2.`GCGC.ipynb`をコピーして使用開始

3.gcログの準備

- DrSumからGCを取得する場合は最初のセルで、接続情報、取得条件を記載しGCログをDBから取得する
- DBから取得しない場合は`gc_logs`の`path`で指しているパスに該当のGCログを配置する
- `gc_logs`には複数のログを設定し比較することも可能