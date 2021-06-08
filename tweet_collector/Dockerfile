FROM python:3.8-slim
WORKDIR /app                
                                #   create a file called app
COPY requirements.txt /app
                                #   fill the app with the requiremnts
RUN pip install --trusted-host pypi.python.org -r requirements.txt
                                #   install the imports, to create an environment which all can use instantly
CMD ["python", "collector.py"]
                                # to run the file inside the src folder


# check the comments, there are probaply wrong!!!!