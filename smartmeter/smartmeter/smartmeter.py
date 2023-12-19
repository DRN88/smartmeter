from .obisMap import *
import urllib.parse
import re

def parseDSMRMessage(meterResult):
    regexKeyValue = re.compile(r'^(.+)\((.+)\)$')       # 1-0:1.8.0(018456.016*kWh)
    regexValueWithUnit = re.compile(r'^(.+)\*(.+)$')    # 018456.016*kWh
    parsedData = {}
    for item in meterResult.text.splitlines():
        regexKeyValueResult = regexKeyValue.search(item)
        if regexKeyValueResult != None:
            obisCode = regexKeyValueResult.group(1)
            if obisCode in obisMap:
                obisName = obisMap[obisCode]
                rawValue = regexKeyValueResult.group(2)
                regexValueWithUnitResult = regexValueWithUnit.search(rawValue)
                value = rawValue
                unit = ''
                if regexValueWithUnitResult != None:
                    value = regexValueWithUnitResult.group(1) 
                    unit = regexValueWithUnitResult.group(2)
                # Integer
                if value.isnumeric():
                    parsedData[obisName] = {
                        'value': int(value),
                        'unit': unit
                    }
                # Float
                elif isFloat(value):
                    parsedData[obisName] = {
                        'value': float(value),
                        'unit': unit
                    }
                # String
                else:
                    parsedData[obisName] = {
                        'value': value,
                        'unit': unit
                    }
    return parsedData


def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def getTelegrafUrlWithData(uri:str, dataDict: dict):
    keyValueDict = {}
    for subkey, item in dataDict.items():
        keyValueDict[subkey] = str(item['value'])
    url = "{}?{}".format(uri, urllib.parse.urlencode(keyValueDict))
    return url
