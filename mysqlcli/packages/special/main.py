from helpers import SpecialCommand, start, end, start_or_end, parse_special_command
import iocommands
#import dbcommands

__all__ = ['show_help']

def show_help(*args):
    header = ['Command', 'Shortcut', 'Description']
    footer = None
    result = [(x.name, x.shortcut, x.help) for _, x in sorted(CASE_SENSITIVE_COMMANDS.items())]
    return [(result, header, footer)]


CASE_SENSITIVE_COMMANDS = {
        '?': SpecialCommand('\?', '\\?', 'Display this help.', show_help, start),
        'help': SpecialCommand('\h', '\\?', 'Display this help.', show_help, start),
        '\h': SpecialCommand('\h', '\\?', 'Display this help.', show_help, start),
        #'\\r': SpecialCommand('connect', '\\r', 'Reconnect to the server', dbcommands.reconnect, start),
        'ego': SpecialCommand('ego', '\\G', 'Display results vertically.', iocommands.expanded_output, end)
        }

def execute(executor, sql):
    """Execute a special command and return the results. If the special command
    is not supported a KeyError will be raised.
    """
    special_command = detect_special_command(sql)
    if special_command is None:
        return None

    CASE_SENSITIVE_COMMANDS




if __name__ == '__main__':
    print show_help()
