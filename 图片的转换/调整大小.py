# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Project : 工程4
# @File    : 调整大小.py
# @Time    : 2022/10/20 18:43
# @Author  : paopaokele 
# @Version : python3.10
# @IDE     : PyCharm
# @Origin  : https://blog.csdn.net/weixin_44799217/article/details/115396251
# @Description: $END$


import os
from typing import Tuple, List, Union

from PIL import Image


class AlterSize(object):
    def __init__(self, path: str, new_size):
        if isinstance(new_size, (tuple, list)):
            new_size: Union[Tuple[int, int], List[int, int]]
            self.new_size = new_size

        elif isinstance(new_size, (str, int)):
            # 按比例调整大小
            new_size: Union[str, int]
            rate = int(new_size)

            img_path = Image.open(path)
            self.new_size = list(map(lambda x: x * rate // 100, img_path.size))
            print("Image:", self.new_size)

        self.path = path

    @staticmethod
    def getSavePath(path, new_dir, new_ex="png"):
        """
        生成保存路径
        :param path: 要处理的图像的路径
        :type path: resource\imaaes\rainbow_ball.png
        :param new_dir: 保存图像的新目录的名称
        :type new_dir: "sizes"
        :param new_ex: 新文件的扩展名
        :type new_ex: defaults to png (optional)
        :return: 保存路径
        :rtype: resource\sizes\rainbow_ball.png
        """
        # 标准化路径normpath
        p_list = os.path.normpath(path).split(os.sep)

        # print(p_list)
        # 前缀
        p_list[-2] = new_dir
        prefix_path = os.path.join(*p_list[:-1])
        if not os.path.exists(prefix_path):
            os.mkdir(prefix_path)
        # print(prefix_path)

        # 后缀
        f_list = p_list.pop().split(".")
        f_list[-1] = new_ex
        postfix = ".".join(f_list)
        p_list.append(postfix)

        s_path = os.path.join(*p_list)
        return s_path

    def setImage(self, path) -> str:
        """
        调整图片大小
        :param path: 待处理图像的路径
        """
        save_path = self.getSavePath(path, "sizes")
        #  待处理图片路径
        img_path = Image.open(path)
        #  resize图片大小，入口参数为一个tuple，新的图片的大小
        img_size = img_path.resize(self.new_size)
        #  处理图片后存储路径，以及存储格式
        img_size.save(save_path)
        return save_path

    def setImages(self) -> List[str]:
        #  待处理图片路径下的所有文件名字
        all_file_names = os.listdir(self.path)

        save_path_list = []
        for file_name in all_file_names:
            path = os.path.join(self.path, file_name)
            save_path = self.setImage(path)
            save_path_list.append(save_path)
        return save_path_list

    def main(self) -> str or List[str]:
        '''
        对路径和文件分开处理
        :returns save_path:
        '''
        if not os.path.exists(self.path):
            raise FileNotFoundError("路径找不到")

        if os.path.isdir(self.path):
            save_path = self.setImages()
        elif os.path.isfile(self.path):
            save_path = self.setImage(self.path)
        else:
            raise FileNotFoundError("输入路径有误")

        return save_path


if __name__ == '__main__':
    a = AlterSize("resource/images/heart.png", (32, 32))
    save_path = a.main()
    print(save_path)
    ...
