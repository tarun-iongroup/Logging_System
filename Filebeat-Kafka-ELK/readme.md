# Readme
Important files for the Filebeat-Kafka-Filebeat-ELK Setup.

- filebeat_test1.yml: Connects S3 to Kafka
- filebeat_test2.yml: Connects Kafka(Topic-1) to Logstash 
- filebeat_test3.yml: Connects Kafka(Topic-2) to Logstash
- first-pipeline.conf: Logstash config file, Connects Logstash to Elasticsearch
- Status: Everything working on the Localhost.


Config files:
- Contains the new Filebeat config files(kafka-filebeat-logstash) which are present in the Server.
- Status: Problem - Able to view the output on the Filebeat console, but unable to send the output to Logstash server.
