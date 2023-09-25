import yaml
from pathlib import Path
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer



# Get config file
pwf_path = Path(__file__)

config_file = open( pwf_path.parent.parent / 'config/config.yaml', 'r')
config = yaml.load(config_file, Loader=yaml.FullLoader)
config_file.close()

# Instantiate model & tokenizer
tokenizer = AutoTokenizer.from_pretrained(config['model']['pretrained_model_name'])
llm = AutoModelForSeq2SeqLM.from_pretrained(config['model']['pretrained_model_name'])

# Prompt test
test_prompt = "What is the wealthiest country in the world?"

inputs = tokenizer(test_prompt , return_tensors='pt')
outputs_encoded = llm.generate(
    max_length = config['model']['max_output_length'],
    temperature = config['model']['temperature'],
    do_sample=config['model']['do_sample'],
    **inputs
    )

outputs = tokenizer.batch_decode(outputs_encoded, skip_special_tokens=True)

for output in outputs:
    print(f'{output}')

