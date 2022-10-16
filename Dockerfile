FROM python:3.7.3-stretch

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
# COPY . wiki_api.py /app
COPY wiki_api.py /app
COPY requirements.txt requirements.txt

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt
# RUN python3 install --upgrade pip &&\
#       pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

## Step 4:
EXPOSE 80

## Step 5:
# Run app.py at container launch
CMD [ "python3", "wiki_api.py"]