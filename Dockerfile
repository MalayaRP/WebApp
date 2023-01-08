FROM python:3.8
CMD mkdir /molecule_vis
COPY . /molecule_vis
WORKDIR /molecule_vis

EXPOSE 8501
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD streamlit run app.py