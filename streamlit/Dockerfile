FROM python:3.9-slim-buster

RUN mkdir /streamlit

# Working Directory
WORKDIR /streamlit

# Copy source code to working directory
COPY . /streamlit


# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8501


CMD ["streamlit", "run","UI_app.py"]