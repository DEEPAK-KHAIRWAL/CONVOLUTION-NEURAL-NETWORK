from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Convolution2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
classifier = Sequential()
classifier.add(Conv2D(64,( 3, 3), input_shape=(64, 64, 3), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(64,( 3, 3), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(activation="relu", units=128))
classifier.add(Dense(activation="sigmoid", units=1))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
train_datagen = ImageDataGenerator(
                                    rescale=1./255,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
                                                    'train',
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='binary')

test_set = test_datagen.flow_from_directory(
                                            'test',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(
                    training_set,
                    steps_per_epoch=25,
                    epochs=10,
                    validation_data=test_set,
                    validation_steps=1)
