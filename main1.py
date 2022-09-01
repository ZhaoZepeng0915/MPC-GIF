import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# 循环7次，生成7个图片
for i in range(0,7):
    k = i
    # 构造数据
    x = np.arange(1, 30)
    y1 = 22 * x ** 0
    # 初始化数据
    if k == 0:
        y2 = [28.7,29,29.1,28.8,28.6,28.3,27.9,27.4,26.8,25.9,25.1,24.4,23.8,23.3,22.955,22.6,22.4,22.2,22.05,21.85,21.7,21.6,21.5,21.52,21.6,21.68,21.75,21.85,21.93]
        y3 = [12, 11.4, 11, 10, 10.5, 11, 10, 9.8, 10.3, 10, 9, 8.5, 9.2, 9, 8.55, 8, 7.8,7.4, 7, 6.5,5.8, 5.2, 4.7, 4.3, 4.0,3.8, 4.0, 3.8, 4.1]
        y5 = [29.7,30,30.4,30.8,31.3,31.9,32.7,33.5,34.1,34.6,34.9,35.1,35.2,35.25,35.155,34.8,34.3,33.6,32.8,31.2,29.7,28.9,27.5,26.6,25.3,24.6,24.5,24.3,24.2]
    y4 = y2.copy()
    # 每次循环在原有数据基础上重新生成随机数据
    for j in range(k,14):
        y2[15+j] = y2[15+j]+np.random.uniform(-0.1, 0.1)
        y3[15+j] = y3[15+j]+np.random.uniform(-0.1, 0.1)
        y5[15+j] = y5[15+j]+np.random.uniform(-0.2, 0.2)

    # 构造多个ax,共享x轴
    fig, ax1 = plt.subplots(figsize=(9, 6))
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()
    ax5 = ax1.twinx()
    # 绘制
    img1, = ax1.plot(x, y1, c='tab:blue')
    img1, = ax1.plot(x, y1 + 1, c='tab:blue',linestyle='--',alpha=0.3)
    img1, = ax1.plot(x, y1 - 1, c='tab:blue',linestyle='--',alpha=0.3)
    img2, = ax2.plot(x[0:(16+k)], y2[0:(16+k)], c='tab:orange')
    img2, = ax2.plot(x[(15+k):], y2[(15+k):], c='tab:orange', linestyle='--')
    img2, = ax2.plot(x[15:], y4[15:], c='tab:orange', linestyle=':', alpha=0.8)
    img5, = ax5.plot(x[0:(16 + k)], y5[0:(16 + k)], c='#FF99CC')
    img5, = ax5.plot(x[(15 + k):], y5[(15 + k):], c='#FF99CC', linestyle='--')
    img5, = ax5.plot(x[16:], y5[16:], c='#FF99CC', linestyle=':', alpha=0.8)

    plt.step(x[:(16+k)], y3[:(16+k)], color='red', where='post', label='post')
    plt.step(x[(15+k):], y3[(15+k):], color='red', where='post', label='post', linestyle='--')

    fig, ax1.add_patch(patches.Rectangle(xy=(16+k, 0), width=5, height=36, edgecolor='gray', fill=False,
                                         linewidth=1, linestyle='--'))   # 添加矩形
    # 设置其他细节
    ax1.set_xlabel('time',fontsize=14)
    ax1.set_ylim(0, 40)
    ax2.set_ylim(0, 40)
    ax5.set_ylim(0, 40)
    ax3.set_ylim(0, 40)
    # 取消坐标轴的显示
    plt.xticks([])
    ax1.set_yticks([])
    ax2.set_yticks([])
    ax3.set_yticks([])
    ax5.set_yticks([])
    # 添加需要的文本
    plt.text(k+15.8, 36.5, 'prediction horizon', fontsize=12, color='g')
    plt.text(1, 19.5, 'target temp', fontsize=12, color='#104E8B')
    plt.text(1, 27.3, 'indoor temp', fontsize=12, color='orange')
    plt.text(1, 32, 'outdoor temp', fontsize=12, color='#FF99CC')
    plt.text(1, 8, 'cooling supply', fontsize=12, color='red')
    # 输出图形并以k值命名
    plt.savefig("{}".format(k), dpi=600)
plt.show()





