FROM python:3.9
RUN pip install numpy
ADD app /app
ENV PORT=8080
EXPOSE 8080
