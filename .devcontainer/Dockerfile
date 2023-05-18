FROM ubuntu:18.04
LABEL maintainer="joao.fracarolli@encora.com"

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user (https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user)
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install packages
RUN apt update && apt install -y \
    bash \
    bash-completion \
    cowsay \
    curl \
    git \
    iputils-ping \
    libncurses5 \
    libpq-dev \
    libstdc++5 \
    python2.7 \
    python-pip \
    python-pyqt5 \
    python-psycopg2 \
    pyqt5-dev \
    software-properties-common \
    vim-common \
    wget
    
WORKDIR /workspaces/xlightdata

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

