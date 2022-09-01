import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

for i in range(0,7):
    k = i
    # 构造数据
    x = np.arange(1, 30)
    y1 = 5 * x ** 0
    if k == 0:
        y2 = 10 - (5.5 * (np.exp(-0.5 * x) + 1.1) + 0.1 * np.sin(x)) + 0.03 * x
        y3 = [12, 10, 8, 11, 9, 8, 10, 9, 7, 10, 9, 7, 5, 9, 8, 6, 6,6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
    y4 = 10 - (5.5 * (np.exp(-0.5 * x) + 1.1) + 0.1 * np.sin(x)) + 0.03 * x
    for j in range(k,14):
        y2[15+j] = y2[15+j]+np.random.uniform(-0.05, 0.05)
        y3[15+j] = (y2[15+j]-4)*8+np.random.uniform(-0.3, 0.3)
    # y3 = np.random.randint(5, 12, size=29) - 0.3 * x + 4.5

    # 构造多个ax
    fig, ax1 = plt.subplots(figsize=(9, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()
    # 绘制
    img1, = ax1.plot(x, y1, c='tab:blue')
    img2, = ax2.plot(x[0:(16+k)], y2[0:(16+k)], c='tab:orange')
    img2, = ax2.plot(x[(15+k):], y2[(15+k):], c='tab:orange', linestyle='--')
    img2, = ax2.plot(x[16:], y4[16:], c='tab:orange', linestyle=':', alpha=0.8)
    # 获取对应折线图颜色给到spine ylabel yticks yticklabels
    axs = [ax1, ax2]
    imgs = [img1, img2]

    for i in range(len(axs)):
        # axs[i].spines['right'].set_color(imgs[i].get_color())
        # axs[i].tick_params(axis='y', color=imgs[i].get_color(), labelcolor=imgs[i].get_color())
        # axs[i].spines['left'].set_color(img1.get_color())  # 注意ax1是left
        # axs[0].set_ylabel('target value',fontsize=12, c=imgs[0].get_color())
        # axs[1].set_ylabel('status value',fontsize=12, c=imgs[1].get_color())
        axs[i].set_yticks([])

    plt.step(x[:(16+k)], y3[:(16+k)], color='red', where='post', label='post')
    plt.step(x[(15+k):], y3[(15+k):], color='red', where='post', label='post', linestyle='--')

    # 矩形
    fig, ax1.add_patch(patches.Rectangle(xy=(16 + k, 0), width=5, height=6, edgecolor='gray',
                                         fill=False, linewidth=1, linestyle='--'))
    # 设置其他细节
    ax1.set_xlabel('time',fontsize=14)
    ax1.set_ylim(0, 7)
    ax2.set_ylim(0, 7)
    ax3.set_ylim(0, 40)
    plt.tight_layout()
    plt.xticks([])
    plt.yticks([])
    plt.text(k+15.5, 35, 'prediction horizon', fontsize=12, color='g')
    plt.text(0, 29.5, 'target value', fontsize=12, color='#104E8B')
    plt.text(0, 20, 'status value', fontsize=12, color='orange')
    plt.text(0, 12.5, 'control value', fontsize=12, color='red')
    plt.savefig("{}".format(k), dpi=600)
plt.show()





