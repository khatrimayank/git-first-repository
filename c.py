w=12345 





def min_coin(coin,w):

    arr=[[0 for j in range(w+1)] for i in range(len(coin)+1)]
    
    for i in range(len(coin)+1):

        for j in range(w+1):

            if i==0:
                arr[i][j]=j
            
            elif coin[i-1]>j:
                
                arr[i][j]=arr[i-1][j]

            else:
                
                arr[i][j]=min(arr[i-1][j],1+arr[i][j-coin[i-1]])

    print(arr[len(coin)][w])

    


min_coin(coin,w)

    sd;'sd;d'