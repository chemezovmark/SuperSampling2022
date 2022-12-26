import numpy as np
import matplotlib.pyplot as plt
from model.common import psnr, ssim

from PIL import Image


def load_image(path):
    return np.array(Image.open(path))
#Загрузка изображения 


def plot(lr, sr, hr):
    plt.figure(figsize=(20, 10))

    images = [lr, sr, hr]
    titles = ['LR', f'SR (x{sr.shape[0] // lr.shape[0]})', 'HR']

    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, 3, i+1)
        plt.imshow(img)
        plt.title(title)
        plt.xticks([])
        plt.yticks([])
        
    plt.figtext(0.43, 0.25, f'PSNR: {psnr(sr, hr).numpy()}', fontsize='xx-large')
    plt.figtext(0.43, 0.22, f'SSIM: {ssim(sr, hr).numpy()}', fontsize='xx-large')
#вывод изображений и метрик