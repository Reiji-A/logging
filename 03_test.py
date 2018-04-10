import logging

detail_formatting = "%(relativeCreated)08d[ms] - %(name)s - %(levelname)s - %(processName)-10s - %(threadName)s -\n*** %(message)s"

# ファイルの設定、logは詳細に！！
logging.basicConfig(
    level = logging.DEBUG,
    format = detail_formatting,#出力のformatも変えられる
    filename = "./sample.log"#logファイルのあるか

# sys.stderrのloggerの設定
# http://docs.python-guide.org/en/latest/writing/logging/#example-configuration-directly-in-code も参考になる

# log出力先をsys.stderrに
console = logging.StreamHandler()
# 個別にformatの形式を変える
console_formatter = logging.Formatter("%(relativeCreated)07d[ms] : %(name)s : %(message)s")
console.setFormatter(console_formatter)
# sys.stderrにざっくりとしたerror情報INFOにする
console.setLevel(logging.INFO)
# consoleという設定logging設定ができたので、適用したいmoduleに対して、addHandlerにその設定を突っ込む
logging.getLogger("my_pac.mod01").addHandler(console)
# 複数のモジュールでlogを出したい場合はこうする(`複数のモジュールでlogを出したい`の例の通り)
# logging.getLogger("my_pac.mod02").addHandler(console)
