import os, sys
from PIL import Image
import numpy as np 
from matplotlib import pyplot as plt

img = 'app/apple.jpg'
# img = 'huluobo61.jpg'

def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    
    size = 299, 299
    img.thumbnail(size, Image.ANTIALIAS)
    
#     img = img.resize((299,299))
    
    data = np.asarray(img, dtype="int32")
    return data

img_data = load_image(img)

# show image
plt.imshow(img_data, interpolation='nearest')
plt.show()


# load model
from keras.models import load_model
model_load = load_model('food_cate.hdf5')

# add one dimension
img_data = np.expand_dims(img_data, axis=0)
# print(img_data.shape)

# prediction
prediction = model_load.predict(img_data)

# print label
label_dict = {0: '苹果', 1: '香蕉', 2: '黄瓜', 3: '大白菜', 4: '大葱', 5: '胡萝卜', 6: '韭菜', 7: '梨', 8: '芒果', 9: '番茄', 10: '土豆', 11: '圣女果'}
label_idx = np.argmax(prediction)
predicted_label = label_dict.get(label_idx)
print(predicted_label)

top3 = np.array(prediction[0]).argsort()[-3:][::-1]
print("top3 are:")
for i in top3:
  print(label_dict.get(i))




def food_predict(string):

    return_data = dict()

    return_data.update({
        'mood_sub_type':{
            "E": ans[0]/10.0,
            "A": ans[1]/10.0,
            "C": ans[2]/10.0,
            "O": ans[3]/10.0,
            "N": ans[4]/10.0
        }
    })

    return_data.update({'mood_sub_result': 'E'})

    return return_data
