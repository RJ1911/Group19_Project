# import pymongo
# import pandas as pd
# import json
# from dataclasses import dataclass 
# import os
# import streamlit as st
# st.write("DB username:", st.secrets["db_username"])

# FOR STREMALIT
# # class EnvironmentVariable:
# #     mongo_db_url:str = os.getenv("MONGO_DB_URL")

# # env_var = EnvironmentVariable()
# client = pymongo.MongoClient(st.secrets["MONGO_DB_URL"])
# # print ("connection established")

# FOR LOCALHOST

import pymongo
import pandas as pd
import json
from dataclasses import dataclass 
import os

class EnvironmentVariable:
    # mongo_db_url:str = os.getenv("MONGO_DB_URL")
    mongo_db_url:str = "mongodb://localhost:27017/"

env_var = EnvironmentVariable()
# Ensure the environment variable is loaded correctly
if env_var.mongo_db_url is None:
    print("MONGO_DB_URL environment variable is not set.")
else:
    # Establish MongoDB connection
    client = pymongo.MongoClient(env_var.mongo_db_url)
    print("Connection established.")
