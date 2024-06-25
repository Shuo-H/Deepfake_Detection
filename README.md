# Deepfake_Detection
Feature extractor for Pengi(base), CLAP(2023), wav2vec, wavlm

## Create Environment
```python
conda create -n "feat_extract" python=3.8
cd models/mspengi
pip install -r requirements.txt
```
## Download Pengi checkpoint
- Download Pengi checkpoint from [here](https://zenodo.org/records/8387083)
- Move the downloaded checkpoint to `AudioEntailment/mspengi/configs/`
