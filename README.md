# 🤖 Desafio RPA — Bootbox Admin

Automação de tarefas no sistema **Bootbox Admin** utilizando **PyAutoGUI**, desenvolvida como desafio de RPA (Robotic Process Automation).

---

## 📋 O que o bot faz

1. **Login** no sistema via teclado
2. **Cria uma tarefa** com as seguintes informações:
   - Título gerado automaticamente com data/hora atual
   - Fluxo: Desenvolvimento
   - Projeto: Agily - Agily Tecnologia
   - Data de início: hoje às 20:00
   - Data de fim: amanhã às 20:30
   - Prioridade: Alta
   - Estimativa: 26h
   - Detalhes e comentário inicial preenchidos automaticamente
3. **Etapa Estimativa** — adiciona comentário e conclui
4. **Etapa Desenvolvimento** — adiciona comentário e conclui
5. **Etapa Code Review** — adiciona comentário e conclui
6. **Logout** e fecha o navegador

---

## 🗂️ Estrutura do projeto

```
DESAFIO_RPA/
├── assets/
│   └── bootbox_admin/     # Screenshots dos elementos da tela
├── .env                   # Credenciais e configurações (não versionado)
├── config.py              # Carrega variáveis de ambiente
├── date_utils.py          # Funções de data e hora
├── flow.py                # Lógica principal do bot
├── login_bootbox.py       # Ponto de entrada
├── screen_utils.py        # Utilitários de automação (clique, teclado, imagem)
├── capture_assets.py      # Script auxiliar para capturar novos assets
└── requirements.txt
```

---

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/FilipeNSV/desafio-botbox-rpa.git
cd desafio-botbox-rpa
```

### 2. Crie o ambiente virtual e instale as dependências

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Configure o `.env`

Crie um arquivo `.env` na raiz com:

```env
BASE_URL=https://admin.agily.com.br/login
USERNAME=seu@email.com
PASSWORD=suasenha

SLOW_MO=0.5
DEFAULT_TIMEOUT=30
IMAGE_CONFIDENCE=0.85
ASSETS_DIR=assets/bootbox_admin
```

---

## ▶️ Como executar

```bash
python login_bootbox.py
```

> ⚠️ Deixe o computador sem interação durante a execução. O PyAutoGUI controla mouse e teclado em tempo real.

---

## 📦 Dependências

| Biblioteca | Uso |
|---|---|
| `pyautogui` | Controle de mouse e teclado |
| `pyperclip` | Cópia de texto para clipboard |
| `opencv-python` | Matching de imagens na tela |
| `pillow` | Manipulação de imagens |
| `python-dotenv` | Leitura do arquivo `.env` |

---

## 🧠 Sobre a abordagem

O bot utiliza **reconhecimento de imagem** (`locateCenterOnScreen`) para encontrar elementos na tela e interagir com eles. Os assets ficam na pasta `assets/bootbox_admin/` e devem ser recapturados caso o layout do sistema mude.

Para recapturar os assets, utilize o script auxiliar:

```bash
python capture_assets.py
```

---

## 👨‍💻 Autor

Desenvolvido por **Filipe Vieira** como desafio de aprendizado em RPA com PyAutoGUI.
