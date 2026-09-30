import pickle

# 打开.pkl文件
with open('/data3/2022/zcx/MotionAGFormer-master/h36m_sh_conf_cam_source_final.pkl', 'rb') as file:
    # 使用pickle模块加载文件中的对象
    obj = pickle.load(file)

# 打印对象的内容
print(obj["train"])