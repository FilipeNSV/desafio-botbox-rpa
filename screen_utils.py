import time
from pathlib import Path
from typing import Optional, Tuple

import pyautogui
import pyperclip
from PIL import Image

from config import ASSETS_DIR, DEFAULT_TIMEOUT, IMAGE_CONFIDENCE, SLOW_MO

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

MIN_IMAGE_CONFIDENCE = 0.5


def sleep(seconds: Optional[float] = None) -> None:
    time.sleep(SLOW_MO if seconds is None else seconds)


def asset_path(filename: str) -> Path:
    return Path(ASSETS_DIR) / filename


def load_image(image_name: str) -> Image.Image:
    image_path = asset_path(image_name)

    if not image_path.exists():
        raise FileNotFoundError(f"Asset not found: {image_path}")

    return Image.open(image_path)


def locate_center(
    image_name: str,
    timeout: Optional[int] = None,
    confidence: Optional[float] = None,
    grayscale: bool = True,
) -> Optional[Tuple[int, int]]:
    timeout = timeout or DEFAULT_TIMEOUT
    confidence = confidence or IMAGE_CONFIDENCE

    needle_image = load_image(image_name)
    end_time = time.time() + timeout
    last_error: Exception | None = None
    confidence_levels = []
    current_confidence = confidence

    while current_confidence >= MIN_IMAGE_CONFIDENCE:
        confidence_levels.append(round(current_confidence, 2))
        current_confidence = round(current_confidence - 0.1, 2)

    while time.time() < end_time:
        for level in confidence_levels:
            try:
                location = pyautogui.locateCenterOnScreen(
                    needle_image,
                    confidence=level,
                    grayscale=grayscale,
                )
            except pyautogui.ImageNotFoundException as exc:
                last_error = exc
                location = None

            if location:
                return location

        time.sleep(0.4)

    if last_error is not None:
        raise TimeoutError(
            f"Image not found on screen within {timeout}s: {image_name}. "
            f"Last match error: {last_error}"
        ) from last_error

    return None


def wait_image(
    image_name: str,
    timeout: Optional[int] = None,
    confidence: Optional[float] = None,
) -> Tuple[int, int]:
    try:
        location = locate_center(
            image_name=image_name,
            timeout=timeout,
            confidence=confidence,
        )
    except TimeoutError:
        raise

    if not location:
        raise TimeoutError(f"Image not found on screen: {image_name}")

    return location


def image_exists(
    image_name: str,
    timeout: int = 2,
    confidence: Optional[float] = None,
) -> bool:
    try:
        return locate_center(
            image_name=image_name,
            timeout=timeout,
            confidence=confidence,
        ) is not None
    except TimeoutError:
        return False


def click_image(
    image_name: str,
    timeout: Optional[int] = None,
    confidence: Optional[float] = None,
    clicks: int = 1,
) -> Tuple[int, int]:
    x, y = wait_image(
        image_name=image_name,
        timeout=timeout,
        confidence=confidence,
    )

    pyautogui.click(x, y, clicks=clicks)
    sleep()
    return x, y


def double_click_image(
    image_name: str,
    timeout: Optional[int] = None,
    confidence: Optional[float] = None,
) -> Tuple[int, int]:
    x, y = wait_image(
        image_name=image_name,
        timeout=timeout,
        confidence=confidence,
    )

    pyautogui.doubleClick(x, y)
    sleep()
    return x, y


def safe_click_image(
    image_name: str,
    timeout: int = 2,
    confidence: Optional[float] = None,
) -> bool:
    if image_exists(image_name=image_name, timeout=timeout, confidence=confidence):
        click_image(image_name=image_name, timeout=timeout, confidence=confidence)
        return True

    return False


def press_enter() -> None:
    pyautogui.press("enter")
    sleep()


def press_tab(times: int = 1) -> None:
    for _ in range(times):
        pyautogui.press("tab")
        sleep(0.2)


def press_esc() -> None:
    pyautogui.press("esc")
    sleep()


def press_down(times: int = 1) -> None:
    for _ in range(times):
        pyautogui.press("down")
        sleep(0.2)


def press_up(times: int = 1) -> None:
    for _ in range(times):
        pyautogui.press("up")
        sleep(0.2)


def press_hotkey(*keys: str) -> None:
    pyautogui.hotkey(*keys)
    sleep()


def click_screen_center() -> None:
    width, height = pyautogui.size()
    pyautogui.click(width // 2, height // 2)
    sleep()


def clear_and_type(text: str) -> None:
    pyautogui.hotkey("ctrl", "a")
    sleep(0.2)
    pyautogui.press("backspace")
    sleep(0.2)

    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    sleep()


def type_text(text: str) -> None:
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    sleep()


def click_and_type(
    image_name: str,
    text: str,
    timeout: int = DEFAULT_TIMEOUT,
) -> None:
    click_image(image_name, timeout=timeout)
    clear_and_type(text)


def click_and_type_then_enter(
    image_name: str,
    text: str,
    timeout: int = DEFAULT_TIMEOUT,
) -> None:
    click_and_type(image_name=image_name, text=text, timeout=timeout)
    press_enter()


def scroll_down(amount: int = -500) -> None:
    pyautogui.scroll(amount)
    sleep()


def select_option_by_text(image_name: str, option_text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
    """Clica num dropdown (imagem) e seleciona a opção pelo texto usando setas do teclado."""
    click_image(image_name, timeout=timeout)
    sleep(0.5)
    # Digita o texto para filtrar (funciona em dropdowns com busca)
    type_text(option_text)
    sleep(0.5)
    press_enter()


def click_day_in_calendar(day: int) -> None:
    """Clica no dia correto dentro de um calendário aberto na tela."""
    import pyautogui
    # Localiza o calendário procurando o número do dia via OCR não disponível,
    # então usamos coordenadas relativas após o calendário abrir.
    # Como o calendário já está visível, usamos screenshot e buscamos o número.
    sleep(0.5)
    # Pressiona o dia como texto no campo de data (fallback via teclado)
    type_text(str(day))
    press_enter()


def select_time_in_dropdown(image_name: str, time_value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
    """
    Clica no dropdown de hora e seleciona o horário desejado navegando com setas.
    time_value ex: '20:00'
    """
    click_image(image_name, timeout=timeout)
    sleep(0.5)
    # O dropdown de hora abre com lista — usa setas para navegar
    # Começa do topo e desce até achar o horário
    # Lista começa em 07:00, cada opção = 30 min
    # Calcula quantas posições descer
    start_hour = 7
    start_min = 0
    h, m = map(int, time_value.split(":"))
    total_start = start_hour * 60 + start_min
    total_target = h * 60 + m
    steps = (total_target - total_start) // 30

    # Vai para o topo da lista
    pyautogui.hotkey("ctrl", "Home")
    sleep(0.3)

    for _ in range(steps):
        press_down(1)

    press_enter()