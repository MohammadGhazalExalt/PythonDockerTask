from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import json
from flask import jsonify
from datetime import datetime
from functools import wraps
import os

db_name = 'system_data.db'
app = Flask(__name__)
#engine = create_engine('mysql+pymysql://root:root@192.168.205.7:33060/system_data', echo = True)
engine = create_engine(f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}', echo = True)
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_SERVER")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
Base = declarative_base()


db = SQLAlchemy(app)

def log_function(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		with open("logs.log",'a') as file:
			file.write(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] : Received ({request.method}) request on ({request.url})\n")
			file.write(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] : Calling function {fn.__name__} with request : {request.args}\n")
		return fn(*args, **kwargs)
	return wrapper

class Disk_stats(Base):
    __tablename__ = 'disk_stats'
    used = Column(Integer)
    free = Column(Integer)
    timestamp = Column(String(50), unique=True, primary_key=True)

    def __init__(self, used, free, timestamp):
    	self.used = used
    	self.free = free
    	self.timestamp = timestamp
    def __repr__(self):
        return f'<used: {self.used} | free: {self.free} at {self.timestamp}>'

    def to_json(self):
    	return "{{\"used\": {0}, \"free\": {1}, \"timestamp\": \"{2}\"}}".format(self.used, self.free, self.timestamp)

class Mem_stats(Base):
    __tablename__ = 'mem_stats'
    used = Column(Integer)
    free = Column(Integer)
    timestamp = Column(String(50), unique=True, primary_key=True)

    def __init__(self, used, free, timestamp):
    	self.used = used
    	self.free = free
    	self.timestamp = timestamp
    def __repr__(self):
        return f'<used: {self.used} | free: {self.free} at {self.timestamp}>'

    def to_json(self):
    	return "{{\"used\": {0}, \"free\": {1}, \"timestamp\": \"{2}\"}}".format(self.used, self.free, self.timestamp)

class Cpu_stats(Base):
    __tablename__ = 'cpu_stats'
    idle = Column(Float)
    timestamp = Column(String(50), unique=True, primary_key=True)
    
    def __init__(self, idle, timestamp):
    	self.idle = idle
    	self.timestamp = timestamp
    def __repr__(self):
        return f'<idle: {self.idle} at {self.timestamp}>'        
    
    def to_json(self):
    	return "{{\"idle\": {0}, \"timestamp\": \"{1}\"}}".format(self.idle, self.timestamp)


@app.route("/cpu" , methods=['GET'])
@log_function
def read_cpu_stats():
	if 'past' in request.args and request.args.get('past'):
		Session = sessionmaker(bind = engine)
		session = Session()
		l = session.query(Cpu_stats).order_by(Cpu_stats.timestamp.desc()).limit(24).all()
		if l:
			result = [json.loads(item.to_json()) for item in l]
			return jsonify({'Cpu_stats': result})
		return jsonify({'Cpu_stats': ""})
	Session = sessionmaker(bind = engine)
	session = Session()
	result = session.query(Cpu_stats).order_by(Cpu_stats.timestamp.desc()).first()
	if result:
		result = json.loads(result.to_json())
		return jsonify({'Cpu_stats': result})
	return jsonify({'Cpu_stats': ""})


@app.route("/disk" , methods=['GET'])
@log_function
def read_disk_stats():
	if 'past' in request.args and request.args.get('past'):
		Session = sessionmaker(bind = engine)
		session = Session()
		l = session.query(Disk_stats).order_by(Disk_stats.timestamp.desc()).limit(24).all()
		if l:
			result = [json.loads(item.to_json()) for item in l]
			return jsonify({'Disk_stats': result})
		return jsonify({'Disk_stats': ""})
	Session = sessionmaker(bind = engine)
	session = Session()
	result = session.query(Disk_stats).order_by(Disk_stats.timestamp.desc()).first()
	if result:
		result = json.loads(result.to_json())
		return jsonify({'Disk_stats': result})
	return jsonify({'Disk_stats': ""})

@app.route("/memory" , methods=['GET'])
@log_function
def read_mem_stats():
	if 'past' in request.args and request.args.get('past'):
		Session = sessionmaker(bind = engine)
		session = Session()
		l = session.query(Mem_stats).order_by(Mem_stats.timestamp.desc()).limit(24).all()
		if l:
			result = [json.loads(item.to_json()) for item in l]
			return jsonify({'Mem_stats': result})
		return jsonify({'Mem_stats': ""})
	Session = sessionmaker(bind = engine)
	session = Session()
	result = session.query(Mem_stats).order_by(Mem_stats.timestamp.desc()).first()
	if result:
		result = json.loads(result.to_json())
		return jsonify({'Mem_stats': result})
	return jsonify({'Mem_stats': ""})


if __name__ == "__main__":
	app.run(host='0.0.0.0')
