#!/bin/sh

#version 1.0

ROOT=$PWD

VENV=$ROOT/venv
VPIP=$VENV/bin/pip3

case "$1" in

    venv-install)

        echo 'venv-install'

        rm -rf $VENV
        virtualenv $VENV
        $VPIP install -r requirements.txt
        ;;

    venv-update)

        echo 'venv-update'

        $VPIP install -r requirements.txt
        ;;

    venv-freeze)

        echo 'venv-freeze'

        rm requirements.txt
        $VPIP freeze >> requirements.txt
        ;;

    venv-uninstall)

        echo 'venv-uninstall'

        rm -rf $VENV
        ;;

    *)
        echo 'enter option'
        ;;

esac
