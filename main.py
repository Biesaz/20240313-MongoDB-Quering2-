# query = {"age":{"$ne":40,"$ne":57}}

#     response = collection.find(query,{})
#     for document in response:
#         print(document)

# ##########################################################
        
# query = {"age":{"$gte":40,"$lte":57}}

#     response = collection.find(query,{})
#     for document in response:
#         print(document)

# ##########################################################

# collection = get_database_collection(db, collection_name)
#     age = [40, 50, 57]
#     query = {"age":{"$nin":age}}

#     response = collection.find(query,{})
#     for document in response:
#         print(document)