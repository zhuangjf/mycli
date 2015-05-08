from collections import namedtuple

# Meta data about each special command.
# name - Name of the special command.
# shortcut - Short form that typically starts with a slash,
# help - docstring for the command,
# handler - function or sql to execute to produce results for the special cmd,
# detector - a function  to detect if an sql command matches the command
_SpecialCommand = namedtuple('SpecialCommand',
        ['name', 'shortcut', 'help', 'handler', 'detector'])

class SpecialCommands(object):
    commands = [
            _SpecialCommand('\?', '\\?', 'Display this help.', show_help, start),
            _SpecialCommand('\h', '\\?', 'Display this help.', show_help, start),
            _SpecialCommand('\h', '\\?', 'Display this help.', show_help, start),
            _SpecialCommand('connect', '\\r', 'Reconnect to the server', dbcommands.reconnect, start),
            _SpecialCommand('ego', '\\G', 'Display results vertically.', iocommands.expanded_output, end),
            ]

    def detect(self, statement):
        for command in self.commands:
            if (command.detector(command.name, statement) or
                    command.detector(command.shortcut, statement)):
                return command.name

    def execute(self, cur, sql, sqlexecute=None):
        """Execute a special command and return the results. If the special command
        is not supported None will be returned.
        """
        command = self.detect(sql)
        if command is None:
            return None

        executor = command.handler
        if callable(executor):
            return executor(cur, sql, sqlexecute)
        elif isinstance(executor, str):
            cur.execute(executor)
            if cur.description:
                headers = [x[0] for x in cur.description]
                return [(None, cur, headers, cur.statusmessage)]
            else:
                return [(None, None, None, cur.statusmessage)]
