class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass


class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


email = input()

while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, mail = email.split('@')
    domain = mail.split('.')
    domain = '.' + domain[1]
    valid_domains = ['.bg', '.com', '.org', '.net']
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
