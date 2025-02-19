class ProcessingPage:
    def process_conditions(self, row, filter_key):
        conditions = []
        for cond in row['Condition'].split(','):
            parts = cond.split('=')
            if len(parts) == 2:
                cond_type, value = parts
                conditions.append({'type': cond_type, 'value': value})
        return {filter_key: conditions}

    def process_highlights(self, row, filter_key):
        highlights = []
        if row.get('Highlight By'):
            for highlight in row['Highlight By'].split(','):
                parts = highlight.split('=')
                if len(parts) == 3:
                    cond_type, value, color = parts
                elif len(parts) == 2:
                    cond_type, value = parts
                    color = ''
                else:
                    continue  # Пропускаем некорректные записи
                highlights.append({'type': cond_type, 'value': value, 'color': color})
        return {filter_key: highlights}