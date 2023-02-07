#!/bin/zsh
autoload -Uz colors && colors

# Define the black color
black="%{\033[30m%}"

# Define the yellow background color
yellow="%{\033[43m%}"

# Set the prompt to use the black font color and yellow background color
PROMPT="$black$black%n@%m %~ %# "
RPROMPT="$black$black[%*] " 

'''In this script, the colors function is loaded to enable color support in the terminal, and the black and yellow variables are defined using ANSI escape codes to set the text color to black and the background color to yellow, respectively. The PROMPT and RPROMPT variables are then set to use the black font color and yellow background color.

To use this script, save it to a file with a .zsh extension, make it executable with chmod +x filename.zsh, and then source the file in your ~/.zshrc file. The next time you start a new terminal session, the font color should be black and the background color should be yellow.'''