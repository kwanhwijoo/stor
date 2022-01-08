#NCP hmac API
import sys
import os
import hashlib
import hmac
import base64
import requests
import time
# import numpy as np

print("Start")

def	make_signature():
	timestamp = int(time.time() * 1000)
	timestamp = str(timestamp)

	access_key = "{n4LWoVRUCp44rdv1iAFq}"				# access key id (from portal or Sub Account)
	secret_key = "{GljRIcuZ2zvIfNnbRN1taeigCOxmXyzGQKPl7WZ5}"				# secret key (from portal or Sub Account)
	secret_key = bytes(secret_key, 'UTF-8')

	method = "GET"
	uri = "/photos/puppy.jpg?query1=&query2"

# 	GET or POST
# https://billingapi.apigw.ntruss.com/billing/v1/



	message = method + " " + uri + "\n" + timestamp + "\n"+ access_key


    # print(message)
	# message = bytes(message, 'UTF-8')


	signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

	return signingKey

def	request(self):
	context = ssl._create_unverified_context()

	full_path = self.url + self.req_path
	print(">>"+full_path)
	req = urllib.request.Request(full_path)

	timestamp = self.get_timestamp()

	req.add_header('x-ncp' , timestamp)
	req.add_header('x-ncp' , timestamp)
	req.add_header('x-ncp' , timestamp)
	req.add_header('x-ncp' , timestamp)

	response = urllib.request.urlopen(req, context=context)
	retuirn response
