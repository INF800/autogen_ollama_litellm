1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Install models you want to run:

```bash
ollama run llama2
ollama run codellama
```

(You may close the terminal.)

3. Spawn the servers and note down port numbers.

```bash
litellm --model ollama/llama2
litellm --model ollama/codellama
```

4. Run the agents

```bash
AUTOGEN_USE_DOCKER=0 python main.py
```
