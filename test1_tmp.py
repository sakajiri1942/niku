def test(x):
    z = x * 10 + 1

    print('Hello World!')
    return z


if __name__ == '__main__':  # 直接yobareru.pyを実行した時だけ、def test()を実行する importしたときに実行しない効果がある時がある。
    test()

print('モジュール名：{}'.format(__name__))  # 実行したモジュール名を表示する
