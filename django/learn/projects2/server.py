#! /usr/bin/env python

#from docopt import docopt
from django.db import models
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
#from flask import render_template
#from flask.ext.restful import reqparse, abort, Api, Resource
#from reservation.model import reservation_connect
from InfoProjects.models import InfoProject
from InfoProjects.views import InfoProject_list, InfoProject_detail
#from reservation.generate import generate_from_string
#from reservation.plot import timeline_plot
from rest_framework.decorators import api_view, renderer_classes
from django.db import models

#import datetime
#import csv
#from flask_bootstrap import Bootstrap
#import json
#from flask import jsonify


#print json.dumps({'4': 5, '6': 7}, sort_keys=False,
#                  indent=4, separators=(',', ': '))

    
#app = Flask(__name__)   
#api = Api(app) 
#Bootstrap(app)
#app.debug = True


class RestDeleteAll(APIView):
    def get(self):
        Reservation().delete_all()
        resp = Response(list(), status=200, mimetype='text/html')
        return resp
    
class List(Resource):
    def get(self):
        data = Reservation.objects()
        resp = Response(list_table(data), status=200, mimetype='text/html')
        return resp
    
class Add(Resource):
    def get(self):
        resp = Response(render_template('add.html', order={}), status=200, mimetype='text/html')
        return resp

class AddSubmit(Resource):
    """submit a new a reservation
    """
    def post(self):
        reservations = Reservation(project=request.form["project"],
                                   cm_id=request.form["cm_id"],
                                   host=request.form["host"],
                                   end_time=request.form["end_time"],
                                   user=request.form["user"],
                                   start_time= request.form["start_time"],
                                   summary=request.form["summary"],
                                   label= request.form["label"])
        str = reservations.add()
        if str is not None:
            print str
            resp = Response(list_table(str), status=200, mimetype='text/html')
            return resp

        """list the reservations"""
        resp = Response(list(), status=200, mimetype='text/html')
        return resp
    
class AddSubmitFile(Resource):
    """add a reservation uploading a csv file

    :use a form to upload
    """
    def post(self):
        file = request.files["file"]
        reader = csv.reader(file)
        for row in reader:
            reservations = Reservation(cm_id=row[0],
                                       label=row[1],
                                       user=row[2],
                                       project=row[3],
                                       start_time=row[4],
                                       end_time=row[5],
                                       host=row[6],
                                       summary=row[7])
            reservations.add()

        """list the reservations"""
        resp = Response(list(), status=200, mimetype='text/html')
        return resp

api.add_resource(RestDeleteAll, '/delete/all')
api.add_resource(List, '/list')
api.add_resource(Add, '/add/')
api.add_resource(AddSubmit, '/add/submit')
api.add_resource(AddSubmitFile, '/add/file')

def main():
    db = reservation_connect()
    app.run()

@app.route('/')
def homepage():
    return 

@app.route('/chart')
def timeline():
    """printing the timeline from mongodb"""
    filename="static/time-plot"
    print "TIMELINE", filename
    timeline_plot(filename)
    return render_template('plot.html')

def list():
    data = InfoProjects.objects()
    return list_table(data)

def list_table(data):
    """this method renders the reservation data in a table
    :param data: The reservation data
    :type data: search result from Reservation
    """ 
    order = Reservation._order
    return render_template('list.html',
                            order=Reservation._order,
                            reservations=data)
    
def entry_table(data):
    """this method renders the reservation data in a table
    :param data: The reservation data
    :type data: search result from Reservation
    """
    try:
        entry = data[0]
    except:
        return error('can not find the specified object')
        
    order = Reservation._order
    return render_template('table.html',
                            order=Reservation._order,
                            reservation=data)

@app.route('/error/<msg>')
def error(msg):
    return render_template('error.html',
                            msg=msg)

    



@app.route("/list/user/<user>")
def list_user_reservations(user):        
    """find the reservations by user
    :param user: the username
    """
    data = Reservation().find_user(user)
    return list_table(data)

@app.route("/list/id/<id>")
def find_reservation_by_id(id):        
    """find the reservations by cm_id"""
    data = Reservation().find_id(id)
    return entry_table(data)

@app.route("/list/label/<label>")
def find_reservation_by_label(label):        
    """list the reservations by label"""
    data = Reservation().find_label(label)
    return entry_table(data)

'''@app.route("/delete/all")
def delete_all():        
    """delete all the reservations"""
    Reservation().delete_all()
    return list()'''

@app.route("/random")
def random_reservations():        
    """delete all the reservations"""
    generate_from_string("m[01-05] 10 10 now")
    return list()


# ######################################################################
# ALL METHODS BELOW THIS ARE POSSIBLY WRONG
# ######################################################################

@app.route("/list/", methods=['GET', 'POST'])
def list_fancy():
    """list the reservations

    as param it can get any of the arguments
    """
    reservations = Reservation()
    data = {}

    start_time ="1901-01-01"
    end_time = "2100-12-31"
    
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end")

        cm_id = request.args.get("cm_id")
        user = request.args.get("user")
        project = request.args.get("project")
        label = request.args.get("label")
        host=request.args.get("host")
        summary=request.args.get("summary")

        data = reservations.list(cm_id=cm_id,
                                user=user,
                                project=project,
                                label=label,
                                start_time=start_time,
                                end_time=end_time,
                                host=host,
                                summary=summary)
        
    return list_table(data)


@app.route("/duration/<id>")
def duration(id):
    """list the reservations by duration"""
    data = Reservation().duration(id)
    #print data 
    return render_template('list.html', order=str(data))


@app.route("/update/", methods=['GET', 'POST'])
def update_selection():        
    """delete all the reservations"""
    if request.method=='GET':
        fromObj = [request.args.keys()[0], request.args.values()[0]]
        toObj = [request.args.keys()[1], request.args.values()[1]]
    reservations = Reservation()
    reservations.update_selection(fromObj, toObj)
    data = reservations.all()
    order = reservations._order
    return render_template('list.html', order=order, reservation=data)

@app.route("/delete/", methods=['GET', 'POST'])
def delete_selection():
    """delete a reservation

    :param label: the label of the reservation
    """
    reservations = Reservation()
    start_time ="1901-01-01"
    end_time = "2100-12-31"
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end")
            
        reservations.delete_selection(cm_id=request.args.get("cm_id"),
                             user=request.args.get("user"),
                             project=request.args.get("project"),
                             label= request.args.get("label"),
                             start_time= start_time,
                             end_time=end_time,
                             host=request.args.get("host"),
                             summary=request.args.get("summary"))
        
    return list()

'''@app.route("/add/file", methods=['POST'])
def add_submitFile():
    """add a reservation uploading a csv file

    :use a form to upload
    """
    if request.method=='POST':
        file = request.files["file"]
        reader = csv.reader(file)
        for row in reader:
            reservations = Reservation(cm_id=row[0],
                                       label=row[1],
                                       user=row[2],
                                       project=row[3],
                                       start_time=row[4],
                                       end_time=row[5],
                                       host=row[6],
                                       summary=row[7])
            reservations.add()

    return list()'''

'''@app.route("/add/submit", methods=['POST'])
def add_submit():
    """submit a new a reservation
    """
    if request.method=='POST':
        reservations = Reservation(project=request.form["project"],
                                   cm_id=request.form["cm_id"],
                                   host=request.form["host"],
                                   end_time=request.form["end_time"],
                                   user=request.form["user"],
                                   start_time= request.form["start_time"],
                                   summary=request.form["summary"],
                                   label= request.form["label"])
        str = reservations.add()
        if str is not None:
            return render_template('list.html', order=str)

    """list the reservations"""
    return list()'''

'''@app.route("/add/")
def route_reservation_add():
    """add a reservation: use a form to get info from the user

    """
    return render_template('add.html', order={})'''

if __name__ == "__main__":
    main()

