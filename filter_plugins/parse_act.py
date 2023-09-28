from __future__ import absolute_import, division, print_function

__metaclass__ = type
import re

class FilterModule(object):
    def filters(self):
        filters = {
            "parse_act": self.parse_act,
        }
        return filters
    
    def parse_act(self, cmd_response):
        if isinstance(cmd_response, list):
            joined_content = '\n'.join(cmd_response)
        elif isinstance(cmd_response, str):
            joined_content = cmd_response

        # For /DIS ACT parsing,
        if " DFS4444I " in joined_content:
            msg = "DFS4444I"
            tmp_content = re.sub(r'( +\+.+?)\n +(.+?)', r'\1\2', joined_content)
            tmp_content = re.sub(r'( +)\+( +)', r'\1 \2', tmp_content)
            extract_regions = tmp_content[tmp_content.find('REGID JOBNAME'):tmp_content.find('VTAM ACB')]
            extract_regions_list = re.findall(r'^ +(\d*) (\S{1,9}) +([^\n]{5})(?: |)([^\n]{1,9}|)(?: |)([^\n]{1,8}|)(?: |)([^\n]{16}|)(?: |)(.+|)', extract_regions, re.MULTILINE)
            regions = []
            for i in extract_regions_list:
                reg_id = i[0].strip() if len(i[0].strip()) > 0 else None
                reg_jobname = i[1].strip() if len(i[1].strip()) > 0 else None
                reg_type = i[2].strip() if len(i[2].strip()) > 0 else None
                if len(i[3].strip()) > 0 and i[3].strip() != 'NONE':
                    reg_tran_or_step = i[3].strip()
                else:
                    reg_tran_or_step = None
                reg_program = i[4].strip() if len(i[4].strip()) > 0 else None
                reg_status = i[5].strip() if len(i[5].strip()) > 0 else None
                reg_classes = list(map(int, i[6].strip().replace(' ', '').split(','))) if len(i[6].strip()) > 0 else None
                tmp_region = {
                    "id": reg_id,
                    "jobname": reg_jobname,
                    "type": reg_type,
                    "tran_or_step": reg_tran_or_step,
                    "program": reg_program,
                    "status": reg_status,
                    "classes": reg_classes,
                }
                regions.append(tmp_region)
            vtam_acb = re.sub(r'[\s\S]+?VTAM ACB (\S+)[\s\S]+', r'\1', tmp_content)
            logons = re.sub(r'[\s\S]+?-LOGONS (\S+)[\s\S]+', r'\1', tmp_content)
            imslu = re.sub(r'[\s\S]+?IMSLU=(\S+)[\s\S]+', r'\1', tmp_content)
            appc_status = re.sub(r'[\s\S]+?APPC STATUS=(\S+)[\s\S]+', r'\1', tmp_content)
            timeout = re.sub(r'[\s\S]+?TIMEOUT= *(\S+)[\s\S]+', r'\1', tmp_content)
            maxc = re.sub(r'[\s\S]+?MAXC= *(\S+)[\s\S]+', r'\1', tmp_content)
            otma_group_name = re.sub(r'[\s\S]+?OTMA GROUP= *(\S+)[\s\S]+', r'\1', tmp_content)
            otma_group_status = re.sub(r'[\s\S]+?OTMA GROUP=.+STATUS= *(\S+)[\s\S]+', r'\1', tmp_content)
            appc_otma_shared_queue_status_local = re.sub(r'[\s\S]+?APPC/OTMA SHARED QUEUE STATUS.+LOCAL= *(\S+)[\s\S]+', r'\1', tmp_content)
            appc_otma_shared_queue_status_global = re.sub(r'[\s\S]+?APPC/OTMA SHARED QUEUE STATUS.+GLOBAL= *(\S+)[\s\S]+', r'\1', tmp_content)
            appc_otma_shared_queues_logging = re.sub(r'[\s\S]+?APPC/OTMA SHARED QUEUES LOGGING= *(\S+)[\s\S]+', r'\1', tmp_content)
            appc_otma_rrs_max_tcbs = re.sub(r'[\s\S]+?APPC/OTMA RRS MAX TCBS *- *(\S+)[\s\S]+', r'\1', tmp_content)
            appc_otma_rrs_attached_tcbs = re.sub(r'[\s\S]+?APPC/OTMA RRS.+ATTACHED TCBS *- *(\S+)[\s\S]+', r'\1', tmp_content)
            appc_otma_rrs_queued_rrswks = re.sub(r'[\s\S]+?APPC/OTMA RRS.+QUEUED RRSWKS *- *(\S+)[\s\S]+', r'\1', tmp_content)
            applid = re.sub(r'[\s\S]+?APPLID= *(\S+)[\s\S]+', r'\1', tmp_content)
            grsname = re.sub(r'[\s\S]+?GRSNAME= *(\S+)[\s\S]+', r'\1', tmp_content)
            applid_status = re.sub(r'[\s\S]+?APPLID=.+STATUS= *(\S+)[\s\S]+', r'\1', tmp_content)
            tcpip_genimsid = re.sub(r'[\s\S]+?TCPIP_GENIMSID=(\S+)[\s\S]+', r'\1', tmp_content)
            tcpip_genimsid_status = re.sub(r'[\s\S]+?TCPIP_GENIMSID=.+?STATUS= *(\S+)[\s\S]+', r'\1', tmp_content)
            line_active_in = re.sub(r'[\s\S]+?LINE ACTIVE-IN *- *(\S+)[\s\S]+', r'\1', tmp_content)
            line_active_out = re.sub(r'[\s\S]+?LINE ACTIVE-IN.* ACTIV-OUT *- *(\S+)[\s\S]+', r'\1', tmp_content)
            node_active_in = re.sub(r'[\s\S]+?NODE ACTIVE-IN *- *(\S+)[\s\S]+', r'\1', tmp_content)
            node_active_in = re.sub(r'[\s\S]+?NODE ACTIVE-IN *- *(\S+)[\s\S]+', r'\1', tmp_content)
            link_active_out = re.sub(r'[\s\S]+?LINK ACTIVE-IN.* ACTIV-OUT *- *(\S+)[\s\S]+', r'\1', tmp_content)
            link_active_out = re.sub(r'[\s\S]+?LINK ACTIVE-IN.* ACTIV-OUT *- *(\S+)[\s\S]+', r'\1', tmp_content)
            # Variable cleanup
            vtam_acb = None if vtam_acb == tmp_content else vtam_acb
            logons = None if logons == tmp_content else logons
            imslu = None if imslu == tmp_content else imslu
            appc_status = None if appc_status == tmp_content else appc_status
            timeout = None if timeout == tmp_content else timeout
            maxc = None if maxc == tmp_content else maxc
            otma_group_name = None if otma_group_name == tmp_content else otma_group_name
            otma_group_status = None if otma_group_status == tmp_content else otma_group_status
            appc_otma_shared_queue_status_local = None if appc_otma_shared_queue_status_local == tmp_content else appc_otma_shared_queue_status_local
            appc_otma_shared_queue_status_global = None if appc_otma_shared_queue_status_global == tmp_content else appc_otma_shared_queue_status_global
            appc_otma_shared_queues_logging = None if appc_otma_shared_queues_logging == tmp_content else appc_otma_shared_queues_logging
            appc_otma_rrs_max_tcbs = None if appc_otma_rrs_max_tcbs == tmp_content else appc_otma_rrs_max_tcbs
            appc_otma_rrs_attached_tcbs = None if appc_otma_rrs_attached_tcbs == tmp_content else appc_otma_rrs_attached_tcbs
            appc_otma_rrs_queued_rrswks = None if appc_otma_rrs_queued_rrswks == tmp_content else appc_otma_rrs_queued_rrswks
            applid = None if applid == tmp_content else applid
            grsname = None if grsname == tmp_content else grsname
            applid_status = None if applid_status == tmp_content else applid_status
            tcpip_genimsid = None if tcpip_genimsid == tmp_content else tcpip_genimsid
            tcpip_genimsid_status = None if tcpip_genimsid_status == tmp_content else tcpip_genimsid_status
            line_active_in = None if line_active_in == tmp_content else line_active_in
            line_active_out = None if line_active_out == tmp_content else line_active_out
            node_active_in = None if node_active_in == tmp_content else node_active_in
            node_active_in = None if node_active_in == tmp_content else node_active_in
            link_active_out = None if link_active_out == tmp_content else link_active_out
            link_active_out = None if link_active_out == tmp_content else link_active_out
            
            tmp_result = {
                "regions": regions,
                "vtam_acb": vtam_acb,
                "logons": logons,
                "imslu": imslu,
                "appc_status": appc_status,
                "timeout": timeout,
                "maxc": maxc,
                "otma_group_name": otma_group_name,
                "otma_group_status": otma_group_status,
                "appc_otma_shared_queue_status_local": appc_otma_shared_queue_status_local,
                "appc_otma_shared_queue_status_global": appc_otma_shared_queue_status_global,
                "appc_otma_shared_queues_logging": appc_otma_shared_queues_logging,
                "appc_otma_rrs_max_tcbs": appc_otma_rrs_max_tcbs,
                "appc_otma_rrs_attached_tcbs": appc_otma_rrs_attached_tcbs,
                "appc_otma_rrs_queued_rrswks": appc_otma_rrs_queued_rrswks,
                "applid": applid,
                "grsname": grsname,
                "applid_status": applid_status,
                "tcpip_genimsid": tcpip_genimsid,
                "tcpip_genimsid_status": tcpip_genimsid_status,
                "line_active_in": line_active_in,
                "line_active_out": line_active_out,
                "node_active_in": node_active_in,
                "node_active_in": node_active_in,
                "link_active_out": link_active_out,
                "link_active_out": link_active_out,
            }
            result = {
                "system": re.findall(r' *(\w+) +.+' + msg + '.+\n', joined_content)[0],
                "datetime": re.findall(r' *\w+ +(.+?) +' + msg + '.+\n', joined_content)[0],
                "content": {
                    "act": tmp_result,
                }
            }
        else:
            result = cmd_response
        return result