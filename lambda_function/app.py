import json
from joblib import load

def handler(event, context):
	print("Event:")
	print(event)

	print("Context:")
	print(context)

	if 'detail-type' in event:
		if event['detail-type'] == "Scheduled Event":
			print("WarmUp - Lambda Model is warm!")
			return {}

	if type(event['body']) is str:
		data = json.loads(event['body'])
	else:
		data = event['body']
	
	#to-do: validate, features, data enchr
	my_model = load('model_risk.joblib') 
	inference = my_model.predict([data])

	if 'aws_request_id' in context:
		request_id = context.aws_request_id
	else:
		request_id = 'default'

	result = {
		'request_id': request_id,
		'customer_id': inference,
	}

	#response
	response = {
	"StatusCode": 200,
		"body": json.dumps(result)
	}
	
	return response