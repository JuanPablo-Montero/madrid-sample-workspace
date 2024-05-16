# Use the latest Python 3.12 image as the base
FROM python:3.12

# Create the /opt/liferay directory
RUN mkdir -p /opt/liferay

# Set the working directory inside the container
WORKDIR /opt/liferay

#COPY requirements.txt .
#COPY python.py .
COPY . /opt/liferay

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "app.py"]
