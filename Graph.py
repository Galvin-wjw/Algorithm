__author__ = 'galvin'
#-*-coding:utf-8-*-

#图的表示(邻接集 adjacency sets)
a,b,c,d,e,f,g,h = range(8)
N1 = [
    {b,c,d,e,f},#a
    {c,e},
    {d},
    {e},
    {f},
    {c,g,h},
    {f,h},
    {g,f}
]


#图的表示(adjacency lists)
a,b,c,d,e,f,g,h = range(8)
N2 = [
    [b,c,d,e,f],
    [c,e],
    [d],
    [e],
    [f],
    [c,g,h],
    [f,h],
    [g,f]
]

#邻接矩阵(adjacency matrix)
a,b,c,d,e,f,g,h = range(8)
N3 = [
    [0,1,1,1,1,1,0,0],
    [0,0,1,0,1,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,1],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,0,1,1,0]
]