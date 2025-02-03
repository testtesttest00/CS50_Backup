Model 1.1 - 8ms/step - accuracy: avg ~  0.7 - loss: avg ~ 1.0:

    original = tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3))
    conv1 = tf.keras.layers.Conv2D(32, 3, activation="relu")(original)
    pool1 = tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides = (1, 1))(conv1)
    conv2 = tf.keras.layers.Conv2D(8, 3, activation="relu")(pool1)
    altered = tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides = (1, 1))(conv2)

    one = tf.keras.layers.Dense(4, activation="relu")(altered)
    two = tf.keras.layers.Dropout(0.5)(one)
    three = tf.keras.layers.Dense(8, activation="relu")(two)
    four = tf.keras.layers.Dropout(0.4)(three)
    five = tf.keras.layers.Dense(16, activation="relu")(four)
    six = tf.keras.layers.Dropout(0.1)(five)
    flattened = tf.keras.layers.Flatten()(six)
    final = tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")(flattened)

    model = tf.keras.Model(inputs=original, outputs=final)
    model.compile(loss=tf.keras.losses.categorical_crossentropy)


Model 1.2 - 8ms/step - accuracy: avg ~  0.7 - loss: avg ~ 1.0:

    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)))
    model.add(tf.keras.layers.Conv2D(32, 3, activation="relu"))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides = (1, 1)))
    model.add(tf.keras.layers.Conv2D(8, 3, activation="relu"))
    model.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides = (1, 1)))
    model.add(tf.keras.layers.Dense(4, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(8, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.4))
    model.add(tf.keras.layers.Dense(16, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"))
    model.compile(loss=tf.keras.losses.categorical_crossentropy)


Model 2 - 11ms/step - accuracy: avg ~  0.7 - loss: avg ~ 1.4:

    model = tf.keras.Sequential()
    model.add(tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)))
    model.add(tf.keras.layers.Dense(32, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(48, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.4))
    model.add(tf.keras.layers.Dense(64, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax"))
    model.compile(loss=tf.keras.losses.categorical_crossentropy)


Model 3 - 4ms/step - accuracy: avg ~ 0.05 - loss: avg ~ 3.5:

    image_processing = tf.keras.Sequential()
    image_processing.add(tf.keras.layers.Conv2D(filters=8, strides=(1,1), kernel_size=(5,5)))
    image_processing.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    image_processing.add(tf.keras.layers.Flatten())

    data_processing = tf.keras.Sequential()
    data_processing.add(tf.keras.layers.Dropout(rate=0.5))
    data_processing.add(tf.keras.layers.Dense(units=4, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(units=8, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(units=10, activation=tf.keras.activations.relu))

    model = tf.keras.Sequential(
        [
        tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        image_processing,
        data_processing,
        tf.keras.layers.Dense(units=NUM_CATEGORIES, activation=tf.keras.activations.softmax)
        ]
    )

    model.compile(loss=tf.keras.losses.categorical_crossentropy)


Model 4 - 3ms/step - accuracy: avg ~ 0.05 - loss: avg ~ 3.5:

    image_processing = tf.keras.Sequential()
    image_processing.add(tf.keras.layers.Conv2D(filters=8, strides=(1,1), kernel_size=(5,5)))
    image_processing.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    image_processing.add(tf.keras.layers.Flatten())

    data_processing = tf.keras.Sequential()
    data_processing.add(tf.keras.layers.Dropout(rate=0.5))
    data_processing.add(tf.keras.layers.Dense(units=4, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(units=8, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(
        units=10, activation=tf.keras.activations.relu, kernel_regularizer=tf.keras.regularizers.L2
        ))

    model = tf.keras.Sequential(
        [
        tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        image_processing,
        data_processing,
        tf.keras.layers.Dense(units=NUM_CATEGORIES, activation=tf.keras.activations.softmax)
        ]
    )

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss=tf.keras.losses.categorical_crossentropy, metrics=["accuracy"])


Model 5 - 4ms/step - accuracy: avg ~  0.7 - loss: avg ~ 0.9:

    image_processing = tf.keras.Sequential()
    image_processing.add(tf.keras.layers.Conv2D(filters=8, strides=(1,1), kernel_size=(5,5)))
    image_processing.add(tf.keras.layers.BatchNormalization())
    image_processing.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    image_processing.add(tf.keras.layers.Flatten())

    data_processing = tf.keras.Sequential()
    data_processing.add(tf.keras.layers.Dropout(rate=0.5))
    data_processing.add(tf.keras.layers.Dense(units=4, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(units=8, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(
        units=10, activation=tf.keras.activations.relu, kernel_regularizer=tf.keras.regularizers.L2
        ))

    model = tf.keras.Sequential(
        [
        tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        image_processing,
        data_processing,
        tf.keras.layers.Dense(units=NUM_CATEGORIES, activation=tf.keras.activations.softmax)
        ]
    )

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss=tf.keras.losses.categorical_crossentropy, metrics=["accuracy"])


Model 6 (Final) - 5ms/step - accuracy: avg ~  0.9 - loss: avg ~ 0.5:

    image_processing = tf.keras.Sequential()
    image_processing.add(tf.keras.layers.Conv2D(filters=32, strides=(1,1), kernel_size=(5,5)))
    image_processing.add(tf.keras.layers.BatchNormalization())
    image_processing.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    image_processing.add(tf.keras.layers.Flatten())

    data_processing = tf.keras.Sequential()
    data_processing.add(tf.keras.layers.Dropout(rate=0.5))
    data_processing.add(tf.keras.layers.Dense(units=12, activation=tf.keras.activations.relu))
    data_processing.add(tf.keras.layers.Dense(
        units=12, activation=tf.keras.activations.relu, kernel_regularizer=tf.keras.regularizers.L1
        ))
    data_processing.add(tf.keras.layers.Dense(
        units=16, activation=tf.keras.activations.relu, kernel_regularizer=tf.keras.regularizers.L2
        ))

    model = tf.keras.Sequential(
        [
        tf.keras.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        image_processing,
        data_processing,
        tf.keras.layers.Dense(units=NUM_CATEGORIES, activation=tf.keras.activations.softmax)
        ]
    )

    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss=tf.keras.losses.categorical_crossentropy, metrics=["accuracy"])

----------

General stuff learnt:

    Filter is similar to what a unit in a dense layer, to a convolutional layer;
    a filter is just a matrix of weights that is learning via backpropogation.
    Adding more filters onto a convolutional layer is like adding more units and may cause overfitting.

Technical stuff learnt:
    Flatten is used:
    Filter creates multiple arrays of the same input
    (e.g. (10, 20) into (8, 18, 3) if 3 filters, stride(1, 1) and kernel_size(3, 3) are used)

    Binary outputs are involved, use:
        activation="softmax"
        tf.keras.losses.categorical_crossentropy

    Building a model:
        1.    Using functional API
            - create Layer_n = tf.keras.layers...
                - Use model = tf.keras.Model(inputs = Input_layer, outputs = Output_layer)
                Or
                - Use model = Output_layer(...(Layer_2(Layer_1(Input_layer(shape)))))

        2.    Using Sequential
            - create model = tf.keras.Sequential()
                - at initialisation, tf.keras.Sequential([Layer_1, Layer_2, ..., Layer_n])
                Or
                - after initialisation, model.add(Layer_n)

    Duck debugger: Here are a few suggestions to improve your model:

        Learning Rate:
            Adjust the learning rate.
            Sometimes a smaller learning rate can help the model converge better.

        Batch Normalization:
            Add batch normalization layers after convolutional layers to stabilize and speed up training.

        Regularization:
            Add L2 regularization to your dense layers to prevent overfitting.

        Data Augmentation:
            Use data augmentation techniques to increase the diversity of your training data.

        Optimizer:
            Experiment with different optimizers like Adam or RMSprop.

        Model Complexity:
            Ensure your model is not too complex for the amount of data you have.
            Sometimes simplifying the model can improve performance.
