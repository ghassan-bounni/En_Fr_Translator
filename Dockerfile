FROM python:3.9

# Create the working directory
RUN set -ex && mkdir /enfr_translator
WORKDIR /enfr_translator

# Install Python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the relevant directories
COPY model/ ./model
COPY . ./

# Run the web server
EXPOSE 8000
ENV PYTHONPATH /enfr_translator
CMD python /enfr_translator/app.py
