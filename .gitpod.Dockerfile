FROM gitpod/workspace-full

USER gitpod

RUN brew tap heroku/brew && brew install \
    heroku \
    k6
