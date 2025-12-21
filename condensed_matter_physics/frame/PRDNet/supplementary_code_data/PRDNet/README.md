

### Installation



#### 1. Environment Setup
```bash
conda create -n prdnet python=3.9 -y
conda activate prdnet
```

#### 2. Core Dependencies
```bash
# PyTorch and PyTorch Geometric
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install torch-geometric pyg-lib torch-scatter torch-sparse torch-cluster torch-spline-conv

# Scientific computing
pip install numpy scipy pandas scikit-learn matplotlib
pip install ase jarvis-tools h5py tqdm

# Machine learning
pip install wandb ignite pydantic pydantic-settings
```

#### 3. Optional Dependencies
```bash
# Visualization
pip install seaborn plotly

# Distributed training
pip install accelerate

# Development tools
pip install pytest black flake8 mypy pre-commit
```

### 4. Verify Installation

```bash
# Quick verification
python -c "
import torch
import prdnet
from prdnet.model import Prdnet, PrdnetConfig
print('✅ PRDNET installed successfully!')
print(f'PyTorch: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'CUDA devices: {torch.cuda.device_count()}')
"
```



## Training

### Command Line Training

```bash
# Basic training
python trainer.py

# Custom parameters
python trainer.py \
    --epochs 200 \
    --batch_size 64 \
    --learning_rate 1e-4


```

### Distributed Training

```bash
# Multi-GPU training with torchrun
torchrun --nproc_per_node=4 trainer.py \
    --epochs 500 \
    --batch_size 96 \
    --learning_rate 1e-4

# With custom data paths
torchrun --nproc_per_node=4 trainer.py \
    --train_db_path data/train.db \
    --val_db_path data/val.db \
    --test_db_path data/test.db
```

### Configuration Options

```bash
# Disable WandB logging
python trainer.py --no_wandb

# Custom cache directory
python trainer.py --cache_dir ./custom_cache

# Force cache rebuild
python trainer.py --force_cache_rebuild

# Custom model configuration
python trainer.py \
    --conv_layers 8 \
    --node_features 512 \
    --use_diffraction True \
    --diffraction_max_hkl 6
```

## Monitoring Training

### WandB Integration

1. **Setup WandB account** (optional but recommended):
```bash
# Install and login to WandB
pip install wandb
wandb login
```

2. **Training with WandB logging**:
```bash
python prd_trainer.py --epochs 100
# Training metrics will be automatically logged to WandB
```









