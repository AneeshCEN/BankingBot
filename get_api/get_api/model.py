'''
Created on Mar 31, 2017

@author: aneesh.c
'''
# import aiml
# import dill
# from .models import RequestCache
# from get_api.models import UserCache
# from externel_api import call_api
# brain_file_medical = "C:/Users/ANEESH/workspace/get_api/get_api/bankbot.brn"
# 
# 
# def create_cache(CACHE_ID):
#     import base64
#     try:
#         req_cache = RequestCache.objects.get(cache_id=CACHE_ID)
#     except RequestCache.DoesNotExist:
#         kern_medical = aiml.Kernel()
#         kern_medical.bootstrap(brainFile=brain_file_medical)
#         kernel_str = dill.dumps(kern_medical)
#         kernel_str = base64.b64encode(kernel_str)
#         req_cache = RequestCache.objects.create(cache_id=CACHE_ID, cache=[],
#                                                 user=UserCache.objects
#                                                 .create(aiml_kernel=kernel_str)
#                                                 )
#     return req_cache




# def generate_reply(question, kernel, cache_list):
#     response = question
#     kernel_reply = kernel.respond(str(question['messageText']))
#     print kernel_reply
#     if "Sorry, I didn't get you.." in kernel_reply:
#         response = call_api(question)
#         return response
#     else:
#         response['entities'] = []
#         response['messageText'] = []
#         response['messageText'].append(kernel_reply)
#         return response
    