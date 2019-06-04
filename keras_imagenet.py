# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__author__ = 'Bear'
import numpy as np
import os, argparse, glob
from keras.preprocessing import image
from keras.applications import ResNet50, InceptionResNetV2
from keras.applications.imagenet_utils import decode_predictions,preprocess_input
parser = argparse.ArgumentParser()
parser.add_argument('--model', default='resnet50',choices=['resnet50', 'inceptionresnetv2'], help='Path to basis.npy to load for attack.')
parser.add_argument('--data', help='Path to images to read.')

args = parser.parse_args()

class DeepModel(_):
    def __init__(self, name):
        if name.lowwer() == 'resnet50':
            self.model = ResNet50()
        elif name.lowwer() == 'inceptionresnetv2':
            self.model = InceptionResNetV2()
    def predict(self, image):
        logits = self.model.predict(image)
        label = np.argmax(logits)
        return logits, label

def load_img(path):
    img = image.load_img(path, target_size=(224, 224, 3), interpolation='BILINEAR')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='tf')
    return x
if __name__ == '__main__':
    #build model
    model = DeepModel(name=args.model)

    #load image
    for img_path in glob.glob(os.path.join(args.data, r'*.*')):
        img = image.load_img(img_path, target_size=(224, 224))
        logits, label = model.predict(img)
        print('{}:'.format(img_path), decode_predictions(logits, top=3))