


import yaml
import time
import os
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer



pwf_path = Path(__file__)




# Get config file
config_file = open( pwf_path.parent.parent / 'config/config.yaml', "r")
config = yaml.load(config_file, Loader=yaml.FullLoader)
config_file.close()

tokenizer = AutoTokenizer.from_pretrained(config['pretrained_model_name'])
model = AutoModelForCausalLM.from_pretrained(config['pretrained_model_name'])
