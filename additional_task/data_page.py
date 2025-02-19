class DataPage:
    def fill_columns(self, table, websocket_response):
        columns = []
        for i, row in enumerate(table):
            col_name = row['Columns View']
            if col_name in websocket_response:
                columns.append({'index': websocket_response[col_name]['index'], 'sort': i})
        return columns

    def fill_order_by(self, row, ws_response):
        return {'direction': row['Sort By'], 'index': ws_response['index']}