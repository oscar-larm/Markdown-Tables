''' Module for making tables in Markdown. '''

def make_budget():
    ''' Creates a budget formatted as a Markdown table. '''
    budget = {
        'column1': ['Categories', '-'],
        'column2': ['Budget', '-'],
        'column3': ['Actual', '-'],
        'column4': ['Difference', '-'],
        'total': 0,
        'spent': 0
        }
    budget['total'] = int(input('Input total budget: '))
    print(padding_seperate(budget))
    while True:
        inp = input('Enter category (empty to continue): ').title()
        if inp == '':
            for _ in range(50):
                print('\n')
            break

        budget['column1'].append(inp)
        for i in range(2, 5):
            budget[f'column{i}'].append(' ' * len(budget[f'column{i}'][0]))

        print(padding_seperate(budget))

    for i, row in enumerate(budget['column1'][2:]):
        print(padding_seperate(budget))

        print(f'Money Left: {budget['total']-budget['spent']}')

        inp = input(f'Enter budget for {row.strip()}: ')
        budget['spent'] += int(inp)

        budget['column2'][i + 2] = inp
        print(padding_seperate(budget))

    table_str = final_row(budget)
    print(table_str)
    save_inp = input('Would you like to save the table to a file? (y/n): ').lower()
    if save_inp == 'y':
        file_name = input("Enter where to save file (default is 'output.md'): ") or 'output.md'
        save_to_file(file_name, table_str)
    
    return table_str

def padding_seperate(budget):
    ''' Adds padding to all rows in columns 1 to 4 and adds seperator lines under the header row.'''
    for i in range(1, 5):
        max_len = len(max(budget[f'column{i}'], key=len))
        for x, row in enumerate(budget[f'column{i}']):
            row = row.ljust(max_len)
            budget[f'column{i}'][x] = row

    for i in range(1, 5):
        budget[f'column{i}'][1] = make_seperator_row(budget[f'column{i}'][0])

    return preview_table(budget)

def make_seperator_row(row: str):
    ''' Makes a seperator line for the arg string. '''
    seperator_row = '-' * len(row)
    return seperator_row

def preview_table(budget):
    ''' Returns a string of the table. '''
    for _ in range(50):
        print('\n')
    preview_str = ''
    column2 = budget['column2']
    column3 = budget['column3']
    column4 = budget['column4']

    for i, category in enumerate(budget['column1']):
        preview_str += f'| {category} | {column2[i]} | {column3[i]} | {column4[i]} |\n'
    return preview_str

def final_row(budget):
    ''' Adds the final row. '''
    budget['column1'].append('Total:')
    budget['column2'].append(f'{budget['spent']} ({budget['total'] - budget['spent']})')
    for i in range(3, 5):
        budget[f'column{i}'].append(' ' * len(budget[f'column{i}'][0]))
    return padding_seperate(budget)

def save_to_file(file_name, content):
    ''' Save the table to a file. '''
    try:
        while True:
            with open(file_name, encoding='utf-8') as handle:
                handle.read()
            inp = input('Theres already a file with this name. Overwrite the file? (y/n)').lower()
            if inp == 'y':
                break
            if inp == 'n':
                print(f'Appending the table to {file_name}')
                with open(file_name, 'a', encoding='utf-8') as handle:
                    handle.write('\n'+content)
                    print(f'Table has been appended to {file_name}.')
                return

            print("Not a valid option. Enter 'y' or 'n'.")

    except FileNotFoundError:
        pass
    with open(file_name, 'w', encoding='utf-8') as handle:
        handle.write(content)
        print(f'Table has been saved to {file_name}.')

    return
