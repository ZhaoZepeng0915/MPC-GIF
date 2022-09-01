import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

for i in range(0,7):
    k = i
    # 构造数据
    x = np.arange(1, 30)
    y1 = 5 * x ** 0
    # 初始化数据
    if k == 0:
        y2 = 10.39 - (5.5 * (np.exp(-0.5 * x) + 1.1) + 0.1 * np.sin(x)) + 0.03 * x
        y3 = [12, 10, 11, 10, 9.5, 11, 10, 9, 8, 10, 9, 7, 8, 7, 8, 6, 6,7, 6, 6,5, 6, 6, 6, 5,5, 5, 5, 5]
        y5 = []
        for t in range(0, 29):
            y5.append((40 - y3[t])*0.7)
            if t <15:
                y5[t] = y5[t]+0.6*t-8
    y4 = 10.39 - (5.5 * (np.exp(-0.5 * x) + 1.1) + 0.1 * np.sin(x)) + 0.03 * x
    for j in range(k,14):
        y2[15+j] = y2[15+j]+np.random.uniform(-0.03, 0.03)
        y3[15+j] = y3[15+j]+np.random.uniform(-0.5, 0.4)-0.15
        y5[15+j] = (40-y3[15+j])*0.7

    # 构造多个ax,twinx表示共享x轴
    fig, ax1 = plt.subplots(figsize=(9, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()
    ax5 = ax1.twinx()
    # 绘制
    img1, = ax1.plot(x, y1, c='tab:blue')
    img1, = ax1.plot(x, y1 + 0.15, c='tab:blue',linestyle='--',alpha=0.3)
    img1, = ax1.plot(x, y1 - 0.15, c='tab:blue',linestyle='--',alpha=0.3)
    img2, = ax2.plot(x[0:(16+k)], y2[0:(16+k)], c='tab:orange')
    img2, = ax2.plot(x[(15+k):], y2[(15+k):], c='tab:orange', linestyle='--')
    img2, = ax2.plot(x[15:], y4[15:], c='tab:orange', linestyle=':', alpha=0.8)
    img5, = ax5.plot(x[0:(16 + k)], y5[0:(16 + k)], c='#FF99CC')
    img5, = ax5.plot(x[(15 + k):], y5[(15 + k):], c='#FF99CC', linestyle='--')
    img5, = ax5.plot(x[16:], y5[16:], c='#FF99CC', linestyle=':', alpha=0.8)

    plt.step(x[:(16+k)], y3[:(16+k)], color='red', where='post', label='post')
    plt.step(x[(15+k):], y3[(15+k):], color='red', where='post', label='post', linestyle='--')

    # 矩形
    fig, ax1.add_patch(patches.Rectangle(xy=(16 + k, 0), width=5, height=6, edgecolor='gray',
                                         fill=False, linewidth=1, linestyle='--'))
    # 设置其他细节
    ax1.set_xlabel('time',fontsize=14)
    ax1.set_ylim(0, 7)
    ax2.set_ylim(0, 7)
    ax5.set_ylim(0, 40)
    ax3.set_ylim(0, 40)

    plt.tight_layout()
    plt.xticks([])
    ax1.set_yticks([])
    ax2.set_yticks([])
    ax3.set_yticks([])
    ax5.set_yticks([])
    plt.text(k+15.8, 35, 'prediction horizon', fontsize=12, color='g')
    plt.text(4, 30, 'target temp', fontsize=12, color='#104E8B')
    plt.text(4, 20, 'indoor temp', fontsize=12, color='orange')
    plt.text(4, 13.7, 'outdoor temp', fontsize=12, color='#FF99CC')
    plt.text(3.5, 7.7, 'frequency of fan', fontsize=12, color='red')
    plt.savefig("{}".format(k), dpi=600)
plt.show()





