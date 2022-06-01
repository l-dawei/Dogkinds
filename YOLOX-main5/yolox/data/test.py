import os
import yolox
if __name__ == '__main__':
    yolox_path = os.path.dirname(os.path.dirname(yolox.__file__))
    yolox_path='/home/inspur/liudw/yolo'
    yolox_datadir = os.path.join(yolox_path, "datasets")
    print(yolox_path)
    print(yolox_datadir)
