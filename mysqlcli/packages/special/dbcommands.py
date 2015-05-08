def parse_special_command(sql):
    command, _, arg = sql.partition(' ')

    command = command.strip()
    return (command, arg.strip())

def reconnect(cur, sql, executor):
    _, name = parse_special_command()
    executor.connect(database=name)
    return [(None, None, None, 'Connected to ' + name)]
