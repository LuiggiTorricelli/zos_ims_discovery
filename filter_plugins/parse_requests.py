from __future__ import absolute_import, division, print_function

__metaclass__ = type
import re

class FilterModule(object):
    def filters(self):
        filters = {
            "parse_requests": self.parse_requests,
        }
        return filters
    
    def parse_requests(self, cmd_response):
        if isinstance(cmd_response, list):
            joined_content = '\n'.join(cmd_response)
        elif isinstance(cmd_response, str):
            joined_content = cmd_response

        # For D R,L,SN parsing,
        if " IEE112I " in joined_content:
            msg = "IEE112I"
            entries = re.findall(r' +(\d+) +(\w) +(\S+) +(\S+) +([\s\S]+?(?= *?        \d+)|[\s\S]+)', joined_content)
            requests = []
            for entry in entries:
                fix_message = re.sub(r' *\n +', ' ', entry[4])
                fix_message = re.sub(r'\n$', '', fix_message)
                tmp_result = {
                    "id": entry[0],
                    "type": entry[1],
                    "system": entry[2],
                    "job_name": entry[3],
                    "message": fix_message,
                }
                requests.append(tmp_result)
            result = {
                "system": re.findall(r' *(\w+) +.+' + msg + '.+\n', joined_content)[0],
                "datetime": re.findall(r' *\w+ +(.+?) +' + msg + '.+\n', joined_content)[0],
                "content": {
                    "requests": requests,
                }
            }
        else:
            result = cmd_response
        return result