import matplotlib
import matplotlib.pyplot as plt
matplotlib. use ('TkAgg')

def bubblesort(theseq):
   n=len(theseq)
   for i in range(n-1):
    for j in range(n-1):
       if theseq[j]<theseq[j+1]:
          tmp=theseq[j+1]
          theseq[j]=theseq[j+1]
          theseq[j+1]=tmp

theseq=[10,30,40,20,80]
print("before sortng",theseq)
bubblesort(theseq)
print("after sorting",theseq)
    
x=list(range(1,1000))
plt.plot(x,[y*y for y in x])
plt.title("bubblesort-time complexity is 0(n/uoob2)")
plt. xlabel("Input")
plt.ylabel("Time")
plt.show()
