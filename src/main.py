import tokenize


def is_comment(token: tokenize.TokenInfo) -> bool:
    return token and token.string and token.string[0] == '#'
def flatten_single_array(array: list):
    while isinstance(array, list) and len(array) == 1 and isinstance(array[0], list):
        array = array[0]
    return array
def parse_data_type_options(tokens: list[tokenize.TokenInfo]) -> list[tokenize.TokenInfo]:
    options = []
    temp_options = []
    while token := next(tokens):
        if token and token.type == tokenize.NAME:
            temp_options.append(token)
        elif token and token.string == '*':
            # options -> [E, F] > E * F
            # temp_options -> [T, A] > T | A
            # Current line > ...before T | A *
            options.append(flatten_single_array(temp_options))
            temp_options = []
        elif token and token.string == '|':
            pass
            # token = next(tokens)
            # temp_options.append(token)
        elif token and token.string == '(':
            new_options = parse_data_type_options(tokens)
            if new_options:
                temp_options.append(flatten_single_array(new_options))
        elif token and token.string == ')':
            options.append(flatten_single_array(temp_options))
            break
        elif token and is_new_line(token):
            options.append(flatten_single_array(temp_options))
            break
        elif token and not is_new_line(token):
            raise Exception('Unexpected token ahead in line', token.start[0], token.string)
        else:
            raise Exception('EOF', token.start[0], token.string)
    return options
def new_identifier_parse(tokens: list[tokenize.TokenInfo]):
    # Current token will be after the `=`, so any type created this way will have its options right now or the parameters valid for a function if it is a function

    options = parse_data_type_options(tokens)

    return options

    # We are valid so far


def is_new_line(token: tokenize.TokenInfo) -> bool:
    return token and token.string and token.string == '\n'

def return_tokens_in_string(options: list[tokenize.TokenInfo]) -> list[str]:
    new_options = []
    options = flatten_single_array(options)
    for item in options:
        if isinstance(item, list):
            new_options.append(return_tokens_in_string(item))
        else:
            new_options.append(item.string)
    return new_options

def main() -> None:
    try:
        with open('../impl.rene') as file:
            tokens = tokenize.generate_tokens(file.readline)
            # src_string = 'Tetromino = I | L | J | O | S | Z | T'
            # tokens = tokenize.tokenize(src_string)
            comments = []
            identifiers = []

            while token := next(tokens):
                if is_comment(token):
                    comments.append(token)
                elif is_new_line(token):
                    pass
                else:
                    token = next(tokens)
                    if token and token.string != '=':
                        raise Exception('Missing `=` in line, functions implements are no go right now', token.start[0],
                                        token.string)
                    options = new_identifier_parse(tokens)
                    # identifiers.append(token)
                    print('Identifier:->\n\tCurrent options->\n', return_tokens_in_string(options))


                # print(token.start[0], token.start[1], '-', token.string)
    except StopIteration as e:
        print(e)


if __name__ == '__main__':
    main()
