"""d定义二叉树"""
#树的节点
class Node():
    #节点的属性，值，左节点，右节点
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left= left
        self.right = right
#二叉树
class BTree():
    #根节点
        _root = None
    #跟节点属性
    def __init__(self,root):
        self._root = root
        # 定义添加方法，node=节点
    def inseft(self,node):
        # 添加节点，pNode父亲节点，node带添加的节点
        def inseft(pNode,node):
            #如果父亲节点大于带添加的节点
            if pNode.value > node.value:
                #如果左节点为空
                if pNode.left is None:
                    #增加的节点为左节点
                    pNode.left = node
                    # 否则递归的添加左节点
                else:
                    inseft(pNode.left,node)
                    # 否则如果右节点的为空
            else:
                if pNode.right is None:
                    # 则添加到右节点
                    pNode.right=node
                    # 右节点递归的添加
                else:
                    inseft(pNode.right,node)
        # 添加根节点
        inseft(self._root,node)
if __name__=='_main_':
    tree =BTree(Node(5))
    list = [2,1,4,6,8,9]
    for value in list :
        tree.insert(Node(value))



