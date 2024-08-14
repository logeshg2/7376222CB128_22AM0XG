# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /Day2

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# RUN python.exe -m pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 scikit-learn

# Run the script when the container launches
CMD ["python", "./app.py"]
