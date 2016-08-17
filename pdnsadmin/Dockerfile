FROM debian:jessie

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y git python-pip python-dev python-mysqldb libmysqlclient-dev libsasl2-dev libldap2-dev libssl-dev mysql-client \
 && apt-get clean

ENV BIND_ADDRESS="0.0.0.0" \
    BIND_PORT="9393" \
    SECRET_KEY='We are the world' \
    PDNS_STATS_URL='http://localhost:8081/' \
    PDNS_API_KEY='An API key' \
    LOGIN_TITLE='PDNS' \
    TIMEOUT='10' \
    LOG_LEVEL='DEBUG' \
    LDAP_TYPE='none' \
    LDAP_URI='' \
    LDAP_USERNAME='' \
    LDAP_PASSWORD='' \
    LDAP_SEARCH_BASE='' \
    LDAP_USERNAMEFIELD='uid' \
    LDAP_FILTER='(objectClass=inetorgperson)' \
    PDNS_VERSION='3.4.7' 

RUN git clone https://github.com/ngoduykhanh/PowerDNS-Admin.git /opt/pdnsadmin \
 && cd /opt/pdnsadmin \
 && pip install virtualenv \
 && virtualenv flask \
 && . ./flask/bin/activate \
 && pip install mysql-python \ 
 && pip install -r requirements.txt 

ADD config.py /opt/pdnsadmin/

ADD start.sh /usr/local/bin/start.sh

RUN chmod +x /usr/local/bin/start.sh

WORKDIR /opt/pdnsadmin 
EXPOSE $BIND_PORT

CMD ["/usr/local/bin/start.sh"]
