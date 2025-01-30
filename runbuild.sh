mkdir -p ./rpmbuild/{SPECS,SOURCES,SRPMS,RPMS}
docker run -it --rm  -v ./rpmbuild:/rpmbuild cookme /bin/bash

