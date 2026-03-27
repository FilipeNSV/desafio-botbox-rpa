from datetime import datetime, timedelta


def build_task_title() -> str:
    now = datetime.now()
    return f"Desenvolvimento de RPA (teste) - {now.strftime('%d/%m/%Y %H:%M:%S')}"


def get_start_date() -> str:
    """Retorna a data de hoje no formato dd/mm/yyyy."""
    return datetime.now().strftime("%d/%m/%Y")


def get_start_time() -> str:
    """Retorna 20:00 como horário de início."""
    return "20:00"


def get_end_date() -> str:
    """Retorna amanhã no formato dd/mm/yyyy."""
    return (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")


def get_end_time() -> str:
    """Retorna 22:00 como horário de fim."""
    return "22:00"


def get_estimated_value() -> str:
    return "26"