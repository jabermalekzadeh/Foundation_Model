from transformers import AutoTokenizer, AutoModelForCausalLM

model = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained(model, torch_dtype = torch.float16)