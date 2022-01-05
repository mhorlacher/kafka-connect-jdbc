# kafka-connect-jdbc

This is a dockerized version of the Confluent JDBC database connector. 


## Usage

This image is running the `connect-standalone` command with a given `worker.properties` and one more more `connector.properties` files. 
Worker properties can be mounted to `/worker.properties`, while a directory of one or more connector properties can be mounted to `/connector.properties.d`. 


## Minimal Working Example

A minimal working *docker-compose* example of kafka-connect-jdbc (including zookeeper, kafka and postgresql) is provided 
in the `example/` directory. 

1. Clone repository
```
git clone https://github.com/mhorlacher/kafka-connect-jdbc.git
```

2. Navigate to the example directory
```
cd kafka-connect-jdbc/example
```

3. Run the example via *docker-compose*
```
docker-compose up
```

4. Connect to the postgresql database (with password *toor*)
```
psql -h localhost -p 5432 -U postgres -d postgresdb
```

5. Confirm that messages are written to the *test* table
```
SELECT * FROM test;
```


---

*Version 0.4.0*