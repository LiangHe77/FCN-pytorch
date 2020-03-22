import numpy as np

#该onehot有问题
def onehot(data, n):
    buf = np.zeros(data.shape + (n, ))    #(160,160,n)
    nmsk = np.arange(data.size)*n + data.ravel()      #ravel()将data扁平化
    buf.ravel()[nmsk-1] = 1
    return buf

    
#改写的onehot
def onehot(data,n):
    buf = np.zeros(data.shape + (n, ))
    for i in range(len(data)):
        for j in range(len(data[0])):
            buf[i][j][abs(data[i][j]-1)] = 1
    return buf
