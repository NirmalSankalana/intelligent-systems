import sys
class CSP:
    def __init__(self, variables, domains,constraint,rooms) -> None:
        self.variables= variables # variables to be constrained
        self.domains = domains # domain of each variable
        self.constraint=constraint # constraints
        self.rooms=rooms # constraints

    def consistent(self, variable:str, assignment)->bool:
        if(self.constraint[variable]=='c'):
            l=[i for i in assignment.keys() if assignment[i]['dateTime']==assignment[variable]['dateTime'] and self.constraint[i]=='c']
            if(len(l)!=1):
                return False
        s=[i for i in assignment.keys() if assignment[i]['dateTime']==assignment[variable]['dateTime']]
        if(len(s)>len(self.rooms)):
            return False
        else:
            assignment[variable]['room']=self.rooms[len(s)-1]
            return True

    def backtracking_search(self, assignment = {}):
        if len(assignment) == len(self.variables):
            return assignment
        unassigned= [v for v in self.variables if v not in assignment] 
        first: str = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first]={}
            local_assignment[first]['dateTime'] = value
            if self.consistent(first, local_assignment):
                result= self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None
    
if __name__=="__main__":
    import csv
    inputFileName=input('Enter the Input file name (with .csv): ')
    list=[]
    try:
        with open(inputFileName, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                list.append(row)
    except:
        print('Error in input file name')
        sys.exit()
    outputFileName=input('Enter the Onput file name (with .csv): ')
    rooms=' '.join(list.pop(-1)).strip().split(' ')      # rooms=['R1','R2','R3']
    variables=[i[0] for i in list]                          # variables:List[str]=['sub1', 'sub2','sub3', 'sub4']
    domains={i[0]:' '.join(i[2:]).strip().split(' ') for i in list}  # domains={'sub1':['M1', 'M2', 'T2','T3'],'sub2':['M1', 'M2', 'T2','T3'],'sub3':['M1', 'M2', 'T2','T3'],'sub4':['M1', 'M2', 'T2','T3']
    cons={i[0]:i[1] for i in list}                          # cons:Dict[str,str]={'sub1':'c', 'sub2':'o','sub3':'c', 'sub4':'o'}
    csp=CSP(variables,domains,cons,rooms)
    schedule=csp.backtracking_search()
    if schedule is not None:
        output=[[i,schedule[i]['dateTime'],schedule[i]['room']] for i in schedule.keys()]
        print(output)
    else:
        output=[['No Solution Found!']]
        print('No Solution Found!')
    with open(outputFileName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output)
