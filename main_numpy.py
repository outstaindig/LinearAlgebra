# -*- coding:utf-8 -*-
import numpy as np


if __name__ == '__main__':
    print(np.__version__)
    #np.array 的创建
    vec = np.array([1,2,3])
    print(vec)
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5,666))

    #np.array 的基本属性
    print('size',vec.size)
    print(vec[0])
    print(vec[-1])
    print(vec[0:2])
    print(type(vec[0:2]))

    #np.array 的基本运算
    vec2 = np.array([4,5,6])
    print('{} + {} = {}'.format(vec,vec2,vec+vec2))
    print('{} - {} = {}'.format(vec,vec2,vec-vec2))
    print('{} * 2 = {}'.format(vec,vec*2))
    print('2 * {} = {}'.format(vec,2+vec))
    print('{} - {} = {}'.format(vec,vec2,vec*vec2))
    print('{}.dot({}) = {}'.format(vec,vec2,vec.dot(vec2)))

    #向量的模
    print(np.linalg.norm(vec))
    #单位向量
    print(vec / np.linalg.norm(vec))
    print(np.linalg.norm(vec / np.linalg.norm(vec)))