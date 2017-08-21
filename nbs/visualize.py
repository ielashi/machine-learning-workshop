import matplotlib.pyplot as plt
import random


def show_sample(images, labels):
  for i in range(0, 12):
    random_idx = random.randint(0, len(images))

    sp = plt.subplot(3, 4, i + 1)
    sp.set_title(labels[random_idx][0], fontsize=16)
    sp.axis('off')
    plt.imshow(images[random_idx])


def show_sample_idx(data, indices):
  for i in range(0, 9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(data[random.choice(indices)])


import numpy as np

def plots(ims, figsize=(12,6), rows=1, interp=False, titles=None):
#    if type(ims[0]) is np.ndarray:
#        ims = np.array(ims).astype(np.uint8)
#        if (ims.shape[-1] != 3):
#            ims = ims.transpose((0,2,3,1))
    f = plt.figure(figsize=figsize)
    cols = len(ims)//rows if len(ims) % 2 == 0 else len(ims)//rows + 1
    for i in range(len(ims)):
        sp = f.add_subplot(rows, cols, i+1)
        sp.axis('Off')
        if titles is not None:
            sp.set_title(titles[i], fontsize=16)
        plt.imshow(ims[i], interpolation=None if interp else 'none')
