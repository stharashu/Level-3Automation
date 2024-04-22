# import requests
# from robocorp import workitems
# from robocorp.tasks import task

# @task
# def consume_traffic_data():
#     """
#     Inhuman Insurance, Inc. Artificial Intelligence System automation.
#     Consumes traffic data work items.
#     """
#     for item in workitems.inputs:
#         if item.payload:
#             traffic_data = item.payload.get("traffic_data")
#             if traffic_data and len(traffic_data.get("country", "")) == 3:
#                 status, return_json = post_traffic_data_to_sales_system(traffic_data)
#                 if status == 200:
#                     item.done()
#                 else:
#                     item.fail(
#                         exception_type="APPLICATION",
#                         code="TRAFFIC_DATA_POST_FAILED",
#                         message=return_json.get("message", ""),
#                     )
#             else:
#                 item.fail(
#                     exception_type="BUSINESS",
#                     code="INVALID_TRAFFIC_DATA",
#                     message=item.payload,
#                 )
#         else:
#             item.fail(
#                 exception_type="APPLICATION",
#                 code="MISSING_PAYLOAD",
#                 message="No payload data found for the current work item.",
#             )

# def post_traffic_data_to_sales_system(traffic_data):
#     url = "https://robocorp.com/inhuman-insurance-inc/sales-system-api"
#     response = requests.post(url, json=traffic_data)
#     return response.status_code, response.json()

import json
import requests

from robocorp.tasks import task

@task
def consume_traffic_data():
    """
    Inhuman Insurance, Inc. Artificial Intelligence System automation.
    Consumes traffic data work items.
    """
    # Load JSON data from the file
    with open(r'C:\Users\acer\Desktop\Internship\AutomationLevel-III\output\work-items-out\workitems.json', 'r') as file:
        workitems_data = json.load(file)
    
    # Iterate over work items
    for index, item in enumerate(workitems_data):
        if 'payload' in item:
            traffic_data = item['payload'].get('traffic_data')
            if traffic_data and len(traffic_data.get('country', '')) == 3:
                status, return_json = post_traffic_data_to_sales_system(traffic_data)
                if status == 200:
                    print(f"Work item {index} processed successfully.")
                    # Assuming you have a way to mark the item as done in your system
                else:
                    print(f"Failed to process work item {index}. Error: {return_json.get('message', '')}")
                    # Assuming you have a way to handle failed items in your system
            else:
                print(f"Invalid traffic data for work item {index}. Payload: {item['payload']}")
                # Assuming you have a way to handle invalid data in your system
        else:
            print(f"No payload data found for work item {index}.")
            # Assuming you have a way to handle missing payload data in your system

def post_traffic_data_to_sales_system(traffimc_data):
    url = "https://robocorp.com/inhuman-insurance-inc/sales-system-api"
    response = requests.post(url, json=traffic_data)
    return response.status_code, response.json()
