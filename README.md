# Logging_System

Install filebeat, aws, and cdk
Clone the repo and cd into the direcotry


## Setup developer env
Go to the root of repo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt
pip install -r .\requirements-dev.txt

## AWS cdk
cdk synth
cdk bootstrap
cdk deploy

## Filebeat
In a new shell go to the root of repo
cd .\filebeat\
filebeat -e --path.config . --path.data . --path.home . --path.logs

