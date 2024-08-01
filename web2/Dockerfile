# Use an official Python runtime as a parent image
FROM python:slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-deps --user --no-cache-dir -r requirements.txt && \ 
    find ~/.local \( -type d -a -name test -o -name tests \) -exec rm -rf '{}' \+ && \
    rm -rf /root/.cache

# Copy the application code
COPY app.py .
# Command to run the application
CMD ["python", "app.py"]