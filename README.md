zos_ims_discovery
=================

The Ansible role 'zos_ims_discovery' will perform a sequence of steps to identify IMS subsystems running on either the specific z/OS LPAR or z/OS sysplex where Ansible is connecting to.

Requirements
============

Python and Z Open Automation Utilities must be installed on the remote z/OS system, since the module ibm.ibm_zos_core.zos_operator is used along the role.

Role Variables
==============

Available variables are listed below, along with default values:

    # Identifies if the IMSs should be discovered by SYSPLEX or LPAR
    scope: SYSPLEX
  
Set the scope of the discovery, if it should identify IMS subsystems available only on the connected LPAR or the sysplex. Available options are: [LPAR, SYSPLEX].

Dependencies
============

None.

Example Playbook (with default scope)
=====================================

    - hosts: zos_server
      roles:
        - role: zos_ims_discovery

Example Playbook (with scope being specified)
=============================================

    - hosts: zos_server
      roles:
        - role: zos_ims_discovery
          scope: lpar

Sample Output
=============

When this role is successfully executed, a fact named `zos_ims_discovery_ims_information` will be set. It is a list of dictionaries, with each item being a discovered IMS subsystem and the collected information about it (region and DC information, online logs, online change libraries, etc.).

    "zos_ims_discovery_ims_information": [
        {
            "act": {
                "appc_otma_rrs_attached_tcbs": "2",
                "appc_otma_rrs_max_tcbs": "40",
                "appc_otma_rrs_queued_rrswks": "0",
                "appc_otma_shared_queue_status_global": "ACTIVE-XCF",
                "appc_otma_shared_queue_status_local": "ACTIVE-XCF",
                "appc_otma_shared_queues_logging": "N",
                "appc_status": "ENABLED",
                "applid": "NTEST990",
                "applid_status": "ACTIVE",
                "grsname": "TSTXXX12",
                "imslu": "XXX.NTEST990",
                "line_active_in": "1",
                "line_active_out": "0",
                "link_active_out": "0",
                "logons": "ENABLED",
                "maxc": "5000",
                "node_active_in": "0",
                "otma_group_name": "MQXCF",
                "otma_group_status": "ACTIVE",
                "regions": [
                    {
                        "classes": [
                            21,
                            50
                        ],
                        "id": "8",
                        "jobname": "IMS1M006",
                        "program": null,
                        "status": "WAITING",
                        "tran_or_step": null,
                        "type": "TP"
                    },
                    {
                        "classes": [
                            5,
                            10,
                            25
                        ],
                        "id": "7",
                        "jobname": "IMS1M005",
                        "program": null,
                        "status": "WAITING",
                        "tran_or_step": null,
                        "type": "TP"
                    },
                    {
                        "classes": [
                            4,
                            10,
                            24
                        ],
                        "id": "6",
                        "jobname": "IMS1M004",
                        "program": null,
                        "status": "WAITING",
                        "tran_or_step": null,
                        "type": "TP"
                    },
                    {
                        "classes": [
                            1,
                            10,
                            21,
                            9
                        ],
                        "id": "5",
                        "jobname": "IMS1M001",
                        "program": null,
                        "status": "WAITING",
                        "tran_or_step": null,
                        "type": "TP"
                    },
                    {
                        "classes": [
                            3,
                            10,
                            23
                        ],
                        "id": "4",
                        "jobname": "IMS1M003",
                        "program": null,
                        "status": "WAITING",
                        "tran_or_step": null,
                        "type": "TP"
                    },
                    {
                        "classes": [
                            2,
                            10,
                            22
                        ],
                        "id": "3",
                        "jobname": "IMS1M002",
                        "program": null,
                        "status": "WAITING",
                        "tran_or_step": null,
                        "type": "TP"
                    },
                    {
                        "classes": null,
                        "id": null,
                        "jobname": "JMPRGN",
                        "program": null,
                        "status": null,
                        "tran_or_step": null,
                        "type": "JMP"
                    },
                    {
                        "classes": null,
                        "id": "1",
                        "jobname": "IMS1MQ",
                        "program": "CSQQTRMN",
                        "status": null,
                        "tran_or_step": "IMS1MQ",
                        "type": "BMPE"
                    },
                    {
                        "classes": null,
                        "id": null,
                        "jobname": "JBPRGN",
                        "program": null,
                        "status": null,
                        "tran_or_step": null,
                        "type": "JBP"
                    },
                    {
                        "classes": null,
                        "id": null,
                        "jobname": "FPRGN",
                        "program": null,
                        "status": null,
                        "tran_or_step": null,
                        "type": "FP"
                    },
                    {
                        "classes": null,
                        "id": null,
                        "jobname": "DBTRGN",
                        "program": null,
                        "status": null,
                        "tran_or_step": null,
                        "type": "DBT"
                    },
                    {
                        "classes": null,
                        "id": null,
                        "jobname": "IMS1DBRC",
                        "program": null,
                        "status": null,
                        "tran_or_step": null,
                        "type": "DBRC"
                    },
                    {
                        "classes": null,
                        "id": null,
                        "jobname": "IMS1DLI",
                        "program": null,
                        "status": null,
                        "tran_or_step": null,
                        "type": "DLS"
                    }
                ],
                "tcpip_genimsid": null,
                "tcpip_genimsid_status": "DISABLED",
                "timeout": "2",
                "vtam_acb": "OPEN"
            },
            "job_name": "IMS1CTL",
            "modify": {
                "libraries": [
                    {
                        "data_sets": [
                            {
                                "data_set": "IMSVS.IMS1.TECH.ACBLIBA",
                                "status": "UNALLOCATED"
                            },
                            {
                                "data_set": "IMSVS.IMS1.ACBLIBA",
                                "status": "UNALLOCATED"
                            },
                            {
                                "data_set": "IMSVS.IMS1.FILEAID.ACBLIB",
                                "status": "UNALLOCATED"
                            }
                        ],
                        "resource_name": "IMSACBA",
                        "resource_type": "LIBRARY"
                    },
                    {
                        "data_sets": [
                            {
                                "data_set": "IMSVS.IMS1.TECH.FORMATA",
                                "status": "ACTIVE"
                            },
                            {
                                "data_set": "IMSVS.IMS1.FORMATA",
                                "status": "ACTIVE"
                            }
                        ],
                        "resource_name": "FORMATA",
                        "resource_type": "LIBRARY"
                    },
                    {
                        "data_sets": [
                            {
                                "data_set": "IMSVS.IMS1A.MODBLKSA",
                                "status": "ACTIVE"
                            }
                        ],
                        "resource_name": "MODBLKSA",
                        "resource_type": "LIBRARY"
                    },
                    {
                        "data_sets": [
                            {
                                "data_set": "IMSVS.IMS1.TECH.ACBLIBB",
                                "status": "ACTIVE"
                            },
                            {
                                "data_set": "IMSVS.IMS1.ACBLIBB",
                                "status": "ACTIVE"
                            },
                            {
                                "data_set": "IMSVS.IMS1.FILEAID.ACBLIB",
                                "status": "ACTIVE"
                            }
                        ],
                        "resource_name": "IMSACBB",
                        "resource_type": "LIBRARY"
                    },
                    {
                        "data_sets": [
                            {
                                "data_set": "IMSVS.IMS1.TECH.FORMATB",
                                "status": "INACTIVE"
                            },
                            {
                                "data_set": "IMSVS.IMS1.FORMATB",
                                "status": "INACTIVE"
                            }
                        ],
                        "resource_name": "FORMATB",
                        "resource_type": "LIBRARY"
                    },
                    {
                        "data_sets": [
                            {
                                "data_set": "IMSVS.IMS1A.MODBLKSB",
                                "status": "INACTIVE"
                            }
                        ],
                        "resource_name": "MODBLKSB",
                        "resource_type": "LIBRARY"
                    }
                ]
            },
            "olds": {
                "automatic_archive": "01",
                "current_bsn": "0000FC81",
                "current_lsn": "00000000_0028277C",
                "logging_olds": "SINGLE",
                "logging_wads": "DUAL",
                "olds": [
                    {
                        "arch_job": "0",
                        "arch_status": null,
                        "ddname": "DFSOLP04",
                        "other_status": "IN USE",
                        "percentage_full_rate": "40"
                    },
                    {
                        "arch_job": null,
                        "arch_status": "AVAILABLE",
                        "ddname": "DFSOLP03",
                        "other_status": null,
                        "percentage_full_rate": null
                    },
                    {
                        "arch_job": null,
                        "arch_status": "AVAILABLE",
                        "ddname": "DFSOLP02",
                        "other_status": null,
                        "percentage_full_rate": null
                    },
                    {
                        "arch_job": null,
                        "arch_status": "AVAILABLE",
                        "ddname": "DFSOLP01",
                        "other_status": null,
                        "percentage_full_rate": null
                    },
                    {
                        "arch_job": null,
                        "arch_status": "AVAILABLE",
                        "ddname": "DFSOLP05",
                        "other_status": "STOPPED",
                        "percentage_full_rate": null
                    }
                ],
                "sldsread": "ON",
                "wads": [
                    "*DFSWADS1",
                    "*DFSWADS2",
                    "DFSWADS3",
                    "DFSWADS4"
                ],
                "zhyperwrite_olds": "NO",
                "zhyperwrite_wads": "NO"
            },
            "subsystem": "IMS1",
            "system": "NWRE"
        }
    ]

License
=======

This role is licensed under licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

Author Information
==================

This role was created in 2023 by Luiggi Torricelli, a Db2 for z/OS system programmer.
