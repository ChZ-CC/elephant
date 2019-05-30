#### API

- 接口：`http://host/image-predict`

	```json
	// post
	{
    "image_url": "http://img.9ku.com/geshoutuji/singertuji/2/2293/2293_2.jpg",
    "key": "SECRET_KEY"
	}

	// response
	{
	    "code": 0,
	    "data": {
				"name": "苹果",
				"num": 0.999
				}
	    },
	    "message": "success"
	}	
	
	// code:
	// 0				success	--成功
	// 401			Unauthorized -- 缺少key
	// 503			Image Recognition failed -- 模型失败
	// 400 			image_url required -- 缺少参数
	```

#### 算法接口

- function: `app/image_prediction/predict.predict`
- model 目录: `app/models/xxx.hdf5`

	```
	# 进入项目目录，启动python环境
	$ cd elephant
	$ pipenv shell

	# 测试接口
	(elephant)$ python -m app.predict 		# == python app/predict.py
	# output 省略一大片提示信息
	('苹果', 0.61621004)
	```

---

**问题**

1. 直接运行 `python app.predict.py` 可以正确执行，但是在 flask 环境下调用，报错：`Tensor Tensor("dense_6/Softmax:0", shape=(?, 12), dtype=float32) is not an element of this graph.`
	
	- 附双生的解决方法：
		
		```
		Cannot interpret feed_dict key as Tensor: Tensor Tensor("Placeholder_2:0", shape=(50, 200), dtype=float32) is not an element of this graph.

		解决办法：
		keras.backend.clear_session()
		```

2. 环境问题：

	- ubuntu 14.04 tensorflow 安装成功，运行报错：`ImportError: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.23' not found (required by /root/.local/share/virtualenvs/elephant-FLgR8YHo/lib/python3.7/site-packages/tensorflow/python/_pywrap_tensorflow_internal.so)`
	- ubuntu 16.04 tensorflow 安装成功，import 