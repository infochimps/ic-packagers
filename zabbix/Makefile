# Requires password-less sudo

ARCHIVE=zabbix-2.0.4.tar.gz
URI=http://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Stable/2.0.4/$(ARCHIVE)

all: ~/rpmbuild/SOURCES/$(ARCHIVE) /usr/build/rpmbuild /usr/include/curl/curl.h
	rpmbuild -bb zabbix-agent.spec

~/rpmbuild/SOURCES/$(ARCHIVE):
	cd ~/rpmbuild/SOURCES; \
	wget $(URI)

/usr/include/curl/curl.h:
	sudo yum install curl-devel

/usr/build/rpmbuild:
	sudo yum install rpm-build

.PHONY: all
