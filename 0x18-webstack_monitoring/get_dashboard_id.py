#!/usr/bin/python3
"""
Get all dashboard lists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi('49558efcf0bad444c5471415a5c53e7efb8e7481')
    response = api_instance.list_dashboard_lists()

    print(response)
