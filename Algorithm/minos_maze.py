class MinosMaze:
    def __init__(self,n):
        self.n = n
        """init——status"""
        self.init_status = 0b001
        self.maze =[([self.init_status]*n)for i in range(n)]
    def show_bin(self):
        for a in self.maze:
            for i in a :
                print('%6s' % bin(i),end='')
            print()
if __name__=='__main__':
    m_8 = MinosMaze(8)
    m_8.show_bin()
