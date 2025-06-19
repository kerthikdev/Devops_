1. the flask app create the log , when we reach the localhost:5001 , 
2. the log will be created in /var/log/flaskapp/flaskapp.log
3. the filebeat will read the log and sent it to the logstash
4. the logstash will parse the log and sent it to elasticsearch 
5. the elasticsearch will store the log and we can see it in kibana
6. kibana will show the log in the dashboard 

filebeat => logstash => elasticsearch => kibana
Flask App → Writes logs → Filebeat → Forwards logs → Logstash → Parses logs → Elasticsearch → Stores logs → Kibana → Visualizes logs


