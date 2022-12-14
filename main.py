# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:28:32 2022

@author: gandh
"""

import pandas as pd
import matplotlib.pyplot as plt

"""
Created function that reads a file.
This function returns converted data to dataframe and transposed dataframe data
"""
def readFileData(file):
    fileData = pd.read_csv(file);
    transposedFileData = pd.read_csv(file, header=None, index_col=0).T
    transposedFileData = transposedFileData.rename(columns={"Country Name":"Year"})
    transposedFileData = transposedFileData.fillna(0.0)
    return fileData, transposedFileData

"""
plotting bar graph using pandas library
"""
def barGraph_df(transposedFileData, Year, label):
    Countries = ["China", "India", "Canada", "United Kingdom", "United States"]
    #Year = ["2010","2010", "2011", "2012", "2013", "2014", "2015"]
    transposedFileData.update({"Year" : Year})
    transposedFileData.plot.bar(x="Year", y=["United States", "China", "India", "Canada", "United Kingdom"])
    plt.ylabel(label)
    plt.legend(Countries)
    plt.savefig("Bar graph")

"""
calculating world data
"""
def totalWorldData(df, year, li):
    for i in year:
        li.append(df[i].sum())
    return li

"""
plotting line graph for world
"""
def lineGraph(year, li, label):
    plt.figure()
    plt.plot(year,li)
    #plt.legend()
    plt.xlabel("Year")
    plt.ylabel(label)
    plt.show()



    
populationDf, transposedPopDf = readFileData("population.csv")
Co2EmiDf, transCo2EmiDf = readFileData("Co2Emittion.csv")
powerConDf, transPowerConDf = readFileData("powerConsumption.csv")
agriLandDf, transAgriLandDf = readFileData("AgricultureLand.csv")

year = ["2005", "2005", "2006", "2007", "2008", "2009", "2010"]

#plotting the bar graph
barGraph_df(transposedPopDf, year, "Population")
barGraph_df(transCo2EmiDf, year, "Co2Emittion")
barGraph_df(transPowerConDf, ["2005","2005","2006", "2007","2008", "2009","2010"], "PowerConsumption")
barGraph_df(transAgriLandDf, year, "Agriculture land")

populationLabel = "Total World Population Data"
powerConsumptionLabel = "Total world Power Consumption"
Co2EmittionLabel = "Total Co2 Emittion"

#calculating world values
population = totalWorldData(populationDf, year, ["Total World Population"])
powerConsumption = totalWorldData(powerConDf, year, ["Total World Power Consumption"])
co2Emittion = totalWorldData(Co2EmiDf, year, ["Total Co2 Emittion"])

#plotting the world line graph
lineGraph(year, population[1:], populationLabel)
lineGraph(year, powerConsumption[1:], powerConsumptionLabel)
lineGraph(year, co2Emittion[1:], Co2EmittionLabel)

