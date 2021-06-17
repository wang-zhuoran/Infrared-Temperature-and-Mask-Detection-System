Datadirectory = "Dataset/"

Classes = ["No_mask", "With_mask"]
for category in Classes:
   path = os.path.join(Datadirectory, category)
   for img in os.listdir(path):
       img_array = cv2.imread(os.path.join(path, img))


img_size = 224  # ImageNet => 224 x 224

# reading the images and converting all to array

training_data = []

# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def create_training_data():
    for category in Classes:
        path = os.path.join(Datadirectory, category)
        class_label = Classes.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_label])
            except Exception as e:
                pass


create_training_data()

print(len(training_data))
random.shuffle(training_data)

X = []  # data
y = []  # label

for features, label in training_data:
    X.append(features)
    y.append(label)


X = np.array(X).reshape(-1, img_size, img_size, 3)

print(X.shape)

# normalize the data
X = X / 225.0

Y = np.array(y)


pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out, protocol = 4)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out, protocol = 4)
pickle_out.close()


pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


model = tf.keras.applications.mobilenet.MobileNet()

model.summary()


base_input = model.layers[0].input


base_output = model.layers[-4].output


Flat_layer = layers.Flatten()(base_output)
final_output = layers.Dense(1)(Flat_layer)
final_ouput = layers.Activation('sigmoid')(final_output)

new_model = keras.Model(inputs=base_input, outputs=final_ouput)

new_model.summary()

new_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

new_model.fit(X, Y, epochs=5, validation_split=0.1)

new_model.save('my_first_model.h5')


new_model.summary()
