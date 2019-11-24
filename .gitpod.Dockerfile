FROM gitpod/workspace-full:latest

USER root

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
RUN apt-get update && apt-get upgrade
RUN apt-get install zsh screenfetch -y
ENV SHELL=/bin/zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \
    cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

USER root
#
# More information: https://www.gitpod.io/docs/42_config_docker/
