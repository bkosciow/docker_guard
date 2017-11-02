People deploy dockers to servers and often forget to set everyting correctly. This script, when run on screen, checks if selected ports are forwarded. if yes it stops container.



Ports: '3306/tcp', '9200/tcp', '5601/tcp'

ToDo:
- external cfg
- unix service/deamon
