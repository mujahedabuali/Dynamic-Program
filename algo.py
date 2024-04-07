#Class for enter data into algortihms
def LED_Lighting(order):
    
        order_length=len(order)

        v = [1 for i in range(order_length)]
       
       # longest incressing subsequense o(n2)
        str=""
        for i in range(1,order_length):
            for j in range(0,i):
                    if order[i] > order[j] and v[i] < v[j] + 1:
                       v[i] = v[j] + 1
            str+=f"{v}"
            str+="\n"                   
                                   
        maxLeng = max(v)

        result = []
        index = v.index(maxLeng)

        result.append(order[index])
        for i in range(index - 1, -1, -1):
           
            if order[i] < order[index] and v[i] == v[index] - 1:
              result.insert(0, order[i])
              print(result)
              index = i

        return result, maxLeng,str
