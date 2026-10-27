#!/bin/bash
# Lance la suite de tests Playwright dans cet environnement (polices à déclarer à la main)
M=/home/hermeswebui/.local/mamba-env
export LD_LIBRARY_PATH=$M/lib:/workspace/libs/usr/lib/x86_64-linux-gnu:/workspace/libs/lib/x86_64-linux-gnu
export FONTCONFIG_PATH=$M/etc/fonts
cd /workspace/nah
python3 "$@"
