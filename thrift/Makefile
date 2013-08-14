# This script creates a .deb of Apache Thrift.
#
# To create the deb:
# 1. Spin up a new m1.small at EC2, Ubuntu Server 13.04 (Amazon default: ami-c30360aa)
# 2. scp this Makefile into 'ubuntu' user's home directory
# 3. sudo apt-get install make
# 4. make
#
# Some trivia.  There are some errors about 'source: not found' which are harmless.
# While the rbenv setup targets bash (the default shell for all users), make runs
# commands under /bin/sh, which Ubuntu hilariously symlinks to /bin/dash.  Lolz Ubuntu.

version=0.8.0
dir=thrift-$(version)
tarball=$(dir).tar.gz
download=http://archive.apache.org/dist/thrift/$(version)/$(tarball)

all: thrift-$(version)-x86_64.deb

thrift-$(version)-x86_64.deb: inst/usr/local/bin/thrift inst/usr/lib/ruby/gems/1.9.1/gems/thrift-$(version)/lib/thrift.rb /tmp/stamp-fpm
	. ~/.bash_profile; \
	cd inst; \
	fpm -s dir -t deb --name thrift --version $(version) --package ../thrift-$(version)-x86_64.deb --deb-user root --deb-group root .

# The ruby part of the thrift install target isn't DESTDIR-aware, and so 
# the gem has been installed under ~/.rbenv  Copy the wayward gem into DESTDIR
inst/usr/lib/ruby/gems/1.9.1/gems/thrift-$(version)/lib/thrift.rb: inst/usr/local/bin/thrift
	mkdir -p inst/usr/lib/ruby/gems/1.9.1/gems
	cp --archive ~/.rbenv/versions/1.9.3-p392/lib/ruby/gems/1.9.1/gems/thrift-$(version) inst/usr/lib/ruby/gems/1.9.1/gems

inst/usr/local/bin/thrift: inst $(dir)/compiler/cpp/thrift
	. ~/.bash_profile; \
	INST=$$(pwd)/inst; \
	cd $(dir); \
	make DESTDIR=$$INST install

inst:
	mkdir inst

/tmp/stamp-mongrel:
	. ~/.bash_profile; \
	if (gem install mongrel -v 1.2.0.pre2 --pre --no-rdoc --no-ri); then \
		~/.rbenv/bin/rbenv rehash; \
		touch /tmp/stamp-mongrel; \
	fi

/tmp/stamp-rspec:
	. ~/.bash_profile; \
	if (gem install rspec -v 1.3.2); then \
		~/.rbenv/bin/rbenv rehash; \
		touch /tmp/stamp-rspec; \
	fi

# From https://github.com/infochimps-labs/ironfan/wiki/INSTALL
/home/ubuntu/.rbenv/bin/rbenv:
	sudo apt-get install --yes git libxml2-dev libxslt1-dev libreadline-dev zlib1g-dev libssl-dev
	sudo apt-get remove clang
	git clone git://github.com/sstephenson/rbenv.git ~/.rbenv
	echo 'export PATH="$$HOME/.rbenv/bin:$$PATH"' >> ~/.bash_profile
	git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
	echo 'eval "$$(rbenv init -)"' >> ~/.bash_profile
	~/.rbenv/bin/rbenv init -
	~/.rbenv/bin/rbenv install 1.9.3-p392
	~/.rbenv/bin/rbenv global 1.9.3-p392 

/tmp/stamp-fpm:
	. ~/.bash_profile; \
	if (gem install fpm); then \
		~/.rbenv/bin/rbenv rehash; \
		touch /tmp/stamp-fpm; \
	fi

$(tarball):
	wget $(download)

/usr/bin/g++:
	sudo apt-get install --yes g++

$(dir)/Makefile: $(tarball) /usr/bin/g++ /home/ubuntu/.rbenv/bin/rbenv
	. ~/.bash_profile; \
	tar xf $(tarball); \
	cd $(dir); \
	./configure

/usr/include/python2.7/Python.h:
	sudo apt-get install --yes python-dev

$(dir)/compiler/cpp/thrift: $(dir)/Makefile /usr/include/python2.7/Python.h /tmp/stamp-rspec /tmp/stamp-mongrel
	. ~/.bash_profile; \
	cd $(dir); \
	make

clean:
	rm -rf ~/.rbenv $(dir) $(tarball) inst /tmp/stamp-* thrift-$(version)-x86_64.deb ~/.bash_profile

.PHONY: all clean
