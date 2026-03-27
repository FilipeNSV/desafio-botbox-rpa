from flow import BootboxBot

if __name__ == "__main__":
    bot = BootboxBot()

    try:
        bot.open()
        bot.login()
        bot.run_flow()
    except Exception as e:
        print(f"[ERRO] {e}")
        raise