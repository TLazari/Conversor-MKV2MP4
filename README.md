
# Conversor de Arquivos MKV para MP4

Este script Python converte arquivos de vídeo no formato **MKV** para **MP4**. Ele percorre todos os arquivos MKV em uma pasta de entrada especificada e os salva em uma pasta de saída após a conversão.

## 🚀 Funcionalidades
- Converte vídeos do formato **MKV** para **MP4**.
- Percorre automaticamente todos os arquivos dentro de uma pasta.
- Salva os arquivos convertidos em uma pasta separada.
- Usa o codec **libx264** para vídeo e **aac** para áudio.

## 🛠️ Requisitos
Antes de executar o script, certifique-se de ter o seguinte configurado:

### Dependências
- Python 3.7 ou superior.
- Biblioteca `moviepy`.

### Instalação de Dependências
Instale as dependências necessárias com o comando:

```bash
pip install moviepy
```

Certifique-se de que o **FFmpeg** está instalado e configurado no PATH do sistema, pois ele é usado internamente pelo `moviepy`.

### Instalação do FFmpeg
- No Windows, baixe e configure o FFmpeg no PATH: [Guia de instalação do FFmpeg](https://ffmpeg.org/download.html).
- No Linux ou macOS, use um gerenciador de pacotes:
  ```bash
  sudo apt install ffmpeg  # Para Debian/Ubuntu
  brew install ffmpeg      # Para macOS
  ```

## 🖥️ Como Usar

1. **Clone ou baixe o repositório:**
   ```bash
   git clone https://github.com/TLazari/Conversor-MKV2MP4
   cd Conversor-MKV2MP4
   ```

2. **Edite as pastas de entrada e saída no script:**
   No arquivo `converter.py`, atualize os caminhos das pastas:
   ```python
   input_folder = "caminho/para/pasta/mkv"  # Pasta com arquivos MKV
   output_folder = "caminho/para/pasta/mp4"  # Pasta para salvar arquivos MP4
   ```

3. **Execute o script:**
   ```bash
   python converter.py
   ```

4. **Confira a pasta de saída:**
   Após a execução, os arquivos convertidos estarão na pasta de saída configurada.

## 📂 Estrutura do Projeto
```
📁 Conversor-MKV2MP4
├── converter.py   # Script principal
├── README.md      # Documentação
```

## ⚠️ Observações
- Dependendo do tamanho e número de vídeos, o tempo de execução pode variar.
- Certifique-se de que há espaço suficiente no disco para armazenar os arquivos convertidos.

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo como desejar.
