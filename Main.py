# @Author Ömer Faruk Tekin
import tensorflow as tf
import random
import matplotlib.pyplot as plt
print('TensorFlow version', tf.__version__)

model=tf.keras.applications.vgg16.VGG16(
    include_top=False, weights='imagenet',
    input_shape=(96,96,3))
model.summary()

def get_submodel(layer_name):
    return tf.keras.models.Model(
        model.input,
        model.get_layer(layer_name).output
    )
get_submodel('block1_conv2').summary()

def create_image():
    return tf.random.uniform((96,96,3),minval=-0.5,maxval=0.5)
def plot_image(image,title='random'):
    image=image-tf.math.reduce_min(image)
    image=image/tf.math.reduce_max(image)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()

image=create_image()
plot_image(image)
def visualize_filter(layer_name,f_index=None,iters=50):
    submodel=get_submodel(layer_name)
    num_filters=submodel.output.shape[-1]
    
    if f_index is None:
        f_index=random.randint(0,num_filters-1)
    assert num_filters>f_index,'f_index is out of bounnds'
    image=create_image()
    verbose_step=int(iters/10)
    
    for i in range(0,iters):
        with tf.GradientTape() as tape:
            tape.watch(image)
            out=submodel(tf.expand_dims(image,axis=0))[:,:,:,f_index]
            loss = tf.math.reduce_mean(out)
        grads=tape.gradient(loss,image)
        grads = tf.math.l2_normalize(grads)
        image+=grads*10
        if (i+1) & verbose_step == 0:
            print(f'Iteration: {i+1}, Loss:{loss.numpy():.4f}')
    plot_image(image,f'{layer_name},{f_index}')
    
print([layer.name for layer in model.layers if 'conv' in layer.name])
layer_name='block2_conv2'
visualize_filter(layer_name)