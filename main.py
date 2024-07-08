import time
from nicegui import ui

def darkMode():
    dark = ui.dark_mode()
    with ui.row().classes('flex flex-col justify-end ml-auto px-auto pb-10 items-center'):
        ui.label('Смена режима:').classes('flex flex-row py-auto my-auto font-mono text-center text-lg')
        with ui.button_group():
            ui.button(on_click=dark.enable, icon='dark_mode').props('outline')
            ui.button(on_click=dark.disable, icon='light_mode').props('outline')

darkMode()

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