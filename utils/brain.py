from keras.layers.core import Dense, Flatten
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.utils.np_utils import to_categorical

import numpy as np


class Brain(object):
  def __init__(self):
    # initialize model
    model = Sequential()
    model.add(Flatten(input_shape=(28,28)))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.compile(
        loss='categorical_crossentropy',
        optimizer=RMSprop(),
        metrics=['accuracy'])

    self.model = model

  def learn(self, images, labels):
    images = self._preprocess_images(images)
    labels = self._preprocess_labels(labels)

    self.model.fit(
        images,
        labels,
        batch_size=64,
        epochs=5,
        verbose=1,
        validation_split=0.2)

  def predict_many(self, images):
    images = self._preprocess_images(images)
    return self.model.predict_classes(images)

  def predict(self, image):
    return self.predict_many(np.array([image]))

  def _preprocess_images(self, images):
    return images.astype('float32') / 255

  def _preprocess_labels(self, labels):
    return to_categorical(labels)
