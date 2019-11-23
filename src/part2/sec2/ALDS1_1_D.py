import math

def ALDS1_1_D():
    """
    ＜問題＞
    FX取引では、異なる国の通貨を交換することで為替差の利益を得ることができます。
    例えば、１ドル100円の時に 1000ドル買い、価格変動により 1ドル 108円になった時に売ると、
    (108円 − 100円) × 1000ドル = 8000円の利益を得ることができます。

    ある通貨について、時刻 t における価格 Rt (t=0,1,2,,,n−1)が入力として与えられるので、
    価格の差 Rj−Ri (ただし、j>i とする) の最大値を求めてください。

    ＜入力＞
    最初の行に整数 n が与えられます。続く n 行に整数 Rt (t=0,1,2,,,n−1) が順番に与えられます。


    ＜出力＞
    最大値を１行に出力してください。

    ＜制約＞
    2 ≤ n ≤ 200,000
    1 ≤ Rt ≤ 10^9
    """
    n = int(input())
    r_list = [int(input()) for _ in range(n)]
    max_v, min_v = -math.inf, r_list[0]
    for j in range(1,n):
        max_v = max_v if max_v > (r_list[j]-min_v) else (r_list[j]-min_v)
        min_v = r_list[j] if min_v > r_list[j] else min_v
    print(max_v)

def main():
    ALDS1_1_D()


if __name__ == '__main__':
    main()