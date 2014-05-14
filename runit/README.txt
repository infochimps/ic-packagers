The runit rpm that's in our repo, we didn't build from here.  To build
it, launch an instance using a new (>=2.x) runit cookbook from the
opscode community cookbook site.  This cookbook builds the rpm, and
leaves it under /root/rpmbuild/RPMS.  Then revert to the older runit 
cookbook :-(
