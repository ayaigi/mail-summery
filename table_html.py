class table_html():
    
    table_str = ''
    width: int
    
    def __init__(self, Width: int):
        self.width = Width
        
    def print(self) -> str: 
        return "<table>{}</table>".format(self.table_str)
    
    def add_row(self, li: list):
        rt = '<tr>'
        for i in li:
            rt = '{}<td>{}</td>'.format(rt, i)
        rt = '{}{}'.format(rt, '</tr>')
        self.table_str = self.table_str + rt
        
    def add_header_row(self, li: str):
        rt = "<tr><th colspan={}>{}</th></tr>".format(self.width, li)
        self.table_str = self.table_str + rt