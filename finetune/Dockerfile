FROM nvcr.io/nvidia/rapidsai/rapidsai:22.12-cuda11.5-runtime-ubuntu20.04-py3.8
WORKDIR /notebooks
ADD ./requirements.txt /notebooks/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt