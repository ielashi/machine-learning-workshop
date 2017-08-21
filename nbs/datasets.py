import pandas as pd
import numpy as np
from keras.utils.np_utils import to_categorical

def load_arabic_digits():
  X_train, y_train = load_arabic_digits_helper(
      '../datasets/train-digits.csv', '../datasets/train-digits-labels.csv')
  X_test, y_test = load_arabic_digits_helper(
      '../datasets/test-digits.csv', '../datasets/test-digits-labels.csv')

  return ((X_train, y_train), (X_test, y_test))


def load_arabic_digits_helper(items_file, labels_file):
  items = pd.read_csv(items_file, header=None).values
  labels = pd.read_csv(labels_file, header=None).values

  # Shape the items from a 1D vector into a 28x28 2D vector (image)
  items = items.reshape(items.shape[0], 28, 28)

  # Rotate image for easier visualization
  items = np.array([np.fliplr(np.rot90(d, k=3)) for d in items])

#  labels = to_categorical(labels)  # One hot encoding for labels

  return (items, labels) 
