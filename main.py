import time
from nicegui import ui

table = ui.aggrid({
    'defaultColDef': {'flex': 1},
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Price', 'field': 'price'},
        {'headerName': 'Quantity', 'field': 'quantity'},
    ],
    'rowData': [
        {'name': 'Тактический запас', 'price': 29000, 'quantity': 15},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40')

def update():
    table.options['rowData'][0]['price'] += 1
    table.update()


ui.button(text='Редактировать', on_click=update)

ui.run()