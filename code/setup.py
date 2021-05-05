import os

strs = ('pip install mmcv==0.6.2')
os.system(strs)

strs = ('pip install terminaltables')
os.system(strs)

strs = ('cd models/py_utils/_cpools && python3 setup.py install --user')
os.system(strs)

strs = ('cd models/py_utils/roi_extractors/ops/roi_align && python3 setup.py install --user')
os.system(strs)

strs = ('cd data/coco/PythonAPI && python3 setup.py install')
os.system(strs)

strs = ('cd external && python3 setup.py install')
os.system(strs)

strs = ('cd models/py_utils/bbox/nms && python3 setup.py install --user')
os.system(strs)

# strs = ('pip install numpy==1.16.0')
# os.system(strs)

