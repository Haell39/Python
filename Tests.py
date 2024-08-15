import matplotlib.pyplot as plt
import numpy as np

# Mandel brot set graph:

def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    
    while abs(z) <= 2 and n < max_iterations:
        z = z**2 + c
        n += 1
        
    return n


#Parametros para vizualizar o grafico:

rows, cols = (800, 800)
re_min, re_max = (-2, 2)
im_min, im_max = (-2, 2)

real = np.linspace(re_min, re_max, cols)
imag = np.linspace(im_min, im_max, rows)
mandelbrot_set = np.zeros((rows, cols))

#Feração do  Fractal:

for x in range(cols):
    for y in range(rows):
        c = complex(real[x], imag[y])
        mandelbrot_set[y, x] = mandelbrot(c, 100)
        

plt.imshow(mandelbrot_set, cmap='Greys')
extent = [re_min, re_max, im_min, im_max]
plt.colorbar()
plt.show()