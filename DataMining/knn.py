#-*- coding: utf-8 -*-

import numpy
import operator

#手动建立一个数据源矩阵group，和数据源的分类结果labels
def createDataSet():
     group = numpy.array([[1.0, 1.1], [1.0, 1.0], [5., 2.], [5.0, 0.1]])
     labels = ['A', 'A', 'B', 'B']
     return group, labels
# newInput为输入的目标，dataset是样本的矩阵，label是分类，k是需要取的个数
def kNNClassify(newInput, dataSet, labels, k):
    #读取矩阵的行数，也就是样本数量
    numSamples = dataSet.shape[0]
    print 'numSamples: ' ,numSamples

    #变成和dataSet一样的行数,行数=原来*numSamples，列数=原来*1 ，然后每个特征点和样本的点进行相减
    diff = numpy.tile(newInput, (numSamples, 1)) - dataSet
    print 'diff: ',diff

    #平方
    squaredDiff = diff ** 2
    print "squaredDiff: ",squaredDiff

    #axis=0 按列求和，1为按行求和
    squaredDist = numpy.sum(squaredDiff, axis = 1)
    print "squaredDist: ",squaredDist

    #开根号，距离就出来了
    distance = squaredDist ** 0.5
    print "distance: ",distance

    #按大小逆序排列
    sortedDistIndices = numpy.argsort(distance)
    print "sortedDistIndices: ",sortedDistIndices

    classCount = {}
    for i in range(k):
        #返回距离（key）对应类别（value）
        voteLabel = labels[sortedDistIndices[i]]
        print "voteLabel: " ,voteLabel

        # 取前几个K值，但是K前几个值的大小没有去比较，都是等效的
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    print "classCount: " ,classCount
    maxCount = 0
    #返回占有率最大的
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)

    return sortedClassCount[0][0]

if __name__ == "__main__":
    dataSet, labels = createDataSet()

    testX = numpy.array([0, 0])
    k = 3
    outputLabel = kNNClassify(testX, dataSet, labels, k)
    print "Your input is:", testX, "and classified to class: ", outputLabel


#########################################
# 运行结果如下:
# numSamples:  4
# diff:  [[-1.  -1.1]
#  [-1.  -1. ]
#  [-5.  -2. ]
#  [-5.  -0.1]]
# squaredDiff:  [[  1.00000000e+00   1.21000000e+00]
#  [  1.00000000e+00   1.00000000e+00]
#  [  2.50000000e+01   4.00000000e+00]
#  [  2.50000000e+01   1.00000000e-02]]
# squaredDist:  [  2.21   2.    29.    25.01]
# distance:  [ 1.48660687  1.41421356  5.38516481  5.0009999 ]
# sortedDistIndices:  [1 0 3 2]
# voteLabel:  A
# voteLabel:  A
# voteLabel:  B
# classCount:  {'A': 2, 'B': 1}
# Your input is: [0 0] and classified to class:  A
