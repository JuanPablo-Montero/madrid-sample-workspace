#!/usr/bin/env bash

nvm use v18.14.2 
gw clean
rm -rf build node_modules
gw deploy
yarn install
yarn start
