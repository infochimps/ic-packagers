Summary: The thrift serialization framework
Name: thrift
Version: 0.9.1
Release: 1
License: Apache
Group: data
URL: http://thrift.apache.org
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: boost boost-devel python python-devel
Requires: boost boost-devel python python-devel

%description
Serialize!

%prep
tar xf ../SOURCES/thrift-0.9.1.tar.gz

%build
cd thrift-0.9.1
# Skip tests due to http://stackoverflow.com/questions/18643642/libtool-error-building-thrift-0-9-1-on-ubuntu-13-04
# Skip ruby for now since install step fails
./configure --without-tests --without-ruby
make

%install
rm -rf $RPM_BUILD_ROOT
cd thrift-0.9.1
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr/*

%changelog
* Wed May  7 2014 Erik Mackdanz <erikmack@rpmbuild> - 
- Initial build.

