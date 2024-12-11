# Open the docker app and run the following commands:
# TO BUILD THE IMAGE FOR YOUR PLATFORM: 
#
# docker build -t REPO-NAME .
#
# TU RUN THE DOCKER CONTAINER: 
#
# docker run -p PORT:PORT REPO-NAME
#
#
# TO PUSH THE IMAGE TO DOCKER HUB:
# docker login
#
# docker tag REPO-NAME:latest ACCOUNT-NAME/REPO-NAME:latest
#
# docker push ACCOUNT-NAME/REPO-NAME:latest
#
#
#
# TO BUILD THE IMAGE FOR MULTIPLE PLATFORMS:
# First create the builder for the multiplatform image if not exixt.
# Use the following command to see if exit:
#
# docker buildx ls
#
# If not create and activate it with:
#
# docker buildx create --name BUILDER-NAME
#
# docker buildx use BUILDER-NAME
#
# docker buildx inspect --bootstrap
#
# The create on docker hub the repository if you want to deploy if not skip
# Suppose you want to deploy and the repo is colled REPO-NAME Now you can build the image with the following command:
# Remember the point at the end in the row below --push \
#
# docker buildx build --platform linux/amd64,linux/arm64 -t ACCOUNT-NAME/REPO-NAME:latest --push .
#
# If you want it locally instead (maybe):
#
# docker buildx build --platform linux/amd64,linux/arm64 -t REPO-NAME --pull .
#
#

# Use a platform-neutral base image
FROM python:3.9 AS base

# Install required system packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory in the container
WORKDIR /TelegramBot-AmazonOffers

# Copy the current directory contents into the container at /app
COPY . /TelegramBot-AmazonOffers

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask application
EXPOSE 8000

# Run main.py when the container launches
CMD ["python", "src/main.py"]
