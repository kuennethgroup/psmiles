# Install `psmiles` with pip

``` sh
pip install git+https://github.com/kuennethgroup/psmiles.git
```

If you need polyBERT and mordred fingerprints use:

``` sh
pip install 'psmiles[polyBERT,mordred]@git+https://github.com/kuennethgroup/psmiles.git'
```

## Install `psmiles` with poetry

``` sh
poetry add git+https://github.com/kuennethgroup/psmiles.git
```

With polyBERT and mordred fingerprints

``` sh
poetry add git+https://github.com/kuennethgroup/psmiles.git -E polyBERT -E mordred
```
