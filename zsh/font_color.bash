#!/bin/zsh
autoload -Uz colors && colors

# Define the black color
black="%{\033[30m%}"

# Set the prompt to use the black color
PROMPT="$black%n@%m %~ %# "
RPROMPT="$black[%*] "