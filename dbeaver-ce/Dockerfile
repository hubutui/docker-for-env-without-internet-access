FROM debian:stable-slim

# install deps
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    fonts-noto-cjk \
    gnupg2 \
    libswt-gtk-4-java \
    wget \
    && rm -rf /var/lib/apt/lists/*
# add repo and install dbeaver-ce
RUN apt-get update \
    && wget -O - https://dbeaver.io/debs/dbeaver.gpg.key | apt-key add - \
    && echo "deb https://dbeaver.io/debs/dbeaver-ce /" > /etc/apt/sources.list.d/dbeaver.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    dbeaver-ce \
    && rm -rf /var/lib/apt/lists/*
# add database driver from dbeaver-ee tarball
RUN wget https://dbeaver.com/files/dbeaver-ee-latest-linux.gtk.x86_64.tar.gz \
    -O /tmp/dbeaver-ee.tar.gz \
    && mkdir /tmp/dbeaver-ee \
    && tar xfv /tmp/dbeaver-ee.tar.gz -C /tmp/dbeaver-ee --strip-components 1 \
    && mkdir /opt/dbeaver \
    && cp -a /tmp/dbeaver-ee/drivers /opt/dbeaver/drivers \
    && rm -rf /tmp/dbeaver-ee /tmp/dbeaver-ee.tar.gz
CMD dbeaver
