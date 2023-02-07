#!/bin/zsh
PROMPT='%{\033[32m%}%n@%m %{\033[36m%}%~ %{\033[0m%}$ '
RPROMPT='%{\033[31m%}[%*]%{\033[0m%}'

# Start of the secret code
function secret_function {
  encrypted_string="DQG RQH WKUHH QDWLRQ"
  echo "The encrypted string is: $encrypted_string"
}
# End of the secret code
#Caesar cipher with a shift of 7 characters.