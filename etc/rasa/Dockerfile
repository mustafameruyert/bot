# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.0

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
#RUN pip install --no-cache-dir google
RUN apt-get update && apt-get install -y git
RUN git clone https://git.dar.kz/DRysbek/qa.git
CMD [ "python3", "qa/setup_qa.py" ]
# Copy actions folder to working directory
#COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001

# Extend the official Rasa SDK image
#FROM rasa/rasa-sdk:1.10.0
# Use subdirectory as working directory
#WORKDIR /app
# Copy any additional custom requirements, if necessary (uncomment next line)
#COPY actions/requirements-actions.txt ./
# Change back to root user to install dependencies
#USER root
# Install extra requirements for actions code, if necessary (uncomment next line)
#RUN pip install --no-cache-dir google
# Copy actions folder to working directory
#COPY ./actions /app/actions
#COPY creds.json /app
# By best practices, don't run the code with root user
#USER 1001
#CMD ["start", "--actions", "actions.actions"]