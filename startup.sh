#!/usr/bin/bash

echo "
============ Anie ============
Copyright (c) 2022 xNKIT | @xNKIT

- Running Pyrogram!
- Installing Anie
- Done!
- Running Anie
- Starting Anie on your Telegram!
================================
"

start_anie () {
    if [[ -z "$ANIE_SESSION" ]]
    then
	    echo "Please Add Pyrogram String Session"
    else
	    python3 -m anie
    fi
  }

_install_anie () {
    start_anie
  }

_install_anie
