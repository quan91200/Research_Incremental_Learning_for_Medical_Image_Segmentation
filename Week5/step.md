```
conda activate hermes
```

```
CUDA_VISIBLE_DEVICES="" python train.py \
  --dataset kits \
  --model hermes_resunet \
  --dimension 3d \
  --batch_size 2 \
  --unique_name phase1_kits \
  --log_path runs/phase1 \
  --cp_path checkpoints/phase1 \
  --gpu cpu
```