import random
import stddraw
from color import Color

# BUBBLE SORT
def bubble_sort(numbers):
    #get the lenght of the array
    n = len(numbers)
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]

def bubble_sort_animated(numbers):
    # CONFIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    #get the lenght of the array
    n = len(numbers)
    
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            draw_bars(numbers, selected=(pair, pair + 1))
            #Draw the rectangules before swap
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]
                #Draw rectangules after swap
                draw_bars(numbers, selected=(pair, pair + 1))
                
    draw_bars(numbers)
    stddraw.show() 

# SELECTION SORT
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

def selection_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(min_idx, j))
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        
        #SWAP
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        draw_bars(numbers, selected=(i, min_idx))
        
    draw_bars(numbers)
    stddraw.show()

# INSERTION SORT
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        j = i
        
        while j > 0 and numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1

def insertion_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j - 1] > numbers[j]:
            draw_bars(numbers, selected=(j - 1, j))
            
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            draw_bars(numbers, selected=(j - 1, j))
            j -= 1
            
    draw_bars(numbers)
    stddraw.show()

# DRAW BARS FUNCTION
def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)
    
# MAIN EXECUTION
numbers = [random.randint(0,100) for x in range(10)]
print(f"Before sort: {numbers}")

# Descomentar la opción a ejecutar

# 1. Bubble Sort
#bubble_sort_animated(numbers)
# bubble_sort(numbers)

# 2. Selection Sort
#selection_sort_animated(numbers)
# selection_sort(numbers)

# 3. Insertion Sort
insertion_sort_animated(numbers)
# insertion_sort(numbers)

print(f"After sort: {numbers}")