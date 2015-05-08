"""List of special commands supported by MySQL that doesn't touch the
database."""

def extract_sql_expanded(sql):
    if sql.endswith('\\G'):
        return sql.rsplit('\\G')
    return sql

def expanded_output(*args):
    raise NotImplementedError
