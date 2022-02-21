FROM public.ecr.aws/lambda/python:3.8

#ARGS
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION

# Copy function code
COPY . ${LAMBDA_TASK_ROOT}/

# Install the function's dependencies using file requirements.txt
# from your project folder.

RUN echo $AWS_ACCESS_KEY_ID
RUN pip3 install awscli
COPY requirements.txt  .
#RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

#download latest pkl
#todo cambiar stage/production dependiendo de la rama
RUN aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
RUN aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
RUN aws configure set default.region $AWS_DEFAULT_REGION
RUN aws s3 cp s3://challenge-kueski/model/model_risk.joblib ${LAMBDA_TASK_ROOT}/model_risk.joblib
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function/app.handler" ] 
