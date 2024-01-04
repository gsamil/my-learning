# Apache Kafka

These are my notes from the Confluent Apache Kafka Tutorials | Kafka 101 playlist.

## Introduction

- Apache Kafka is a distributed streaming platform to collect, store and process real-time data streams at scale.
- It has numerous use cases, including distributed logging, stream processing and Pub-Sub Messaging.

### Event

- An event is a record of something that has happened in the past. It is a fact.
- It's a combination of notification and a state
- An event in Kafka is modeled as a key-value pair.
- `Topics` are primary components of storage in Kafka.
- Events are immutable.

### Topic

- Fundemanetal unit of organization for the events in Kafka.
- Durable logs of events.
- Can only seek by offset, not indexed.
- Retention period is configurable.
- Producing to and consuming from a topic is done through a Kafka `broker`.

### Partition

- `Topics` are broken down into partitions.
- When we write a `message` to a topic, it is written to one of the partitions of the topic.
- Partition that it's routed to is based on the `key` of the message.
- Each partition can in a separate `node` in a Kafka `cluster`.

### Broker

- Kafka is a distributed system that consists of machines called `brokers`.
- Each broker hosts some set of `partitions` and handles incoming requests for producing and consuming messages.
- Brokers also handles `replication` of partitions across the cluster.

### Replication

- We need to copy partition data to several other brokers to keep it safe.
- Those copies are called follower replicas.
- Whereas the main partition is called the leader replica.
- In general, writing and reading is done from the leader replica.
- Tunable in the `producer`.

### Producer

- Applications that use Kafka are producers and consumers.

### Consumer

- ConsumerRecords are returned from a call to poll on a Consumer.
- Reading a message doesn't delete it from the topic.
- Scaling consumers is automatic.

## Broader Kafka Ecosystem

- Things like Kafka Connect, Kafka Streams, KSQL, Schema Registry, etc. are all examples of infrastructure code.

### Kafka Connect

- Ecosystem of pluggable connectors 
- Data integration system and ecosystem
- An application running outside the cluster

  ```
  Data Source -> Kafka Connect -> Cluster -> Kafka Connect -> Data Sink
  ```

- Horizaontally scalable
- Fault tolerant
- A connect worker which is one of these nodes in the connect cluster runs one or more connectors
- A connector is a plugable component that's responsible for interfacing with that external system
  - Source connector - reads data from an external system and writes it to Kafka (producer)
  - Sink connector - reads data from Kafka and writes it to an external system (consumer)
- Reading from a relational database, getting messages from Twitter, a legacy htfs file system, etc. these are all same operations no matter application

**Note :** This type of code is called undifferentiated code or infrastructure code. It's not the core business logic of the application. It's not what makes the application unique. It's not what makes the application valuable. It's just the code that's necessary to get the application to work.

### Schema Registry

- New consumers will emerge over time
- Consumers need to know how to interpret the data (format of the messages in the topic)
- Schema Registry is a standalone service process that maintains a database of schemas
- Database is persisted in an internal Kafka topic, and it's cached in Schema Registry for low latency access
- When producer wants to write a new message, it first checks the Schema Registry if it's the same with the previous one
- Schema registry currently supports 3 serialization formats: Avro, JSON and Protobuf


### Kafka Streams

- Kafka Streams is a stream processing API that's built into Kafka
- Filtering, grouping, aggregating, joining, etc.
- Scalable, fault tolerant state management
- It's a library, not an infrastructure

### ksqlDB

- ksqlDB is a SQL-like language for Kafka Streams
- Database optimized for stream processing
- Run on its own scalable, fault tolerant cluster adjacent to Kafka cluster
- Provides an integration with Kafka Connect

## References

- [Confluent Kafka 101 - Youtube Watchlist](https://youtube.com/playlist?list=PLa7VYi0yPIH0KbnJQcMv5N9iW8HkZHztH&si=eHXuwLYpMdiJnnXM)
