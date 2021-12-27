from matplotlib import pyplot as plt
import numpy as np

def f(s):
    return [np.cos(np.pi * s), np.sin(np.pi * s)]

def g(s):
    return [np.cos(np.pi * s), 2 * np.sin(np.pi * s)]

def h(s):
    return [np.cos(np.pi * s), -1 * np.sin(np.pi * s)]

x = np.arange(-1, 1, 10)
y1, y2, y3 = [], [], []
for i in x:
    y1.append(f(i))
    y2.append(

