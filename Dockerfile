FROM confluentinc/cp-kafka-connect-base:6.2.1

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.2.5

# # copy properties
# COPY worker.properties .
# COPY connector.properties.d/ connector.properties.d

# copy entrypoint script
COPY entrypoint.sh .

ENTRYPOINT [ "bash", "entrypoint.sh" ]