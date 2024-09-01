def banner(text:str=' ', screenwide:int=50) -> None: 
    """
    The banner function prints text in the center which a user need to print.
    It has two parameters which are `str` and `int` inputs.

    :param text: text that will be printed
    :param screenwide: size of the screen
    :raises ValueError: if the supplied string is too long to fit.
    :return: `None`
    """
    
    if len(text) > screenwide-4:
        raise ValueError(f'{text} is too long')
    if text=='*':
        print(text*screenwide)
    else:
        center_text = text.center(screenwide-4)
        print(f'**{center_text}**')

banner('*')
banner(screenwide=60)
banner('My name is Munna')
banner('I\'m a software engineer')
banner()
banner('*')
print(banner.__doc__)
# text = 'lormmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'
# banner(text)