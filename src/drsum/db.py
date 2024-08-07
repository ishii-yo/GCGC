"""
Dr.Sumと接続するためのモジュール
"""
import os
import subprocess
import ea_py3.dbi.dbi_connection as dbi_con  # type: ignore


def dump_gc_log(output_path: str, conn: dict, exp: str = "") -> None:
    """
    gcログをダンプする
    """
    sql = "select gc_log from log_gc_log;"
    if exp:
        sql = f"select gc_log from log_gc_log where {exp};"
    # with open(output_path, "w", encoding='utf8', newline='') as f:
    #     for line in select(conn, sql):
    #         f.write(line[0] + '\n')
    # FIXME: ea_py3を使うと、'のエスケープがうまくいかないため、dwtab_export_csv.batを使ってエクスポートする。
    export_csv(conn['server'], str(conn['port']), conn['user'], conn['pwd'], conn['db'],
               sql, os.path.dirname(output_path), os.path.basename(output_path))


def export_csv(host: str, port: str, user_id: str, password: str,
               db: str, sql: str, csv_path: str, csv_name: str) -> None:
    """
    データのエクスポート
    """
    bat_path = os.path.join(os.environ['DWODS57_TOOLS_PATH'], 'cmd', 'JPN', 'dwtab_export_csv.bat')

    export_args = [bat_path, host, port, user_id, password,
                   db, sql, csv_path, csv_name, '0', ',', 'utf8', '0', '1']

    # subprocess.run(export_args, check=True)  # 失敗時は例外を出力
    # FIXME: 引数に","が含まれるとエラーになるため、以下の呼び出し方で実行する。
    args = [f'"{arg}"' for arg in export_args]
    subprocess.run(' '.join(args), shell=True, check=True)


def select(conn: dict, sql: str):
    """
    select
    """
    with dbi_con.connect(**conn) as con:
        cur = con.cursor()
        cur.execute(sql)
        for row in cur.fetchall():
            yield row
