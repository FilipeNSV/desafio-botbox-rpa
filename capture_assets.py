# capture_assets.py
import pyautogui
import time
from PIL import Image

assets = [
    # 1. Login
    "inputEmail",
    "inputPassword",
    "btnLogin",
    "btnTask",          # aguarda após login

    # 2. Criar tarefa
    "addTask",
    "inputTaskTitle",
    "inputTaskFlow",
    "inputTaskProject",
    "inputTaskEstimated",
    "inputTaskStart",
    "inputTaskEnd",
    "inputTaskPriority",
    "btnTaskDetails",   # abre a aba de detalhes
    "inputTaskDetails",
    "btnTaskSave",

    # 3. Buscar tarefa
    "inputTaskSearch",

    # 4. Abrir e interagir com a tarefa
    "btnTaskCodeReview",  # card da tarefa no resultado da busca
    "btnTaskComment",     # abre seção de comentários
    "inputTaskComment",
    "btnTaskAddComment",
    "btnTaskConclude",

    # 5. Code Review (fluxo opcional)
    "btnCodeReview",      # aba de code review

    # 6. Logout
    "btnUser",
    "btnUserLogout",
]

OUTPUT_DIR = "assets/bootbox_admin"

def capture(name: str):
    print(f"\n>>> Próximo: {name}.png")
    print("1. Navegue até onde o elemento aparece na tela")
    print("2. Pressione ENTER aqui para tirar o screenshot")
    input("   [ENTER para capturar]")
    
    screen = pyautogui.screenshot()
    screen.save(f"temp_{name}.png")
    print(f"✓ Screenshot salvo como temp_{name}.png")
    print(f"  Abra no Paint, recorte APENAS o elemento e salve em:")
    print(f"  {OUTPUT_DIR}/{name}.png")
    input("  [ENTER quando terminar o recorte e salvar]")
    print(f"✓ {name}.png concluído!")

print("=== CAPTURADOR DE ASSETS ===")
print(f"Serão capturados {len(assets)} assets.")
print("Para cada um: navegue até o elemento, pressione ENTER, recorte no Paint e salve.")
input("\n[ENTER para começar]")

for asset in assets:
    capture(asset)

print("\n✅ Todos os assets capturados!")