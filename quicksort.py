from pyscript import display
import asyncio

async def bubbleSort(A):
    F = len(A)
    for i in range(F):
        for j in range(0,F-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                display(A, target="quicksort-output", append=False)
                await asyncio.sleep(0.5)
    display(A, target="quicksort-output", append=False)

def main():
    list1 = [3,5,1,6,5,2,9,0,4,6,1,2,5,4,6]
    asyncio.ensure_future(bubbleSort(list1))
    
main()