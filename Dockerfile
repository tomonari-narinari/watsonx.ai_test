FROM python:3.9
RUN pip install numpy
ENV PORT=8080
EXPOSE 8080
