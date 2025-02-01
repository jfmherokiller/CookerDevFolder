mkdir -p ./rpmbuild/{SPECS,SOURCES,SRPMS,RPMS}
docker run -it --rm  -v ./rpmbuild:/root/rpmbuild cookme /root/rpmbuild/SPECS/$1
