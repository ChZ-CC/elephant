from app import app
from flask import request, jsonify
from config import Config
import json

try:
    from image_predict import predict, ModelLoadError
except Exception as e:
    app.logger.error(e)


@app.route('/image-predict', methods=['POST'])
def image_predict():
    app.logger.info('request for /image-predict')
    image_url = request.json.get('image_url')
    key = request.json.get('key')
    response_data = {}

    if key != Config.SECRET_KEY:
        code, message = 401, 'Unauthorized'
    elif image_url:
        try:
            result, confidence = predict(image_url)
            response_data.update(dict(
                name=result,
                num=float(confidence),
            ))
            code, message = 0, 'success' 
        except IOError:
            code, message = 403, 'image_url not accessable'
        except ModelLoadError:
            code, message = 504, 'fail to load model'
        except Exception as e:
            app.logger.error(e)
            code, message = 503, 'Image Recognition failed'
        
    else:
        code, message = 400, 'image_url required'

    return jsonify(code=code, message=message, data=response_data)
