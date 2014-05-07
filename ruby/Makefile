# Run as normal user with password-less sudo

PKG=ruby-1.9.3-p545
URI="http://cache.ruby-lang.org/pub/ruby/1.9/$(PKG).tar.gz"
BUILDDEPS=/usr/bin/gcc \
	/usr/bin/rpmbuild \
	~/rpmbuild/SOURCES/$(PKG).tar.gz \
	/usr/include/yaml.h \
	/usr/include/openssl/ssl.h

all: ~/rpmbuild/RPMS/x86_64/$(PKG)-1.x86_64.rpm

/usr/include/yaml.h: /etc/yum.repos.d/epel.repo
	sudo yum install --assumeyes libyaml-devel

/usr/include/openssl/ssl.h:
	sudo yum install --assumeyes openssl-devel

/etc/yum.repos.d/epel.repo:
	cd /tmp; \
	wget http://mirror.pnl.gov/epel/6/i386/epel-release-6-8.noarch.rpm; \
	sudo rpm -i epel-release-6-8.noarch.rpm; \
	sudo yum makecache

~/rpmbuild/RPMS/x86_64/$(PKG)-1.x86_64.rpm: $(BUILDDEPS)
	rpmbuild -bb ruby.spec

dirinst: $(BUILDDEPS)
	rpmbuild -bi ruby.spec

compile: $(BUILDDEPS)
	rpmbuild -bc ruby.spec

prep: $(BUILDDEPS)
	rpmbuild -bp ruby.spec

~/rpmbuild/SOURCES/$(PKG).tar.gz:
	cd ~/rpmbuild/SOURCES && wget $(URI)

/usr/bin/rpmbuild:
	sudo yum install --assumeyes rpm-build

/usr/bin/gcc:
	sudo yum install --assumeyes gcc

clean:
	rm -rf $(PKG)

.PHONY: all clean dirinst compile prep