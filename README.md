# continue-dlt-demo
A demo on fine-tuning an LLM on coding data to improve autocomplete predictions for continue.dev within an organization. Using the tools: [dlt](https://github.com/dlt-hub/dlt), Hugging Face and Ollama

## Creating the dataset from continue.dev autocomplete suggestions
The continue.dev tool has an [autocomplete](https://continue.dev/docs/walkthroughs/tab-autocomplete) feature, and stores data in a `autocomplete.jsonl` file on whether the person using the tool has accepted or rejected the suggestions made. The `continue-hf-pipeline.py` file contains code for a custom dlt destination that takes this data, converts it to a parquet file and pushes it to a Hugging Face dataset repo, in a format ready for finetuning an LLM. 

## Finetuning process
I finetuned the `starcoder2:3b` model using the SFTTrainer from Hugging Face, based on the finetuning [code](https://github.com/bigcode-project/starcoder2/) that the creators of that model open-sourced.

I tried finetuning both on the dlt github repository, as well as the autocomplete dataset mentioned above. The code for the finetuning process can be found here: https://colab.research.google.com/drive/1jjb14BDlEeGjRmeXnfm41gDBlTNvsscn?usp=sharing
