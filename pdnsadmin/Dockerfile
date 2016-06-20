FROM debian:jessie

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y git python-pip python-dev python-mysqldb libmysqlclient-dev libsasl2-dev libldap2-dev libssl-dev mysql-client \
 && apt-get clean

ENV BIND_ADDRESS="0.0.0.0" \
    BIND_PORT="9393" \
    SECRET_KEY='We are the world' \
    PDNS_STATS_URL='http://172.16.214.131:8081/' \
    PDNS_API_KEY='An API key' 

RUN git clone https://github.com/ngoduykhanh/PowerDNS-Admin.git /opt/pdnsadmin \
 && cd /opt/pdnsadmin \
# && git checkout new_ui \
 && pip install virtualenv \
 && virtualenv flask \
 && . ./flask/bin/activate \
 && pip install -r requirements.txt 

ADD config.py /opt/pdnsadmin/

ADD start.sh /usr/local/bin/start.sh

RUN chmod +x /usr/local/bin/start.sh

WORKDIR /opt/pdnsadmin 
EXPOSE $BIND_PORT

CMD ["/usr/local/bin/start.sh"]
