FROM openmandriva/cooker:latest
COPY MagicScript.sh /MagicScript.sh
RUN echo "LANG=en_US.UTF-8" | tee /etc/locale.conf && chmod +x /MagicScript.sh 
RUN dnf install -y \
    basesystem-build \
    bash \
    rpmdevtools \
    rpmlint \
    packaging-tools \
    man \
    locales-en \
    myspell-en \
    hunspell && \
    dnf clean all
ENTRYPOINT [ "/MagicScript.sh" ]
