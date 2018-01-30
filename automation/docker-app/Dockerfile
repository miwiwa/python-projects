FROM docker-local.artifactory1.fyre.ibm.com/httpd

MAINTAINER Michael Walker miwalker@us.ibm.com

ADD war/*.war /home/exec/tomcat/webapps/swampup.war

CMD /bin/bash -c cd /home/exec; /home/exec/tomcat/bin/catalina.sh run
