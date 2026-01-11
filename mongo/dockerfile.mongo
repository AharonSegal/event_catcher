FROM mongo:7.0

ENV MONGO_INITDB_ROOT_USERNAME=admin \
    MONGO_INITDB_ROOT_PASSWORD=adminpassword \
    MONGO_INITDB_DATABASE=events_db

EXPOSE 27017

CMD ["mongod", "--bind_ip", "0.0.0.0"]

# - Build image:  
#   `docker build -f Dockerfile.mongo -t event-catcher .`
# - Run container:  
#   `docker run -d -p 27017:27017 --name sdf-mongo event-catcher`