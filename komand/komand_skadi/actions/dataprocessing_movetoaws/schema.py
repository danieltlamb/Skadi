# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class DataprocessingMovetoawsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bucket": {
      "type": "string",
      "title": "Bucket",
      "description": "Bucket in AWS",
      "order": 2
    },
    "prefix": {
      "type": "string",
      "title": "Prefix",
      "description": "Prefix",
      "order": 3
    },
    "source": {
      "type": "string",
      "title": "Source",
      "description": "Source",
      "order": 1
    }
  },
  "required": [
    "source",
    "bucket",
    "prefix"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DataprocessingMovetoawsOutput(komand.Output):
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