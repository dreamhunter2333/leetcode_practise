FROM gitpod/workspace-full:latest

USER root

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
RUN sed -i.bkp -e 's/%sudo ALL=NOPASSWD:ALL/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/g' /etc/sudoers
RUN echo "root:0000" | chpasswd
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install zsh screenfetch -y
ENV SHELL=/bin/zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \
    cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
RUN echo 'zsh'  >>  ~/.bashrc && echo 'eval "$(pyenv init -)"' >> ~/.zshrc
RUN apt-get update -y && apt-get upgrade -y
USER root
#
# More information: https://www.gitpod.io/docs/42_config_docker/
