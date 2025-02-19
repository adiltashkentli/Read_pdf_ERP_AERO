from data_page import DataPage
from processing_page import ProcessingPage

class MainPage:
    def __init__(self):
        self.result = {
            'columns': [],
            'order_by': {},
            'conditions_data': {},
            'page_size': '',
            'row_height': '',
            'color_conditions': {},
            'module': 'SO'
        }
        self.data_page = DataPage()
        self.processing_page = ProcessingPage()

    def process_table(self, table, websocket_response, base_ws):
        # Заполняем columns
        self.result['columns'] = self.data_page.fill_columns(table, websocket_response)

        # Обрабатываем Sort By, Row Height, Lines per page
        for row in table:
            col_name = row['Columns View']
            if row.get('Sort By'):
                self.result['order_by'] = self.data_page.fill_order_by(row, websocket_response[col_name])
            
            if row.get('Lines per page'):
                self.result['page_size'] = row['Lines per page']
            
            if row.get('Row Height'):
                self.result['row_height'] = row['Row Height']

        # Обрабатываем Condition и Highlight By
        for row in table:
            col_name = row['Columns View']
            if row.get('Condition'):
                self.result['conditions_data'].update(
                    self.processing_page.process_conditions(row, websocket_response[col_name]['filter'])
                )
            
            if row.get('Highlight By') or not row.get('Highlight By'):
                self.result['color_conditions'].update(
                    self.processing_page.process_highlights(row, websocket_response[col_name]['filter'])
                )

        return self.result