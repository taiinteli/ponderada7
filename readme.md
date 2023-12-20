# Tradução, Speech-to-Text e Text-to-Speech

# Link do vídeo de demonstração do projeto: https://drive.google.com/file/d/19QDYVbVaXnJ-jhSVH0YmSW1N490wmfxT/view?usp=sharing

A ferramenta de terminal desenvolvida é capaz de processar um arquivo de áudio fornecido pelo usuário, transformá-lo em texto, traduzir esse texto para outro idioma (por padrão, de português para inglês), e em seguida, sintetizar o texto traduzido em áudio.

## 3. Instalação e Uso

### Requisitos
- Python 3.10 ou superior
- Bibliotecas necessárias: `whisper`, `txtai`, `soundfile`, `simpleaudio`, `googletrans==4.0.0-rc1`

### Instalação
Para instalar as dependências necessárias, execute:
```
pip install whisper txtai[pipeline] soundfile simpleaudio googletrans==4.0.0-rc1
```

### Execução
Para executar a aplicação:
```
python3 modelo.py <caminho_para_o_arquivo_de_audio>
```
Substitua `<caminho_para_o_arquivo_de_audio>` pelo caminho do seu arquivo de áudio. No caso, "audio_fra.mp3"


