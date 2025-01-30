FROM openmandriva/cooker:latest
RUN dnf install -y basesystem-build bash rpmdevtools rpmlint packaging-tools man
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
