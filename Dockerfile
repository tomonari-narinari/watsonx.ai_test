FROM python:slim
ADD ./test.py /root/test.py
WORKDIR /root
RUN apt update
RUN pip install sdcclient
RUN pip install sendgrid
CMD ["python","/root/test.py"]