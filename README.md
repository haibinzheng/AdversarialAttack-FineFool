##########environment###############
CUDA: 9.0
python: 3.6
keras: 2.2.4
tensorflow-gpu: 1.10.0
numpy: 1.14.5

##########directory###############
imagenet images in the imagenet directory
adversarial images in the adversarials directory
.h5 file  in the model directory
#############################
#predict the imagenet images on the resnet50
.h5 file download link:
    https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels.h5

python keras_imagenet.py --data=imagenet --model=model/resnet50_weights_tf_dim_ordering_tf_kernels.h5

#predict the imagenet images on the InceptionResnetV2
.h5 file download link:
    https://github.com/fchollet/deep-learning-models/releases/download/v0.7/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5

python keras_imagenet.py --data=imagenet --model=model/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5

#############################
#predict the adversarial images on the resnet50
.h5 file download link:
    https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels.h5

python keras_imagenet.py --data=adversarials --model=model/resnet50_weights_tf_dim_ordering_tf_kernels.h5

#predict the adversarial images on the InceptionResnetV2
.h5 file download link:
    https://github.com/fchollet/deep-learning-models/releases/download/v0.7/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5

python keras_imagenet.py --data=adversarials --model=model/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5
