#!/bin/bash

#SBATCH --job-name=untar
#SBATCH --output=log/untar.out.%j
#SBATCH --error=log/untar.err.%j
#SBATCH --time=12:00:00
#SBATCH --qos=high
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=cbcb
#SBATCH --account=cbcb

cd biased_samples/high
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../mid
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../low
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../../fix_samples/high
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../mid
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../low
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../../unbiased_samples/high
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../mid
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;

cd ../low
for i in {1..9};
do 
    tar xvzf 0${i}.tar.gz 

done;
for i in {10..50};
do 
    tar xvzf ${i}.tar.gz 

done;