from json import dumps
class ReturnData:
    def __init__(self, downJson:dict = dict(), formattedJson:str = ""):
        self.downJson = downJson
        self.formattedJson = formattedJson

def downDataFormatter(
    downStatus
):
    downJson = {
        "downStatus": f"{downStatus}"
    }
    # format the data using json formatter
    formattedJson = dumps(downJson, indent=4)
    # save the down datas in to a file
    # return the formatted down ips data
    return ReturnData(downJson, formattedJson)
