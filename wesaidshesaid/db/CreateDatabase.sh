#Run with sudo -u postgres ./CreateDatabase.sh

#Script modifies postgres configuration to enable passwordless access for all users on the local system
#Creates a database called wsss owned by wsss
#Use following command to access database via sql command line.
#psql -U wsss



cp /etc/postgresql/9.3/main/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf_bck
cp pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
service postgresql restart
createuser wsss
createdb -e -O wsss wsss

