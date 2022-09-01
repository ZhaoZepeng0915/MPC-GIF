import imageio

gif_images = []
for i in range(0, 7):
    gif_images.append(imageio.imread("D:\\zhaozp24\\python\\python_learning\\"+str(i)+".png"))   # 读取多张图片
imageio.mimsave("mpc.gif", gif_images, fps=3)   # 转化为gif动画