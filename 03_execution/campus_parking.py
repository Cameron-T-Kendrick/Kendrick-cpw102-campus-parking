#use a named constant
#using 2.0 make its value a float auto
#we defined it at the top, it is now available to any function in program
COST_PER_HR = 2.0

def cal_est_parking_cost(hrs):
    est_cost = hrs * COST_PER_HR 
    return est_cost 

#define the main logic of my program
def main():
    
    #create variable to store user-entered parked time
    #a var is a name space in memory
    parked_hrs = float(input("How long are you parking / have parked?"))
    
    print(parked_hrs)

#call my main function and execute the logic of the program
main()

   