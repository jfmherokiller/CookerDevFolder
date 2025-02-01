FROM openmandriva/cooker:latest
RUN dnf install -y basesystem-build bash rpmdevtools rpmlint packaging-tools man
COPY MagicScript.sh /MagicScript.sh
RUN chmod +x /MagicScript.sh
ENTRYPOINT [ "/MagicScript.sh" ]
