#!/bin/bash

rsync -avz --progress \
    -e "ssh -i /Users/xi/Downloads/6140.pem" \
    --exclude '.git' \
    --exclude '__pycache__' \
    --exclude '*.pyc' \
    --exclude 'checkpoints/' \
    --exclude 'logs/' \
    --exclude 'runs/' \
    ./ \
    ec2-user@ec2-54-202-71-108.us-west-2.compute.amazonaws.com:/home/ec2-user/project/Multilingual_Code_Switch_Prediction-ML/
