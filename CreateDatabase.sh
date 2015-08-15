cp /etc/postgresql/9.3/main/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf_bck
cp pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
service postgresql restart
createuser wsss
createdb -e -O wsss wsss

