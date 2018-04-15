# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class TimesketchCreateuserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "b64_password": {
      "type": "string",
      "title": "B64 Password",
      "description": "b64_password",
      "order": 2
    },
    "b64_username": {
      "type": "string",
      "title": "B64 Username",
      "description": "b64_username",
      "order": 1
    }
  },
  "required": [
    "b64_username",
    "b64_password"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TimesketchCreateuserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "type": "string",
      "title": "Results",
      "description": "Output results",
      "order": 1
    }
  },
  "required": [
    "results"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)