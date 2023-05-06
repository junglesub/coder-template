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

# Install Python

RUN apt-get update && \
    apt-get install -y software-properties-common python3-pip

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
