import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- グラフ描画前の設定 ---
plt.rcParams["lines.linewidth"] = 6  # 全ての線のデフォルトの太さを2.0に
plt.rcParams["xtick.labelsize"] = 24  # X軸の目盛りラベルサイズ
plt.rcParams["ytick.labelsize"] = 24  # Y軸の目盛りラベルサイズ
plt.rcParams["axes.labelweight"] = "bold"  # 軸ラベルの太さを太字に
# -------------------------


def sigmoid(x):

    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    """シグモイド関数の導関数"""
    s = sigmoid(x)
    return s * (1 - s)


def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    """ReLU関数の導関数"""
    # x > 0 の場合は 1
    # x <= 0 の場合は 0
    return np.where(x > 0, 1, 0)


def tanh(x):
    """
    双曲線正接関数 (Tanh function)
    """
    # np.exp() は e^x を計算します
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


def tanh_derivative(x):
    """
    双曲線正接関数の導関数 (Derivative of Tanh)
    """
    # 導関数は 1 - (tanh(x))^2 で表される
    t = tanh(x)
    return 1 - t**2


input_data = np.arange(-10.0, 10.0, 0.1)
output_data = tanh_derivative(input_data)
plt.plot(input_data, output_data)

# 現在のAxesオブジェクトを取得
ax = plt.gca()

# X軸の目盛りを 5.0 刻みに設定
ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

# x=0 の位置に垂直な補助線を入れる
plt.axvline(
    x=0,
    linestyle="--",  # 線の種類: 破線 (dashed)
    color="gray",  # 線の色: 黒
    linewidth=1,
)  # 線の太さ
plt.axhline(
    y=1,
    linestyle="--",  # 線の種類: 破線 (dashed)
    color="gray",  # 線の色: 黒
    linewidth=1,
)  # 線の太さ
plt.axhline(
    y=0,
    linestyle="--",  # 線の種類: 破線 (dashed)
    color="gray",  # 線の色: 黒
    linewidth=1,
)  # 線の太さ
# plt.axhline(
#    y=-1,
#    linestyle="--",  # 線の種類: 破線 (dashed)
#    color="gray",  # 線の色: 黒
#    linewidth=1,
# )  # 線の太さ

plt.savefig("my_plot.png")
