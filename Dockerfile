FROM nvcr.io/nvidia/pytorch:24.09-py3
RUN pip install flask paramiko web3 py-snark whisper-ngx
COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
