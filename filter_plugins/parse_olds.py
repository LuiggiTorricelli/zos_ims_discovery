from __future__ import absolute_import, division, print_function

__metaclass__ = type
import re

class FilterModule(object):
    def filters(self):
        filters = {
            "parse_olds": self.parse_olds,
        }
        return filters
    
    def parse_olds(self, cmd_response):
        if isinstance(cmd_response, list):
            joined_content = '\n'.join(cmd_response)
        elif isinstance(cmd_response, str):
            joined_content = cmd_response

        # For /DIS OLDS parsing,
        if " DFS4444I " in joined_content:
            msg = "DFS4444I"
            extract_olds = joined_content[joined_content.find('OLDS-DDNAME'):joined_content.find('OLDS LOGGING') - 10].strip()
            extract_olds_list = re.findall(r'^ +(?:\*|)([^\n]{8}) ([^\n]{11}) ([^\n]{11}) ([^\n]{12})(?: |)(.+|)', extract_olds, re.MULTILINE)
            olds = []
            for i in extract_olds_list:
                olds_ddname = i[0].strip() if len(i[0].strip()) > 0 else None
                olds_percentage_full_rate = i[1].strip() if len(i[1].strip()) > 0 else None
                olds_arch_job = i[2].strip() if len(i[2].strip()) > 0 else None
                olds_arch_status = i[3].strip() if len(i[3].strip()) > 0 else None
                olds_other_status = i[4].strip() if len(i[4].strip()) > 0 else None
                tmp_olds = {
                    "ddname": olds_ddname,
                    "percentage_full_rate": olds_percentage_full_rate,
                    "arch_job": olds_arch_job,
                    "arch_status": olds_arch_status,
                    "other_status": olds_other_status,
                }
                olds.append(tmp_olds)
            logging_olds = re.sub(r'[\s\S]+?(DUAL|DEGRADED DUAL|NONDEGRADABLE DUAL|SINGLE) OLDS LOGGING[\s\S]+', r'\1', joined_content)
            logging_wads = re.sub(r'[\s\S]+?(DUAL|SINGLE|NO) WADS LOGGING[\s\S]+', r'\1', joined_content)
            automatic_archive = re.sub(r'[\s\S]+?AUTOMATIC ARCHIVE += +(\S+)[\s\S]+', r'\1', joined_content)
            wads = re.sub(r'[\s\S]+?WADS += +(.+)[\s\S]+', r'\1', joined_content).split(' ')
            sldsread = re.sub(r'[\s\S]+?SLDSREAD (\S+)[\s\S]+', r'\1', joined_content)
            current_bsn = re.sub(r'[\s\S]+?CURRENT BSN += +(\S+),[\s\S]+', r'\1', joined_content)
            current_lsn = re.sub(r'[\s\S]+?CURRENT BSN += +\S+, +LSN += +(\S+)[\s\S]+', r'\1', joined_content)
            zhyperwrite_olds = re.sub(r'[\s\S]+?ZHYPERWRITE: +OLDS += +(\S+),[\s\S]+', r'\1', joined_content)
            zhyperwrite_wads = re.sub(r'[\s\S]+?ZHYPERWRITE: +OLDS += +\S+, +WADS += +(\S+)[\s\S]+', r'\1', joined_content)
            tmp_result = {
                "olds": olds,
                "logging_olds": logging_olds,
                "logging_wads": logging_wads,
                "automatic_archive": automatic_archive,
                "wads": wads,
                "sldsread": sldsread,
                "current_bsn": current_bsn,
                "current_lsn": current_lsn,
                "zhyperwrite_olds": zhyperwrite_olds,
                "zhyperwrite_wads": zhyperwrite_wads,
            }
            result = {
                "system": re.findall(r' *(\w+) +.+' + msg + '.+\n', joined_content)[0],
                "datetime": re.findall(r' *\w+ +(.+?) +' + msg + '.+\n', joined_content)[0],
                "content": {
                    "olds": tmp_result,
                }
            }
        else:
            result = cmd_response
        return result