#!/usr/bin/python3

'''
Lightweight python script to generate tables in Markdown.
'''
import md_table

def main():
    ''' Main loop for generating a table. '''
    print('\n'+md_table.make_budget()+'\n')

if __name__ == '__main__':
    main()
