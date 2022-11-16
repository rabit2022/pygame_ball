# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程3
# @File    : 透明图转换.py
# @Time    : 2022/10/18 17:58
# @Author  : paopaokele 
# @Version : python3.10
# @IDE     : PyCharm
# @Origin  : 
# @Description: $END$
import os

import numpy
from PIL import Image


def transparent_background(path):
    '''https://www.cnblogs.com/lab-zj/p/12896305.html
    将图像转换为 RGBA 格式，然后检查像素值。
    如果像素值大于 color_no，则将像素值设置为 (255, 255, 255, 0)。
    '''
    try:
        img = Image.open(path)
        img = img.convert("RGBA")  # 转换获取信息
        # 为图像分配存储空间并加载像素数据
        pixdata = img.load()
        color_no = get_convert_middle(path) + 30  # 抠图的容错值

        # 从图像中删除白色背景。
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                # pixdata[x, y] = (255, 255, 255, 0),r,g,b,alpha
                if pixdata[x, y][0] > color_no and pixdata[x, y][1] > color_no \
                        and pixdata[x, y][2] > color_no and pixdata[x, y][3] > color_no:
                    pixdata[x, y] = (255, 255, 255, 0)

        save_path = getSavePath(path)
        img.save(save_path)
        img.close()
    except Exception as e:
        return False
    return save_path


def get_convert_middle(img_path):
    """
    它采用图像路径，将其转换为灰度，对像素值进行平方，并返回最小和最大像素值的平均值

    :param img_path: 要处理的图像的路径
    """
    gray = Image.open(img_path).convert('L')  # 灰度
    im = numpy.array(gray)
    im4 = 255.0 * (im / 255.0) ** 2  # 对图像的像素值求平方后得到的图像
    middle = (int(im4.min()) + int(im4.max())) / 2
    # print(middle)
    return middle





def getSavePath(path):
    # 标准化路径normpath
    p_list = os.path.normpath(path).split(os.sep)

    # 前缀
    p_list[-2] = "alphas"
    prefix_path = os.path.join(*p_list[:-1])
    if not os.path.exists(prefix_path):
        os.mkdir(prefix_path)
    print(prefix_path)

    # 后缀
    f_list = p_list.pop().split(".")
    f_list[-1] = "png"
    postfix = ".".join(f_list)
    p_list.append(postfix)

    s_path = os.path.join(*p_list)
    return s_path


if __name__ == '__main__':
    path = "resource/images/dragon_0.png"
    # 调用 transparent_background, 传入图片路径, 该方法把图片修改后替换了源文件
    res = transparent_background(path)
    print(res)