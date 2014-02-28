ic-packagers
============

A handful of scripts for creating debs for some infochimps platform recipes

Some scripts have manual prerequisites in comments at the top.

The scripts build on stock EC2 Ubuntu Server 13.04 64-bit (t1.micro is ample).

ATTENTION!!! Make sure zeromq is built first and installed using 
dpkg -i zeromq-X.Y.Z-amd64.deb otherwise jzmq build will fail 
