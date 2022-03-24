#!/bin/bash
set -e

cd /usr/local
git clone https://github.com/MicrosoftDocs/edge-modules.git

cd edge-modules
git checkout main /usr/local/edge-modules/actions/action-asz-validation/entrypoint.sh

python /usr/local/edge-modules/scripts/val_ki_dockeraction.py

state=`cat state.txt`

echo $state

if [ $state == "True" ] ; then
  echo "All is well."
fi

if [ $state == "False" ]; then
  echo "Game over!"
  exit 1
fi