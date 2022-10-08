FROM python:3.9

# Create the working directory
RUN set -ex && mkdir /en_fr_translator
WORKDIR /en_fr_translator

# Install Python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the relevant directories
COPY model/ ./model
COPY . ./

# Run the web server
EXPOSE 8000
ENV PYTHONPATH /en_fr_translator
CMD python /en_fr_translator/app.py
