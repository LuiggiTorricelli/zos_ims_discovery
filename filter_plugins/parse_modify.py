from __future__ import absolute_import, division, print_function

__metaclass__ = type
import re

class FilterModule(object):
    def filters(self):
        filters = {
            "parse_modify": self.parse_modify,
        }
        return filters
    
    def parse_modify(self, cmd_response):
        if isinstance(cmd_response, list):
            joined_content = '\n'.join(cmd_response)
        elif isinstance(cmd_response, str):
            joined_content = cmd_response

        # For /DIS MODIFY parsing,
        if " DFS4444I " in joined_content:
            msg = "DFS4444I"
            extract_libs = re.findall(r'(LIBRARY +[\s\S]+?)(?=LIBRARY|DISPLAY MODIFY)', joined_content)
            libs = []
            for lib in extract_libs:
                parse_vals = re.findall(r' *(\S+) +(\S+)', lib)[0]
                parse_datasets = re.findall(r'\(([ UAI])\) +(.+)', lib)
                data_sets = []
                for dataset in parse_datasets:
                    match dataset[0]:
                        case 'A':
                            tmp_status = 'ACTIVE'
                        case 'I':
                            tmp_status = 'INACTIVE'
                        case 'U':
                            tmp_status = 'UNALLOCATED'
                        case '_':
                            tmp_status = ''
                    tmp_dataset = {
                        "status": tmp_status,
                        "data_set": dataset[1],
                    }
                    data_sets.append(tmp_dataset)
                resource_type = parse_vals[0]
                resource_name = parse_vals[1]
                tmp_lib = {
                    "resource_type": resource_type,
                    "resource_name": resource_name,
                    "data_sets": data_sets,
                }
                libs.append(tmp_lib)
            tmp_result = {
                "libraries": libs,
            }
            result = {
                "system": re.findall(r' *(\w+) +.+' + msg + '.+\n', joined_content)[0],
                "datetime": re.findall(r' *\w+ +(.+?) +' + msg + '.+\n', joined_content)[0],
                "content": {
                    "modify": tmp_result,
                }
            }
        else:
            result = cmd_response
        return result