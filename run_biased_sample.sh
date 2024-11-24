#!/bin/bash

#SBATCH --job-name=simphy_tree_gen
#SBATCH --output=log/simphy_tree_gen.out.%j
#SBATCH --error=log/simphy_tree_gen.err.%j
#SBATCH --time=12:00:00
#SBATCH --qos=high
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=cbcb
#SBATCH --account=cbcb

mkdir biased_samples/
cd biased_samples/

#Gloabal parameters
#   -rs 50                      50 replicates
#   -rl u:1000,1000  -rg 1      1000 genes
#   -sb u:0.000001,0.000001     10^-6 births per time
#   -sl u:200,200               200 species
#   -si u:10,30                 uniform distr of 10 to 30 individuals per species
#   -sp u:200000,200000         population size of 200K
#   -su e:10000000              substitution rate
#   -hs ln:1.5,1                Species branch rate
#   -hl ln:1.2,1                Locus rate
#   -hg ln:1.4,1                Gene-tree-branch rate
#   -so u:1,1                   ingroup height : branch from the root to the ingroup ratio
#   -cs 293745                  Random number generator seed
#   -v 3                        global settings summary, sampled settings per species, 
#                               locus and gene trees, simulation progress per gene tree, 
#                               warnings and errors
#   -ot 0                       Species and locus tree branches written in generations
#   -op 1                       Logging of sampled options
#   -od 1                       SQLite database output


#500K generations
#   -st u:500000,500000         500K generations
#   -o low                      Common output prefix-name (for folders and files).                

simphy_lnx64 -rs 50 -rl u:1000,1000 -rg 1 -st u:500000,500000 \
 -sb u:0.000001,0.000001 -sl u:200,200 -si u:10,30 -sp u:200000,200000 \
 -su e:10000000 -hs ln:1.5,1 -hl ln:1.2,1 -hg ln:1.4,1 -so u:1,1 \
 -v 3 -cs 293745 -ot 0 -op 1 -od 1 -o low

#1M generations
#   -st u:1000000,1000000       1M generations
#   -o mid                      Common output prefix-name (for folders and files).                

simphy_lnx64 -rs 50 -rl u:1000,1000 -rg 1 -st u:1000000,1000000 \
 -sb u:0.000001,0.000001 -sl u:200,200 -si u:10,30 -sp u:200000,200000 \
 -su e:10000000 -hs ln:1.5,1 -hl ln:1.2,1 -hg ln:1.4,1 -so u:1,1 \
 -v 3 -cs 293745 -ot 0 -op 1 -od 1 -o mid

#2M generations
#   -st u:2000000,2000000       2M generations
#   -o high                     Common output prefix-name (for folders and files).                

simphy_lnx64 -rs 50 -rl u:1000,1000 -rg 1 -st u:2000000,2000000 \
 -sb u:0.000001,0.000001 -sl u:200,200 -si u:10,30 -sp u:200000,200000 \
 -su e:10000000 -hs ln:1.5,1 -hl ln:1.2,1 -hg ln:1.4,1 -so u:1,1 \
 -v 3 -cs 293745 -ot 0 -op 1 -od 1 -o high