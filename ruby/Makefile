# Run as normal user with password-less sudo

PKG=ruby-1.9.3-p545
URI="http://cache.ruby-lang.org/pub/ruby/1.9/$(PKG).tar.gz"

all: ~/rpmbuild/RPMS/x86_64/$(PKG)-1.x86_64.rpm

~/rpmbuild/RPMS/x86_64/$(PKG)-1.x86_64.rpm: ~/rpmbuild/BUILDROOT/$(PKG)-1.x86_64/usr/bin/ruby
	rpmbuild -bb ruby.spec

~/rpmbuild/BUILDROOT/$(PKG)-1.x86_64/usr/bin/ruby: ~/rpmbuild/BUILD/$(PKG)/ruby
	rpmbuild -bi ruby.spec

~/rpmbuild/BUILD/$(PKG)/ruby: ~/rpmbuild/BUILD/$(PKG) /usr/bin/gcc
	rpmbuild -bc ruby.spec

~/rpmbuild/BUILD/$(PKG): /usr/bin/rpmbuild ~/rpmbuild/SOURCES/$(PKG).tar.gz
	rpmbuild -bp ruby.spec

~/rpmbuild/SOURCES/$(PKG).tar.gz:
	cd ~/rpmbuild/SOURCES && wget $(URI)

/usr/bin/rpmbuild:
	sudo yum install --assumeyes rpm-build

/usr/bin/gcc:
	sudo yum install --assumeyes gcc

clean:
	rm -rf $(PKG)

.PHONY: all clean