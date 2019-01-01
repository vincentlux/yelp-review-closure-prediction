#!/bin/bash

#SBATCH -p general
#SBATCH -N 1
#SBATCH -n 16
#SBATCH -t 72:00:00

python bigram_generation_longleaf.py
