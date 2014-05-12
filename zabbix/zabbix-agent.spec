Summary: An agent which sends monitoring information to a zabbix server
Name: zabbix-agent
Version: 2.0.4
Release: 1
License: GPL
Group: monitoring
URL: http://zabbix.com
Source0: zabbix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libcurl-devel
Requires: libcurl

%description
Monitor things

%prep
tar xf %SOURCE0

%build
cd zabbix-%version
./configure --prefix=/usr --sysconfdir=/etc/zabbix --localstatedir=/var --enable-agent --with-libcurl
make

%install
rm -rf $RPM_BUILD_ROOT
cd zabbix-%version
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/*
/etc/*

%changelog
* Sat May 10 2014 Erik Mackdanz <erikmack@rpmbuild> - agent-1
- Initial build.

