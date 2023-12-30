def get_contacts():
    return {'tel': 12345678,
            'address': 'address',
            'email': 'info@mail.com'}


def get_product():
    return [{'id': i + 1, 'name': f'product{i + 1}', 'description': f'product{i + 1}', 'price': 99} for i in range(5)]
