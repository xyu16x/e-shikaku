import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 日本語フォントを指定（例：IPAexGothic）

plt.rcParams["font.family"] = "IPAexGothic"


# シグモイド関数
def sigmoid(x, a):
    return 1 / (1 + np.exp(-a * x))


# x の範囲
x = np.linspace(-10, 10, 400)

# 比較する a の値
a_values = [0.2, 0.5, 1, 10]

plt.figure(figsize=(8, 5))

for a in a_values:
    y = sigmoid(x, a)
    plt.plot(x, y, label=f"a = {a}")

plt.title("sigmoid")
plt.xlabel("x")
plt.ylabel("σ(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("sigmoid.png")
