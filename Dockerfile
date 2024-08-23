FROM registry.redhat.io/rhel8/python-312:1-24.1724033887
COPY ./* .
RUN pip install flask
EXPOSE 8088
CMD python main.py