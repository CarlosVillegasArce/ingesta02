FROM python:3-slim
WORKDIR /programas/ingesta

# Instalamos las librerías necesarias: 
# - boto3 (S3)
# - pandas (Manejo de datos)
# - mysql-connector-python (Conexión a la BD)
RUN pip3 install boto3 pandas mysql-connector-python

COPY . .

CMD [ "python3", "./ingesta.py" ]