import pandas as pd
import numpy as np
from keras.utils.np_utils import to_categorical

def load_arabic_digits():
  return load_arabic_digits_helper(
      'datasets/arabic-digits/csvTrainImages 60k x 784.csv', 'datasets/arabic-digits/csvTrainLabel 60k x 1.csv')


def load_arabic_digits_test():
  return load_arabic_digits_helper(
      'datasets/arabic-digits/csvTestImages 10k x 784.csv', 'datasets/arabic-digits/csvTestLabel 10k x 1.csv')

def load_arabic_digits_helper(items_file, labels_file):
  items = pd.read_csv(items_file, header=None).values
  labels = pd.read_csv(labels_file, header=None).values

  # Shape the items from a 1D vector into a 28x28 2D vector (image)
  items = items.reshape(items.shape[0], 28, 28)

  # Rotate image for easier visualization
  items = np.array([np.fliplr(np.rot90(d, k=3)) for d in items])

  return (items, labels) 


def load_mnist(train_file='../datasets/mnist/train.csv', test_file='../datasets/mnist/test.csv'):
  train = pd.read_csv(train_file)
  test = pd.read_csv(test_file)

  X_train = train.iloc[:, 1:].values
  X_train = X_train.reshape(X_train.shape[0], 28, 28)
    
  y_train = train.iloc[:, 0].values
    
  X_test = test.values
    
  return (X_train, y_train, X_test)

"""
def load_arabic_characters():
  X_train, y_train = load_arabic_digits_helper(
      'datasets/arabic-characters/csvTrainImages 13440x1024.csv', 'datasets/arabic-characters/csvTrainLabel 13440x1.csv')

  return (X_train, y_train)
"""

