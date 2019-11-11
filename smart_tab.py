from kitty.conf.utils import parse_kittens_shortcut
from kitty.config import parse_key_action
from kitty import keys

def main(args):
    pass


def _actions(extended):
    yield keys.defines.GLFW_PRESS
    if extended:
        yield keys.defines.GLFW_RELEASE


def handle_result(args, answer, target_window_id, boss):
    _kitten = args[0]
    action_if_tabs = ' '.join(args[1:-1])
    if_no_tabs = args[-1]

    tm = boss.active_tab_manager
    if tm is None:
        return

    if len(tm.tabs) > 1:
        boss.dispatch_action(parse_key_action(action_if_tabs))
        return

    w = boss.window_id_map.get(target_window_id)
    mods, key, is_text = parse_kittens_shortcut(if_no_tabs)
    if is_text:
        w.send_text(key)
        return

    extended = w.screen.extended_keyboard
    for action in _actions(extended):
        sequence = (
            ('\x1b_{}\x1b\\' if extended else '{}')
            .format(
                keys.key_to_bytes(
                    getattr(keys.defines, 'GLFW_KEY_{}'.format(key)),
                    w.screen.cursor_key_mode, extended, mods, action)
                .decode('ascii')))
        w.write_to_child(sequence)


handle_result.no_ui = True
