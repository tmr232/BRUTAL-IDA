'''
BRUTAL IDA

Block Redo & Undo To Achieve Legacy IDA
'''
import os

import idaapi


def get_brutal_icon_path(brutal_icon_name):
    return idaapi.load_custom_icon(os.path.join(os.path.dirname(__file__), 'BRUTAL-ICONS', brutal_icon_name))


BRUTAL5_ICON = get_brutal_icon_path('BRUTAL_IDA5.png')
BRUTAL6_ICON = get_brutal_icon_path('BRUTAL_IDA6.png')
BRUTAL_LETTERS = {
    brutal_letter: get_brutal_icon_path('BRUTAL_{}.png'.format(brutal_letter)) for brutal_letter in 'BRUTAL'
}


class BrutalLetterHandler(idaapi.action_handler_t):
    def __init__(brutal_self):
        idaapi.action_handler_t.__init__(brutal_self)

    def activate(brutal_self, brutal_context):
        pass

    def update(brutal_self, brutal_context):
        return idaapi.AST_DISABLE_ALWAYS


class BrutalActionHandler(idaapi.action_handler_t):
    def __init__(brutal_self):
        idaapi.action_handler_t.__init__(brutal_self)
        brutal_self.brutal_mode = '6.x'

    def activate(brutal_self, brutal_context):
        brutal_self.brutal_mode = {
            '5.x': '6.x',
            '6.x': '5.x',
        }[brutal_self.brutal_mode]

    @property
    def icon(brutal_self):
        return {
            '5.x': BRUTAL5_ICON,
            '6.x': BRUTAL6_ICON,
        }[brutal_self.brutal_mode]

    def update(brutal_self, brutal_context):
        idaapi.update_action_icon(brutal_context.action, brutal_self.icon)
        return idaapi.AST_ENABLE


class BrutalIDA(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = 'BRUTAL IDA'
    help = 'Block Redo & Undo To Achieve Legacy IDA'
    wanted_name = 'BRUTAL-IDA'
    wanted_hotkey = ''

    def handle_5x(brutal_self):
        idaapi.error('bTree error: Brutal. Just like the good ol\' days!')

    def handle_6x(brutal_self):
        idaapi.msg('Brutal. Just like the good ol\' days!\n')

    def dispatch_brutality(brutal_self):
        {
            '5.x': brutal_self.handle_5x,
            '6.x': brutal_self.handle_6x,
        }[brutal_self.brutal_action_handler.brutal_mode]()

    def init(brutal_self):
        brutal_self.brutal_action_handler = BrutalActionHandler()
        brutal_action_desc = idaapi.action_desc_t('BRUTAL', 'BRUTAL IDA', brutal_self.brutal_action_handler, '',
                                                  'IDA', BRUTAL6_ICON)
        idaapi.register_action(brutal_action_desc)
        idaapi.create_toolbar('BRUTAL IDA', 'BRUTAL IDA')

        brutal_self.brutal_letter_handlers = []

        for brutal_letter in 'BRUTAL':
            brutal_letter_handler = BrutalLetterHandler()
            brutal_self.brutal_letter_handlers.append(brutal_letter_handler)

            brutal_label = 'BRUTAL {}'.format(brutal_letter)
            brutal_letter_desc = idaapi.action_desc_t(brutal_label,
                                                      brutal_label,
                                                      brutal_letter_handler,
                                                      '',
                                                      brutal_letter,
                                                      BRUTAL_LETTERS[brutal_letter])
            idaapi.register_action(brutal_letter_desc)
            idaapi.attach_action_to_toolbar('BRUTAL IDA', brutal_label)

        idaapi.attach_action_to_toolbar('BRUTAL IDA', 'BRUTAL')

        brutal_self.brutal_hotkeys = [
            idaapi.add_hotkey('Ctrl+Z', brutal_self.dispatch_brutality),
            idaapi.add_hotkey('Ctrl+Shift+Z', brutal_self.dispatch_brutality),
        ]

        return idaapi.PLUGIN_KEEP

    def term(brutal_self):
        pass

    def run(brutal_self, arg):
        pass


def PLUGIN_ENTRY():
    return BrutalIDA()
