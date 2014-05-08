Summary: The qt toolkit, Infochimps build
Name: qt-all
Version: 4.8.6
Release: 1
License: GPL3
Group: frameworks
URL: http://qt-project.org
Source0: %{name}-everywhere-opensource-src-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The qt UI toolkit

%prep
tar xf ../SOURCES/qt-everywhere-opensource-src-4.8.6.tar.gz

%build
cd qt-everywhere-opensource-src-4.8.6
./configure -prefix /usr -opensource -webkit
make

%install
rm -rf $RPM_BUILD_ROOT
cd qt-everywhere-opensource-src-4.8.6
make INSTALL_ROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr/*

%changelog
* Tue May  6 2014 Erik Mackdanz <erikmack@rpmbuild> - 
- Initial build.

