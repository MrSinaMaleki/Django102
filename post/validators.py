from django.core.exceptions import ValidationError


def len_min(title):
    if len(title) < 3:
        print(f"{title} is not longer than 3!")
        raise ValidationError("Not longer than 3!")


def author_name_valid(author: str):
    if not author.isalpha():
        raise ValidationError("Author's name cannot contain number or symbols!")
