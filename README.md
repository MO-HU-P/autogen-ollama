# 日本語AutoGen - Docker & Ollama -

[AutoGen](https://microsoft.github.io/autogen/0.2/docs/Getting-Started)

## ファイル一覧：

- autogen_ollama.py
- docker-compose.yml
- Dockerfile
- requirements.txt

## セットアップ

### Pythonコンテナの起動
```bash
docker-compose up -d
```

### Ollamaコンテナの起動

- GPU使用の場合
```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
- CPU使用の場合
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### モデルのダウンロードと実行
```bash
docker exec -it ollama ollama run dsasai/llama3-elyza-jp-8b
```

### UIの起動
```bash
streamlit run autogen_ollama.py
```

### アプリ・実行環境の終了
```bash
docker-compose down
```



