import logging

# my_package.my_moduleのみに絞ってsys.stderrにログを出す
logging.basicConfig() # 最初に呼び出しが必要 defaultはlevel=logging.WARNING
logging.getLogger("my_pac.mod01").setLevel(level=logging.INFO)

"""
このように指定することで、
logging.INFO以上(logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
のレベルに当てはまるlogがmy_package.my_moduleに関して出力されます。
(setLevelにlogging.DEBUGを指定すれば、logging.DEBUGのものも出力)
"""
