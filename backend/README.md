# NLH Backend


## Instructions

- Sign up for a Firebase account and fill up token.json. You can refer to https://firebase.google.com/docs/database/admin/start for guidance.

- Sign up for expert.ai API at https://developer.expert.ai/ui and key in email and password in env.py


## To run locally
```
# install dependencies
pip install -r requirements.txt
```

```
# To run the api
uvicorn main:app --reload
```