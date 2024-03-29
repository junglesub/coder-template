FROM ubuntu:jammy

# Change Apt Mirror to Korea
COPY change-ubuntu-mirror.sh /
RUN bash /change-ubuntu-mirror.sh

# Install dependencies
RUN apt-get update \
	&& apt-get install -y \
	curl \
	git \
	sudo \
	vim \
	wget

# Install Node

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
apt-get install -y nodejs

# Install MariaDB
RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash && \
apt-get install -y mariadb-server mariadb-client
#RUN service mariadb start && \
#    mysql -e "DROP USER ''@'localhost'" && \
#    mysql -e "DROP USER ''@'$(hostname)'" && \
#    mysql -e "DROP DATABASE test" && \
#    mysql -e "FLUSH PRIVILEGES" && \
#    service mariadb stop

# Install Caddy
RUN apt install -y debian-keyring debian-archive-keyring apt-transport-https && \
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg && \
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list && \
    apt update && \
    apt install -y caddy

# Move Caddy Config (Caddyfile)
COPY Caddyfile /etc/caddy/

# Move caddy service file
COPY caddy /etc/init.d/caddy
RUN chmod +x /etc/init.d/caddy

# Install phpmyadmin
RUN apt-get update && \
    apt-get -y install software-properties-common && \
    add-apt-repository -y ppa:ondrej/php && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata && \
    apt-get install -y php8.2 \
                       php8.2-fpm \
                       php8.2-cli \
                       php8.2-common \
                       php8.2-mysql \
                       php8.2-zip \
                       php8.2-gd \
                       php8.2-mbstring \
                       php8.2-curl \
                       php8.2-xml \
                       php8.2-bcmath

COPY pma_installer.sh /
RUN bash /pma_installer.sh -q

COPY phpmyadmin_cred.sh /
RUN bash /phpmyadmin_cred.sh

# Install Korean
RUN apt-get install -y locales
RUN locale-gen ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8

# Remove apt cache
RUN rm -rf /var/lib/apt/lists/*

# Do Rest
ARG USER=coder
RUN useradd --groups sudo --no-create-home --shell /bin/bash ${USER} \
	&& echo "${USER} ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/${USER} \
	&& chmod 0440 /etc/sudoers.d/${USER}
USER ${USER}
WORKDIR /home/${USER}
RUN mkdir /home/${USER}/workspace
