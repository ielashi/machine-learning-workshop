from keras.layers.core import Dense, Flatten
from keras.models import Sequential
from keras.optimizers import RMSprop

class Brain(object):
  def __init__(self):
    # initialize model
    model = Sequential()
    model.add(Flatten(input_shape=(28,28)))
    model.add(Dense(512, activation='relu', input_shape=(728,)))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    model.compile(
        loss='categorical_crossentropy',
        optimizer=RMSprop(),
        metrics=['accuracy'])

    self.model = model

  def learn(self, elements, labels):
    self.model.fit(
        elements,
        labels,
        batch_size=64,
        epochs=20,
        verbose=1,
        validation_split=0.2)

  def predict(self, elements):
    return self.model.predict(elements)
