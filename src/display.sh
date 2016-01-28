#!/bin/bash

export DISPLAY=:0

# Works in a non-display manager environment
# XUSER="$(ps -fp $(cat /tmp/.X0-lock ) | tail +2|awk '{print $1}')"
# This might work for environments running /etc/X11/xdm/Xsession
# and only one session (the one for :0 presumably)
XUSER=$(ps auxww | grep "/etc/X11/xdm/Xsession" | grep -v grep | awk '{print $1}')
# If you have some other measure.... Well, play with ps a bit and
# dream up something that works for you:-). ... or use another scheme
# ... For example you might be able to use the given -auth on the X
# command line directly.
echo $XUSER
if [ "x$XUSER" != "x" ]
then
        echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        xauth list
        echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        xauth -i -f /home/$XUSER/.Xauthority extract - $DISPLAY|xauth merge -
        xauth list
        # do your stuff here
        xset dpms force off
        echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        xauth remove $DISPLAY
        xauth list
        echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
else
        echo "X doesn't seem to run"
fi
