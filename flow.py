import webbrowser

from config import BASE_URL, PASSWORD, USERNAME
from date_utils import (
    build_task_title,
    get_end_date,
    get_estimated_value,
    get_start_date,
)
from screen_utils import (
    click_and_type,
    click_and_type_then_enter,
    click_image,
    click_screen_center,
    press_down,
    press_enter,
    press_tab,
    sleep,
    clear_and_type,
    type_text,
    wait_image,
)

class BootboxBot:
    def __init__(self) -> None:
        self.task_title: str = build_task_title()

    def log(self, message: str) -> None:
        print(f"[BOOTBOX] {message}")

    # =========================
    # Browser
    # =========================
    def open(self) -> None:
        self.log("Abrindo página de login")
        webbrowser.open(BASE_URL)
        sleep(1)

    def close(self) -> None:
        import pyautogui
        self.log("Fechando navegador")
        pyautogui.hotkey("ctrl", "w")
        sleep(1)

    # =========================
    # Login
    # =========================
    def login(self) -> None:
        self.log("Preenchendo formulário de login")
        click_screen_center()
        press_tab(1)
        clear_and_type(USERNAME)
        press_tab(1)
        clear_and_type(PASSWORD)
        press_enter()
        
        self.log("Aguardando botão de tarefas após login")
        click_image("btnTask.png", timeout=30)

    # =========================
    # Navegação
    # =========================
    def go_to_tasks(self) -> None:
        self.log("Indo para aba de tarefas")
        click_image("btnTask.png", timeout=10)
        sleep(2)

    def open_add_task_modal(self) -> None:
        self.log("Abrindo modal de adicionar tarefa")
        click_image("addTask.png", timeout=20)
        sleep(2)

    # =========================
    # Preencher formulário — aba Básico
    # =========================
    def fill_title(self) -> None:
        self.log(f"Preenchendo título: {self.task_title}")
        click_and_type("inputTaskTitle.png", self.task_title, timeout=20)

    def fill_flow(self, flow_name: str = "Desenvolvimento") -> None:
        self.log(f"Selecionando fluxo: {flow_name}")
        click_image("inputTaskFlow.png", timeout=20)
        sleep(0.5)
        # Navega com setas — "Desenvolvimento" é a 3ª opção (2 downs)
        press_down(2)
        press_enter()

    def fill_project(self, project_name: str = "Agily - Agily Tecnologia") -> None:
        self.log(f"Selecionando projeto: {project_name}")
        click_image("inputTaskProject.png", timeout=20)
        sleep(0.5)
        # Tenta digitar para filtrar — se não funcionar, manda print do dropdown
        type_text(project_name)
        sleep(0.5)
        press_enter()

    def fill_start_date(self) -> None:
        start_date = get_start_date()
        self.log(f"Preenchendo data de início: {start_date}")
        click_image("inputTaskStart.png", timeout=20)
        sleep(0.5)
        clear_and_type(start_date)
        press_tab()  # fecha o calendário e vai pro dropdown de hora
        sleep(0.5)

    def fill_start_time(self) -> None:
        self.log("Selecionando horário de início: 20:00")
        # Dropdown nativo aceita digitação da primeira letra para pular
        # Digita "2" para ir direto para as opções que começam com 20:xx
        import pyautogui
        pyautogui.press("2")  # pula para 20:00
        sleep(0.2)
        pyautogui.press("0")
        press_enter()
        sleep(0.3)

    def fill_end_date(self) -> None:
        end_date = get_end_date()
        self.log(f"Preenchendo data de fim: {end_date}")
        click_image("inputTaskEnd.png", timeout=20)
        sleep(0.5)
        clear_and_type(end_date)
        press_tab()  # fecha calendário e vai pro dropdown de hora
        sleep(0.5)

    def fill_end_time(self) -> None:
        self.log("Selecionando horário de fim: 20:30")
        import pyautogui
        pyautogui.press("2")  # vai para 20:00
        sleep(0.2)
        pyautogui.press("down")  # avança para 20:30
        press_enter()
        sleep(0.3)

    def fill_priority_high(self) -> None:
        self.log("Selecionando prioridade Alta")
        click_image("btnTaskPriorityAlta.png", timeout=20)
        sleep(0.3)

    def fill_estimated(self) -> None:
        estimated = get_estimated_value()
        self.log(f"Preenchendo estimativa: {estimated}")
        click_and_type("inputTaskEstimated.png", estimated, timeout=20)

    # =========================
    # Preencher formulário — aba Detalhes
    # =========================
    def fill_details(self, details: str) -> None:
        self.log("Preenchendo aba Detalhes")
        click_image("btnTaskDetails.png", timeout=20)
        sleep(1)
        # Clica na área do editor rico (abaixo da toolbar)
        click_image("inputTaskDetails.png", timeout=20)
        sleep(0.5)
        type_text(details)

    # =========================
    # Preencher formulário — aba Comentários
    # =========================
    def fill_comment_in_modal(self, comment: str) -> None:
        self.log(f"Adicionando comentário no modal: {comment}")
        click_image("btnTaskComment.png", timeout=20)
        sleep(1)
        click_image("inputTaskComment.png", timeout=20)
        type_text(comment)
        click_image("btnTaskAddComment.png", timeout=20)
        sleep(2)

    # =========================
    # Salvar tarefa
    # =========================
    def save_task(self) -> None:
        self.log("Salvando tarefa")
        click_image("btnTaskSave.png", timeout=20)
        sleep(3)

    # =========================
    # Criar tarefa completa
    # =========================
    def create_task(self) -> None:
        self.open_add_task_modal()

        # Aba Básico
        self.fill_title()
        self.fill_flow(flow_name="Desenvolvimento")
        self.fill_project(project_name="Agily - Agily Tecnologia")
        self.fill_start_date()
        self.fill_start_time()
        self.fill_end_date()
        self.fill_end_time()
        self.fill_priority_high()
        self.fill_estimated()

        # Aba Detalhes
        self.fill_details(
            "Esta é uma tarefa de teste para aprendizador de RPA. Bom, lá vai… Hello World! :)"
        )

        # Aba Comentários
        self.fill_comment_in_modal("Estive aqui :)")

        # Salvar
        self.save_task()

    # =========================
    # Buscar tarefa
    # =========================
    def search_task(self) -> None:
        self.log(f"Buscando tarefa: {self.task_title}")
        click_and_type_then_enter("inputTaskSearch.png", self.task_title, timeout=20)
        sleep(2)

    def open_task_from_search(self) -> None:
        self.log("Abrindo tarefa a partir da busca")
        import pyautogui
        
        # "Título" é o cabeçalho fixo da coluna — asset simples de capturar
        x, y = wait_image("btnTaskTitleArea.png", timeout=20)
        
        # O link da tarefa fica ~45px abaixo do cabeçalho "Título"
        pyautogui.click(x, y + 45)
        sleep(2)

    # =========================
    # Comentários e conclusão dentro da tarefa aberta
    # =========================
    def add_comment_in_edit_task(self, comment: str) -> None:
        self.log(f"Adicionando comentário na tarefa: {comment}")
        click_image("btnTaskComment.png", timeout=20)
        sleep(1)
        click_image("inputEditTaskComment.png", timeout=20)
        type_text(comment)
        click_image("btnTaskAddComment.png", timeout=20)
        sleep(2)

    def conclude_task(self) -> None:
        self.log("Concluindo tarefa")
        click_image("btnTaskConclude.png", timeout=20)
        sleep(1)
        # Confirma o popup "Tem certeza que quer concluir a tarefa?"
        click_image("btnTaskConfirmConclude.png", timeout=10)
        sleep(2)

    def open_code_review_section(self) -> None:
        self.log("Abrindo seção Code Review")
        # Clica no header "Tarefas de Code Review" para expandir
        click_image("btnCodeReview.png", timeout=20)
        sleep(2)

    def open_task_from_code_review(self) -> None:
        self.log("Abrindo tarefa na seção Code Review")
        import pyautogui
        # Usa o cabeçalho "Título" como âncora — mesmo asset
        x, y = wait_image("btnTaskTitleArea.png", timeout=20)
        pyautogui.click(x, y + 45)
        sleep(2)        

    # =========================
    # Logout
    # =========================
    def logout(self) -> None:
        self.log("Fazendo logout")
        click_image("btnUser.png", timeout=20)
        sleep(1)
        click_image("btnUserLogout.png", timeout=20)
        sleep(2)

    # =========================
    # Fluxo completo
    # =========================
    def run_flow(self) -> None:
        # 1. Vai para tarefas e cria a tarefa
        self.go_to_tasks()
        self.create_task()

        # 2. Busca a tarefa — etapa Estimativa
        self.log("=== ETAPA: Estimativa ===")
        self.search_task()
        self.open_task_from_search()
        self.add_comment_in_edit_task("Etapa de estimativa OK")
        self.conclude_task()

        # 3. Busca novamente — etapa Desenvolvimento
        self.log("=== ETAPA: Desenvolvimento ===")
        self.open_task_from_search()
        self.add_comment_in_edit_task("Etapa de Desenvolvimento OK")
        self.conclude_task()

        # 4. Code Review
        self.log("=== ETAPA: Code Review ===")
        self.open_code_review_section()
        self.open_task_from_code_review()
        self.add_comment_in_edit_task("Finalizando desenvolvimento")
        self.conclude_task()

        # 5. Logout e fecha navegador
        self.logout()
        self.close()