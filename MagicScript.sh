#!/bin/bash
mkdir /tmp/BuildDir
mount --bind /tmp/BuildDir /root/rpmbuild/BUILD
dnf builddep -y $1
rpmbuild -ba $1