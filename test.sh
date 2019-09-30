#!/bin/bash

/home/joaoepj/.opam/4.06.0/bin/frenetic http-controller --verbosity debug 2>controller.log & 
sleep 1
python /mnt/docs/doutorado/ocamlsandbox/joao.py | tee application.log 2>application.log &
sleep 1
python net.py

