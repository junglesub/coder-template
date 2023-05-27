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
COPY Caddyfile /etc/caddy/

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
