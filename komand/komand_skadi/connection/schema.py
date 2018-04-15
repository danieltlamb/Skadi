# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Remote host to connect to. Can be over-ridden in actions",
      "order": 4
    },
    "key": {
      "type": "string",
      "title": "Key",
      "displayType": "password",
      "description": "A base64 encoded SSH private key to use to authenticate to remote server. A newline is required after the beginning and before the end marker",
      "format": "password",
      "order": 3
    },
    "password": {
      "type": "string",
      "title": "Password",
      "displayType": "password",
      "description": "Password authentication or password to decrypt provided private key. Either this or SSH private key is required",
      "format": "password",
      "order": 2
    },
    "port": {
      "type": "integer",
      "title": "Port",
      "description": "Remote port to use",
      "default": 22,
      "order": 5
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "User to run command as",
      "order": 1
    }
  },
  "required": [
    "port",
    "username",
    "host"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)