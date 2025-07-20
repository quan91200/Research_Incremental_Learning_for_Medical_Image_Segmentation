#!/bin/bash

echo "===> Phase 1: Kidney only"
python train.py \
  --dataset kits23_IL/phase1/hermes_3D.yaml \
  --model hermes \
  --dimension 3D \
  --amp \
  --batch_size 2 \
  --gpu 0 \
  --log_path logs/phase1/ \
  --unique_name phase1_run

echo "===> Phase 2: Kidney + Tumor"
python train.py \
  --dataset kits23_IL/phase2/hermes_3D.yaml \
  --model hermes \
  --dimension 3D \
  --amp \
  --batch_size 2 \
  --gpu 0 \
  --log_path logs/phase2/ \
  --unique_name phase2_run

echo "===> Phase 3: Kidney + Tumor + Cyst"
python train.py \
  --dataset kits23_IL/phase3/hermes_3D.yaml \
  --model hermes \
  --dimension 3D \
  --amp \
  --batch_size 2 \
  --gpu 0 \
  --log_path logs/phase3/ \
  --unique_name phase3_run

echo "✅ Incremental training pipeline completed."
