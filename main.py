import time
from nicegui import ui

dark = ui.dark_mode()
ui.label('Switch mode: ')
ui.button('Dark', on_click=dark.enable)
ui.button('Light', on_click=dark.disable)

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
}).classes('container m-auto p-auto border-separate text-center')

def update():
    table.options['rowData'][0]['price'] += 1
    table.update()


ui.button(text='Редактировать', on_click=update).classes('container mx-auto px-auto text-center')

ui.run()