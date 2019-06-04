AdversarialAttack-FineFool
=================
FineFool: Fine Object Contour Attack via Attention  <br>
An adversarial attack method combined with attention mechanism.

Environment
---------------------
CUDA: 9.0 <br>
python: 3.6 <br>
keras: 2.2.4 <br>
tensorflow-gpu: 1.10.0 <br>
numpy: 1.14.5 <br>

Directory
----------------------
imagenet images in the imagenet directory <br>
adversarial images in the adversarials directory <br>
.h5 file  in the model directory <br>

predict the imagenet images on the resnet50
---------------------
.h5 file download link: <br>
    https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels.h5 <br>
python keras_imagenet.py --data=imagenet --model=model/resnet50_weights_tf_dim_ordering_tf_kernels.h5 <br>

predict the imagenet images on the InceptionResnetV2
---------------------
.h5 file download link: <br>
    https://github.com/fchollet/deep-learning-models/releases/download/v0.7/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5 <br>
python keras_imagenet.py --data=imagenet --model=model/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5 <br>

predict the adversarial images on the resnet50
---------------------
.h5 file download link: <br>
    https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_th_dim_ordering_th_kernels.h5 <br>
python keras_imagenet.py --data=adversarials --model=model/resnet50_weights_tf_dim_ordering_tf_kernels.h5 <br>

predict the adversarial images on the InceptionResnetV2
---------------------
.h5 file download link: <br>
    https://github.com/fchollet/deep-learning-models/releases/download/v0.7/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5 <br>
python keras_imagenet.py --data=adversarials --model=model/inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5 <br>
