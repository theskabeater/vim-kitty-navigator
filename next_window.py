def main():
    pass


def handle_result(args, result, target_window_id, boss):
    try:
        delta = int(args[1])
    except Exception as e:
        delta = 1

    if delta > 0:
        boss.active_tab.next_window()
    else:
        boss.active_tab.previous_window()


handle_result.no_ui = True
