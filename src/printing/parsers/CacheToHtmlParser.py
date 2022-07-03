from parsers.IParser import IParser


class CacheToHtmlParser(IParser):
    def parse(self, list):
        html = '''<table>
                <tr>
                    <th>Id</th>
                    <th>Type</th>
                    <th>Content</th>
                </tr>'''

        for dict in list:
            html += f'<tr>'
            html += f'<td>{dict["id"]}</td>'
            html += f'<td>{dict["type"]}</td>'
            html += f'<td>{dict["content"]}</td>'
            html += f'</tr>\n'

        html += '</table>'
        return html