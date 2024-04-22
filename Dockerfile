# Base image
FROM python:3.12-slim

# Add 'app_user' and use it instead of root, for better security
RUN useradd --create-home --shell /bin/bash app_user

# Set working directory
WORKDIR /home/app_user/app

# Copy requirements file
COPY requirements.txt ./

# Install requirements from the file
RUN pip install -r requirements.txt

# Create 'data' directory
RUN mkdir data

# Change owner of the 'data' directory to 'app_user'
RUN chown -R app_user:app_user data

# Switch to the newly created user
USER app_user

# Copy all files from current local directory, to the docker container
COPY --chown=app_user:app_user . .

# Set bash as default command which will be invoked when the container runs
CMD [ "bash" ]