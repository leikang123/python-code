from typing import List, Union, Any
import random
def show_bin(maze):
        for a  in maze:
            for i in a:
                print('%6s' % bin(i),end='')
            print()

class MinosMaze:

    def __init__(self,n):
        self.n = n
        """init——status"""
        self.init_status = 0b001
        self.maze =[([self.init_status]*n)for i in range(n)]

    """拆墙方法，i-行号，j-列号，side-拆墙方向"""
    def remove_wall(self,i,j,side):
        if side == 'U':
            self.maze[i][j] &=0b110
        elif side == 'R':
            self.maze[i][j] &=0b110
    def create(self):
        def check(i,j,side):
            if side == 'U':
                return i -1 >=0 and self.maze[i-1][j] ==self.init_status
            elif side == 'D':
                return i+1 < self.n and self.maze[i+1][j] ==self.init_status
            elif side =='L':
                return j-1 >=0 and self.maze[i][j-1] ==self.init_status
            elif side =='R':
                return j+1 <self.n and self.maze[i][j+1] ==self.init_status
            else:
                return False
        def auto_rm_wall(i,j):
            sides = ['U', 'D', 'L', 'R']  # 上、下、左、右四个方向
            self.maze[i][j] |= 0b100  # maze[i][j] 已经被设置过
            # 如果可以从当前方格向上、下、左、右几个方向之一移动，开始拆墙操作
            while (len([s for s in sides if check(i, j, s)]) > 0):
                side = random.choice(sides)  # 随机方向
                if side == 'U' and check(i, j, side):  # 能够向上走
                    self.remove_wall(i, j, 'U')  # 拆除当前方格的上墙
                    auto_rm_wall(i - 1, j)  # 向上走
                elif side == 'D' and check(i, j, side):  # 能够向下走
                    self.remove_wall(i + 1, j, 'U')  # 拆除下侧方格的上墙
                    auto_rm_wall(i + 1, j)  # 向下走
                elif side == 'L' and check(i, j, side):  # 能够向左走
                    self.remove_wall(i, j - 1, 'R')  # 拆除左侧方格的右墙
                    auto_rm_wall(i, j - 1)  # 向左走
                elif side == 'R' and check(i, j, side):  # 能够向右走
                    self.remove_wall(i, j, 'R')  # 拆除当前方格的右墙
                    auto_rm_wall(i, j + 1)  # 向右走

        auto_rm_wall(0, 0)  # 从入口位置开始遍历


if __name__=='__main__':
    m_8 = MinosMaze(8)
    m_8.show_bin()
