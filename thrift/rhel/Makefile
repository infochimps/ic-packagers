# Requires password-less sudo

ARCHIVE=thrift-0.9.1.tar.gz
URI=http://apache.mirrors.tds.net/thrift/0.9.1/$(ARCHIVE)

all: ~/rpmbuild/SOURCES/$(ARCHIVE)
	rpmbuild -bb thrift.spec

~/rpmbuild/SOURCES/$(ARCHIVE): /usr/build/rpmbuild
	cd ~/rpmbuild/SOURCES; \
	wget $(URI)

/usr/build/rpmbuild:
	sudo yum install rpm-build

.PHONY: all prereq