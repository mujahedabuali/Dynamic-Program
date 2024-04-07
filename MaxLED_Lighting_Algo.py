#Class for enter data into algortihms
class MaxLED_Lighting :

    def __init__(self,n,order):
        self.n=list(range(1,n+1))
        self.order=order
        
        self.n_length =len(self.n)
        self.order_length=len(self.order)

        self.sched1 = [[0 for i in range(self.n_length+1)] for j in range(self.order_length+1)]
        self.sched2 = [["''" for i in range(self.n_length+1)] for j in range(self.order_length+1)]

        for i in range(1,  self.n_length):
            self.sched1[i][0] = 0

        for j in range(1, self.order_length):
            self.sched1[0][j] = 0

        # 2 loops to make shed1 and shed2 o(n^2)
        for i in range(1,self.n_length+1):
            for j in range(1,self.order_length+1):
                    if self.n[i-1] == self.order[j-1]:
                        self.sched1[i][j] = self.sched1[i - 1][j - 1] + 1
                        self.sched2[i][j] = 'A'
                    else:
                            if self.sched1[i-1][j] >= self.sched1[i][j-1]:
                                self.sched1[i][j] = self.sched1[i-1][j]
                                self.sched2[i][j] = 'U'
                            else:
                                self.sched1[i][j]=self.sched1[i][j-1]
                                self.sched2[i][j] = 'L'
            
    #get suggest solution o(1)
    def LEDs_Sugg(self,str1,i, j):
        if  i== 0 or j == 0:
            return str1

        if self.sched2[i][j] == 'A':
            x= (self.sched1[i].index(self.sched1[i][j]))
            str1 += str(f"{self.order[x-1]}")
            str1 += " "
            return self.LEDs_Sugg(str1, i - 1, j - 1)
         
        elif self.sched2[i][j] == 'U':
            return self.LEDs_Sugg(str1, i-1, j)

        else:
            return self.LEDs_Sugg(str1, i, j-1)
        
    #print method    
    def print_res(self):
        max=self.sched1[self.n_length][self.order_length] #get maximum number of leds
        
        #loop to get all suggest solution and put it in string "leds" o(n)
        leds=""
        last_row = self.sched1[-1]
        for i in range(len(last_row)-1, -1, -1):
            if last_row[i] == max:
                 x = str(f"'{self.LEDs_Sugg('',self.n_length,i)}'")
                 if x not in leds:
                     leds += x+", "
        if leds.endswith(", "): leds = leds[:-2]         

        #loop to get dp table by print sched1,sched2 in put it in string "dpTable" o(n*n)
        dpTable=""
        for i in self.sched1:
             dpTable += str("\n") 
             for j in i:
              dpTable += str(f"{j} ")    
        dpTable += str("\n") 
        for i in self.sched2[1:]:
             dpTable += str("\n") 
             for j in i[1:]:
              dpTable += str(f"{j} ")     

        return max,leds,dpTable            
            