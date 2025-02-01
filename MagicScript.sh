#!/bin/bash
dnf builddep -y $1
rpmbuild -ba $1