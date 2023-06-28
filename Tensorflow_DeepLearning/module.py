'''
import os, sys
current_dir = os.path.dirname(os.path.abspath("../module.py"))
sys.path.append(current_dir)
from module import *
'''
import pandas as pd
from tensorflow import keras as tf
import numpy as np
import matplotlib.pyplot as plt
from attention import Attention
from tf_explain.core.grad_cam import GradCAM
from tf_explain.core.occlusion_sensitivity import OcclusionSensitivity

optimizers = tf.optimizers
metrics = tf.metrics
Input = tf.Input
models = tf.models
layers = tf.layers

# models
Sequential = tf.models.Sequential
Model = tf.models.Model

# layers
Dense = tf.layers.Dense
LSTM = tf.layers.LSTM
Embedding = tf.layers.Embedding
Dropout = tf.layers.Dropout
Conv1D = tf.layers.Conv1D
MaxPooling1D = tf.layers.MaxPooling1D
Activation = tf.layers.Activation
Input = tf.layers.Input
Reshape = tf.layers.Reshape
BatchNormalization = tf.layers.BatchNormalization
LeakyReLU = tf.layers.LeakyReLU
UpSampling2D = tf.layers.UpSampling2D
Conv2D = tf.layers.Conv2D
Flatten = tf.layers.Flatten
MaxPooling2D = tf.layers.MaxPooling2D

# utils
to_categorical = tf.utils.to_categorical

# preprocessing
sequence = tf.preprocessing.sequence
Tokenizer = tf.preprocessing.text.Tokenizer
text_to_word_sequence = tf.preprocessing.text.text_to_word_sequence
pad_sequence = tf.preprocessing.sequence.pad_sequences
ImageDataGenerator = tf.preprocessing.image.ImageDataGenerator

# callbacks
EarlyStopping = tf.callbacks.EarlyStopping

# 데이터
reuters = tf.datasets.reuters
imdb = tf.datasets.imdb
mnist = tf.datasets.mnist
fashion_mnist = tf.datasets.fashion_mnist

# applications
VGG16 = tf.applications.VGG16

# 한글
plt.rcParams['font.family'] = 'Malgun Gothic'