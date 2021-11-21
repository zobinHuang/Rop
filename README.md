# ROP (Routing OPtimizer)
**ROP** (i.e. short for Routing Optimizer) is a multi-path network routing offline solver based on [CVXPY](https://www.cvxpy.org/). This work is supported under the guidance of Professor X.Wang from University of Electronic Science and Technology of China.

## Enviroment Configuration

1. enter the root diectory and create virtual environment via conda
```bash
# create virtual enviroment
conda create -v ./env python=3.8

# activate enviroment
conda activate ./env
```

2. install dependencies

```bash
conda install -c conda-forge cvxpy pyyaml
```

## Usage

TODO

## Repo Structure
* tools 里面放生成 topo 和 demand 的工具代码