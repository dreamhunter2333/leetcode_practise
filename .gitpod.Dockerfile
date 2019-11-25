FROM gitpod/workspace-full:latest

USER root

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install zsh screenfetch -y
ENV SHELL=/bin/zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \
    cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
RUN echo 'zsh'  >>  ~/.bashrc && echo 'eval "$(pyenv init -)"' >> ~/.zshrc
RUN apt-get update -y && apt-get upgrade -y

USER root
