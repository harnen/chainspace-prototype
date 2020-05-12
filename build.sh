virtualenv -p `which python2` .chainspace.env

source .chainspace.env/bin/activate

pip2 install --editable chainspacecontract

mvn -Dversion=1.0-SNAPSHOT package assembly:single

