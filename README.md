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
	- ubuntu 16.04 keras.load_model 错误，内存开销大，2G内存卡死：

		```
		>>> from keras.models import load_model
		Using TensorFlow backend.
		>>> model = load_model('app/models/food_cate.hdf5')
		WARNING:tensorflow:From /home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
		Instructions for updating:
		Colocations handled automatically by placer.
		2019-05-30 15:45:51.267837: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
		2019-05-30 15:45:51.337513: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2399995000 Hz
		2019-05-30 15:45:51.338192: I tensorflow/compiler/xla/service/service.cc:150] XLA service 0x8cba7a0 executing computations on platform Host. Devices:
		2019-05-30 15:45:51.338217: I tensorflow/compiler/xla/service/service.cc:158]   StreamExecutor device (0): <undefined>, <undefined>
		Traceback (most recent call last):
			File "/usr/lib/python3.7/runpy.py", line 193, in _run_module_as_main
				"__main__", mod_spec)
			File "/usr/lib/python3.7/runpy.py", line 85, in _run_code
				exec(code, run_globals)
			File "/home/ubuntu/elephant/app/predict.py", line 14, in <module>
				model = load_model('app/models/food_cate.hdf5')
			File "/home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/keras/models.py", line 255, in load_model
				custom_objects=custom_objects)
			File "/home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/keras/optimizers.py", line 653, in deserialize
				printable_module_name='optimizer')
			File "/home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/keras/utils/generic_utils.py", line 141, in deserialize_keras_object
				return cls.from_config(config['config'])
			File "/home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/keras/optimizers.py", line 101, in from_config
				return cls(**config)
			File "/home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/keras/optimizers.py", line 371, in __init__
				super(Adam, self).__init__(**kwargs)
			File "/home/ubuntu/.local/share/virtualenvs/elephant-dt_Zz8No/lib/python3.7/site-packages/keras/optimizers.py", line 38, in __init__
				'passed to optimizer: ' + str(k))
		TypeError: Unexpected keyword argument passed to optimizer: amsgrad
		```