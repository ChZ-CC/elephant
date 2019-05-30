from PIL import Image
from keras.models import load_model
from urllib.request import urlopen
from io import BytesIO
import numpy as np


LABLE_MAP = {
    0: '苹果', 1: '香蕉', 2: '黄瓜', 3: '大白菜', 
    4: '大葱', 5: '胡萝卜', 6: '韭菜', 7: '梨', 
    8: '芒果', 9: '番茄', 10: '土豆', 11: '圣女果',
}
# 加载模型
model = load_model('app/models/food_cate.hdf5')


def predict(image_url):
    """
    args: image_url: 图片url
    return: (name, confidence)
    """

    # 从url获取图片数据
    try:
        fp = BytesIO(urlopen(image_url).read())
    except:
        raise IOError
    
    # 格式化图片数据
    img = Image.open(fp)
    img.load()

    img.thumbnail((299, 299), Image.ANTIALIAS)
    img = img.resize((299,299))

    img_data = np.asarray(img, dtype='int32')
    img_data = np.expand_dims(img_data, axis=0)
    
    # 预测，并返回结果
    prediction = model.predict(img_data)
    
    index, confidence = np.argmax(prediction), np.amax(prediction)
    return LABLE_MAP.get(index), confidence


if __name__ == "__main__":
    url = 'http://img.9ku.com/geshoutuji/singertuji/2/2293/2293_2.jpg'
    print(predict(url))
