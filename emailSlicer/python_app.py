def main():
    print('Welcome to the e-mail slicer :)\n')

    email_input = input('Enter your e-mail address: ')

    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print(f'Username: {username}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension}')


main()
