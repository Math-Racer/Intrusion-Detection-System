from pymongo import MongoClient
# MONGO_URI = "mongodb+srv://vijayragav71:0gy2gasqAmaeGWNt@cluster0.7rst8.mongodb.net/vehicle_orders?retryWrites=true&w=majority"
MONGO_URI = "mongodb://localhost:27017/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['IntrustionDataDetection']
log_activity = db['log_activity'] 

# db.log_activity.deleteMany({})