# Need password-less sudo.  Also note that the configure step is
# forced interactive

ARCHIVE=qt-everywhere-opensource-src-4.8.6.tar.gz
URI=http://download.qt-project.org/official_releases/qt/4.8/4.8.6/$(ARCHIVE)

all: ~/rpmbuild/RPMS/x86_64/qt-all-4.8.6-1.x86_64.rpm

~/rpmbuild/RPMS/x86_64/qt-all-4.8.6-1.x86_64.rpm: ~/rpmbuild/SOURCES/$(ARCHIVE) /usr/bin/g++ /usr/lib64/pkgconfig/xext.pc /usr/lib64/pkgconfig/xrender.pc
	rpmbuild -bb qt-all.spec

~/rpmbuild/SOURCES/$(ARCHIVE): ~/rpmbuild/SOURCES
	cd ~/rpmbuild/SOURCES && wget $(URI)

~/rpmbuild/SOURCES:
	sudo yum install --assumeyes rpm-build

/usr/bin/g++:
	sudo yum install --assumeyes gcc-c++

/usr/lib64/pkgconfig/xext.pc:
	sudo yum install --assumeyes libXext-devel

/usr/lib64/pkgconfig/xrender.pc:
	sudo yum install --assumeyes libXrender-devel

.PHONY: all

