
import GWO as gwo
import csv
import numpy
import time
def selection(function_scenario,size_value,Iteration):
   # functiontion_name=function_scenario[0]
    l_b=function_scenario[0]
    u_b=function_scenario[1]
    dimension=function_scenario[2]
    x=gwo.GWO(l_b,u_b,dimension,size_value,Iteration)
    return x
def parameter(a):
    parameter = {0: [0, 1, 24]}
    return parameter.get(a,"noting")
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
Number_of_Run=1
# Select general parameters for all optimizers (population size, number of Iteration)
Population_Size = 7
Iteration= 7
#Export results ?
Export=True

#ExportToFile="YourResultsAreHere.csv"
#Automaticly generated name by date and time
ExportToFile="./result/experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv"

# Check if it works at least once
Flag=False

# CSV Header for for the cinvergence 
CnvgHeader=[]

for l in range(0,Iteration):
	CnvgHeader.append("Iteration"+str(l+1))

for k in range(0, Number_of_Run):
    function_scenario = parameter(0)
    x = selection(function_scenario, Population_Size, Iteration)
    if (Export == True):
        with open(ExportToFile, 'a', newline='\n') as out:
            writeration = csv.writeration(out, delimiteration=',')
            if (Flag == False):  # just one time to write the header of the CSV file
                header = numpy.concatenate(
                    [["Optimizer", "objfname", "startTime", "EndTime", "ExecutionTime"], CnvgHeader])
                writeration.writerationow(header)
            a = numpy.concatenate([[x.optimizer, x.objfname, x.startTime, x.endTime, x.executionTime], x.convergence])
            writeration.writerationow(a)
        out.close()
    Flag = True  # at least one experiment
if (Flag==False): # Faild to run at least one experiment
    print("No Optomizer or Cost functiontion is selected. Check lists of available optimizers and cost function") 
        
        
