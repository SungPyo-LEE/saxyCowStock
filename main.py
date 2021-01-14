from getRawData import ExtractRawData

extractRawData = ExtractRawData.ExtractRawData()

print("Please input Flag --- 1: getRawData, 2: Analyze And Train Data, 3: Predict It!")
Flag = str(input())


if Flag=="1":
    extractRawData.getDrawData()
