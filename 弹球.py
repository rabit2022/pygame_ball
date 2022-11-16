import sys

import pygame  # 导入游戏库


class Ball(object):
    PAUSE = False

    def __init__(self):
        self.WIDTH = 800  # 设置窗口的宽度
        self.HEIGHT = 600  # 设置窗口的高度

        # 小球初始化位置
        self.x = self.WIDTH / 2  # 小球的x坐标，初始化在窗口中间
        self.y = self.HEIGHT / 2  # 小球的y坐标，初始化在窗口中间

        self.speed_x = 3  # 小球x方向的速度
        self.speed_y = 5  # 小球y方向的速度
        # self.r = 65  # 小球的半径

        self.bg_color = 255, 255, 0
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # 定义屏幕要在转换图片之前，
        self.image = pygame.image.load("resource/alphas/rainbow_ball.png").convert_alpha()
        self.w, self.h = self.image.get_size()
        self.r = min(self.w, self.h)

    def draw(self):  # 绘制模块，每帧重复执行
        self.screen.fill(self.bg_color)  # 白色背景
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):  # 更新模块，每帧重复操作
        self.x += self.speed_x  # 利用x方向速度更新x坐标
        self.y += self.speed_y  # 利用y方向速度更新y坐标

        if self.x >= self.WIDTH - self.r or self.x <= 0:  # 当小球碰到左右边界时
            self.speed_x = -self.speed_x  # x方向速度反转
        if self.y >= self.HEIGHT - self.r or self.y <= 0:  # 当小球碰到上下边界时
            self.speed_y = -self.speed_y  # y方向速度反转

    @staticmethod
    def music():
        # 添加背景音乐
        pygame.mixer.init()
        pygame.mixer.music.load('./素材/音乐/kanon.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # 循环次数  -1表示无限循环

    @classmethod
    def check_events(cls):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    if not cls.PAUSE:
                        cls.PAUSE = True
                    elif cls.PAUSE:
                        cls.PAUSE = False


def main():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    red_ball = Ball()

    pygame.display.set_caption("弹球")
    # red_ball.music()

    while True:
        Ball.check_events()

        if not Ball.PAUSE:
            red_ball.draw()
            red_ball.update()

            pygame.display.update()
            pygame.time.Clock().tick(60)


if __name__ == '__main__':  # 图片
    main()  # 开始执行游戏
