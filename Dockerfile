FROM python:3.10

RUN yum -y install tar gzip zlib freetype-devel \
    gcc \
    ghostscript \
    lcms2-devel \
    libffi-devel \
    libimagequant-devel \
    libjpeg-devel \
    libraqm-devel \
    libtiff-devel \
    libwebp-devel \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
    tcl-devel \
    tk-devel \
    tkinter \
    which \
    xorg-x11-server-Xvfb \
    zlib-devel \
    && yum clean all

COPY requirements.txt ./

RUN python3.10 -m pip install -r requirements.txt
RUN pip uninstall -y pillow && CC="cc -mavx2" pip install -U --force-reinstall pillow-simd

# Copy the earlier created app.py file to the container
COPY app.py ./

# Download ResNet50 and store it in a directory
RUN mkdir model
RUN curl -L https://tfhub.dev/google/imagenet/resnet_v1_50/classification/4?tf-hub-format=compressed -o ./model/resnet.tar.gz
RUN tar -xf model/resnet.tar.gz -C model/
RUN rm -r model/resnet.tar.gz

# Download ImageNet labels
RUN curl https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt -o ./model/ImageNetLabels.txt

# Set the CMD to your handler
CMD ["app.lambda_handler"]