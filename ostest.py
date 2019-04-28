import pandas as pd 
import tensorflow as tf
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split




dataframe = pd.read_csv("feats/combined.csv", encoding = "utf-8")

train, test = train_test_split(dataframe, test_size = .2)
train, val = train_test_split(train, test_size=.2)
print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')



def df_to_dataset(dataframe, shuffle=False, batch_size=32):
	dataframe = dataframe.copy()
	labels = dataframe.pop('target')
	ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
	if shuffle:
		ds = ds.shuffle(buffer_size=len(dataframe))
	ds = ds.batch(batch_size)
	return ds

train_ds = df_to_dataset(train, shuffle = True)
val_ds = df_to_dataset(val)
test_ds = df_to_dataset(test)

headers = []

for feature_batch, label_batch in train_ds.take(1):
	headers =  list(feature_batch.keys())

	print('A batch of targets:', label_batch )


f_cols = []

for header in headers:
	f_cols.append(feature_column.numeric_column(header))

feat_layer = tf.keras.layers.DenseFeatures(f_cols)



model = tf.keras.models.Sequential([
  feat_layer,
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_ds, epochs=10)
model.evaluate(test_ds)

