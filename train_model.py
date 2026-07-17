<<<<<<< HEAD
"""
train_model.py

Regenerates model_cnn.h5 for the fabric pattern classifier using the
images already present in Data/train and Data/test.
"""

import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ---- Config ----
IMG_SIZE = (224, 224)   # must match app.py's target_size
BATCH_SIZE = 16
EPOCHS = 20
TRAIN_DIR = os.path.join("Data", "train")
TEST_DIR = os.path.join("Data", "test")
MODEL_OUT = "model_cnn.h5"

# These must match the label order in app.py exactly.
LABELS = ['animal', 'cartoon', 'floral', 'geometry', 'ikat', 'plain',
          'polka dot', 'squares', 'stripes', 'tribal']

# ---- Data generators ----
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_gen = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    classes=LABELS,   # force the exact class order app.py expects
    shuffle=True,
)

test_gen = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    classes=LABELS,
    shuffle=False,
)

print("Class indices (should match app.py's LABELS order):")
print(train_gen.class_indices)

# ---- Model ----
model = models.Sequential([
    layers.Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dropout(0.4),
    layers.Dense(128, activation="relu"),
    layers.Dense(len(LABELS), activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

model.summary()

# ---- Train ----
history = model.fit(
    train_gen,
    validation_data=test_gen,
    epochs=EPOCHS,
)

# ---- Save ----
model.save(MODEL_OUT)
=======
"""
train_model.py

Regenerates model_cnn.h5 for the fabric pattern classifier using the
images already present in Data/train and Data/test.
"""

import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ---- Config ----
IMG_SIZE = (224, 224)   # must match app.py's target_size
BATCH_SIZE = 16
EPOCHS = 20
TRAIN_DIR = os.path.join("Data", "train")
TEST_DIR = os.path.join("Data", "test")
MODEL_OUT = "model_cnn.h5"

# These must match the label order in app.py exactly.
LABELS = ['animal', 'cartoon', 'floral', 'geometry', 'ikat', 'plain',
          'polka dot', 'squares', 'stripes', 'tribal']

# ---- Data generators ----
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_gen = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    classes=LABELS,   # force the exact class order app.py expects
    shuffle=True,
)

test_gen = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    classes=LABELS,
    shuffle=False,
)

print("Class indices (should match app.py's LABELS order):")
print(train_gen.class_indices)

# ---- Model ----
model = models.Sequential([
    layers.Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3)),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dropout(0.4),
    layers.Dense(128, activation="relu"),
    layers.Dense(len(LABELS), activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

model.summary()

# ---- Train ----
history = model.fit(
    train_gen,
    validation_data=test_gen,
    epochs=EPOCHS,
)

# ---- Save ----
model.save(MODEL_OUT)
>>>>>>> 2a62090 (Add Data folder)
print(f"\nSaved trained model to {MODEL_OUT}")