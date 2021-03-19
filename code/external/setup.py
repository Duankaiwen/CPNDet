import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "nms", 
        ["nms.pyx"]
    )
]

setup(
    name="coco",
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]
)
