from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import Connection
from models import Restaurant
from serializers import RestaurantSerializer

@csrf_exempt
@api_view(['GET','POST'])
def restaurants(request):
    #connect to our local mongodb
    db = Connection('localhost',27017)
    #get a connection to our database
    dbconn = db.restaurants
    restaurantCollection = dbconn['restaurants']

    if request.method == 'GET':
        #get our collection
        restaurants = []
        for r in restaurantCollection.find():
            restaurant = Restaurant(r["_id"],r["name"],r["address"])
            restaurants.append(restaurant)
        serializedList = RestaurantSerializer(restaurants, many=True)
        return Response(serializedList.data)
    elif request.method == 'POST':
        #get data from the request and insert the record
        name = request.POST["name"]
        address = request.POST["address"]
        try:
            restaurantCollection.insert({"name" : name, "address": address})
        except:
            return Response({ "ok": "false" })
        return Response({ "ok": "true" })

# Create your views here.
