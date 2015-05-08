from collections import namedtuple

# Meta data about each special command.
# name - Name of the special command.
# shortcut - Short form that typically starts with a slash,
# help - docstring for the command,
# handler - function or sql to execute to produce results for the special cmd,
# detector - a function  to detect if an sql command matches the command
SpecialCommand = namedtuple('SpecialCommand',
        ['name', 'shortcut', 'help', 'handler', 'detector'])

def detect_special_command(statement):
    from main import CASE_SENSITIVE_COMMANDS
    for _, command in sorted(CASE_SENSITIVE_COMMANDS.items()):
        if (command.detector(command.name, statement) or
                command.detector(command.shortcut, statement)):
            return command.name

def start(command, statement):
    return statement.startswith(command)

def end(command, statement):
    return statement.endswith(command)

def start_or_end(command, statement):
    return statement.startswith(command) or statement.endswith(command)

if __name__ == '__main__':
    print detect_special_command('select * from blah\G')
