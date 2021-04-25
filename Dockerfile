FROM python:3.8

COPY . .

WORKDIR /TinderPlusPlus

RUN pip install -r requirements.txt

CMD ["pipenv", "run", "jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
CMD ["python", "app.py"]