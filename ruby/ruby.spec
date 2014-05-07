Summary: Be a rock star
Name: ruby
Version: 1.9.3.p545
Release: 1
License: BSD
Group: Productivity
URL: http://ruby-lang.org
Source0: %{name}-1.9.3-p545.tar.gz
BuildRoot: %{_tmppath}/%{name}-1.9.3-p545-root

%description
Such require.  Wow.

%prep
tar xf ../SOURCES/ruby-1.9.3-p545.tar.gz

%build
cd ruby-1.9.3-p545
echo "Im in $PWD"
./configure --prefix=/usr --disable-install-doc --enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT
cd ruby-1.9.3-p545
echo "Im in $PWD"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr/*

%changelog
* Tue May  6 2014 Erik Mackdanz <erikmack@rpmbuild> - 
- Initial build.

