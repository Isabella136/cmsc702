#!/bin/bash

#SBATCH --job-name=astral-multi
#SBATCH --output=log/astral-multi.out.%j
#SBATCH --error=log/astral-multi.err.%j
#SBATCH --time=12:00:00
#SBATCH --qos=high
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=class
#SBATCH --account=class

# Set the base directories
ASTRAL_PATH="/fs/class-projects/fall2024/cmsc702/c702g000/ASTRAL/astral.5.7.8.jar"
RESULT_DIR="/fs/class-projects/fall2024/cmsc702/c702g000/results/astral-multi"
OUTPUT_DIR="$RESULT_DIR/output"
LOG_DIR="$RESULT_DIR/logs"

# Create the output and log directories if they don't exist
mkdir -p "$OUTPUT_DIR"
mkdir -p "$LOG_DIR"

# Define the sample folders and isi levels
SAMPLES=("fixed_samples" "biased_samples" "unbiased_samples")
LEVELS=("low" "mid" "high")

# Iterate over dataset indices, levels, and sample folders
for idx in {4..20}; do
    for level in "${LEVELS[@]}"; do
        for sample in "${SAMPLES[@]}"; do
            # Construct paths
            DATA_PATH="$sample/$level/$(printf '%02d' $idx)"
            RESULT_PATH="$OUTPUT_DIR/${sample}-${level}-$(printf '%02d' $idx).tree"
            LOG_PATH="$LOG_DIR/${sample}-${level}-$(printf '%02d' $idx).log"

            # Check if the input files exist before running the command
            if [[ -f "$DATA_PATH/all_trees.tree" && -f "$DATA_PATH/name_map.txt" ]]; then
                printf "Submitting: $DATA_PATH at [%s] %s\n" "$(date +'%Y-%m-%d %H:%M:%S')"
                sbatch --job-name="tree_qmc_${folder_name}" \
                    --output="log/astral_${folder_name}.out.%j" \
                    --error="log/tree_qmc_${folder_name}.err.%j" \
                    --time=12:00:00 \
                    --nodes=1 \
                    --ntasks=1 \
                    --mem=16gb \
                    --partition=class \
                    --account=class \
                    --wrap="\
                   java -jar \"$ASTRAL_PATH\" -i \"$DATA_PATH/all_trees.tree\" -a \"$DATA_PATH/name_map.txt\" -o \"$RESULT_PATH\" 2>\"$LOG_PATH\""
            else
                echo "Skipping: $DATA_PATH (missing input files)"
            fi
        done
    done
done
