import pygame, random

class ArrayBars():

    def __init__(self, size, color, update_window):
        #The bars will be represented as an array of different ints
        self.size = size
        self.array = [{
            'barSize': i + 1,
            'barColor': 'red'
        } for i in range(size)]
        self.RED = color
        self.GREEN = "#454B1B"
        self.algorithm = ""
        self.update_window = update_window
      
        self.num_passes = 0
        self.num_comps = 0
        self.num_swaps = 0
  

    def draw(self, win):
        TALLEST_BAR = 220
        height_factor = TALLEST_BAR / self.size
        #Loop through elements in bar array
        for index, value in enumerate(self.array):
            barSize, barColor = value['barSize'], value['barColor']
            color = self.RED if barColor == 'red' else self.GREEN

            width, height = 450 / self.size, barSize * height_factor
            left, top = 25 + index * width, 400 - height - 20
            pygame.draw.rect(win, color,
                             pygame.Rect((left, top), (width, height)))


    def shuffle(self):
        random.shuffle(self.array)

    def set_size(self, num):
        #This will only make a new array if the size changes
        if self.size != num:
            self.size = num
            self.array = [{
                'barSize': i + 1,
                'barColor': 'red'
            } for i in range(num)]

    def bubble_sort(self):
        #Iterate over entire array
        for i in range(self.size):
            #Loop over the list again, last i elements have already been sorted
            self.num_passes += 1

            for j in range(0, self.size - i - 1):
                green_bar = 0
                self.num_comps += 1
                if self.array[j]['barSize'] > self.array[j + 1]['barSize']:
                    self.num_swaps += 1
                    self.array[j]['barSize'], self.array[
                        j + 1]['barSize'] = self.array[
                            j + 1]['barSize'], self.array[j]['barSize']
                    self.array[j + 1]['barColor'] = 'green'
                    green_bar = j + 1
                    self.update_window()

                self.array[green_bar]['barColor'] = 'red'

        print('Array sorted using bubble sort!')
        print('There were:')
        print(self.num_passes, 'passes')
        print(self.num_comps, 'comparisons')
        print(self.num_swaps, 'swaps')
              
    def insertion_sort(self):
        #Expand the top by one each iteration
        for top in range(1, len(self.array)):
            self.num_passes += 1
            topItem = self.array[top]['barSize']
            i = top
            while i > 0 and topItem < self.array[i - 1]['barSize']:
                self.num_comps += 1
                self.num_swaps += 1
                self.array[i]["barSize"] = self.array[i - 1]['barSize']
                i -= 1
                self.update_window()
            self.num_swaps += 1
            self.array[i]["barSize"] = topItem

        print('Array sorted using insertion sort!')
        print('There were:')
        print(self.num_passes, 'passes')
        print(self.num_comps, 'comparisons')
        print(self.num_swaps, 'swaps')

    def selection_sort(self):
        for i in range(len(self.array)):
            self.num_passes += 1
            pastMinIndex = i
            minIndex = i
            for j in range(i + 1, len(self.array)):
                self.num_comps += 1
                if self.array[minIndex]['barSize'] > self.array[j]['barSize']:
                    pastMinIndex = minIndex
                    minIndex = j
                    self.array[pastMinIndex]['barColor'] = 'red'
                    self.array[minIndex]['barColor'] = 'green'
                self.update_window()
            self.num_swaps += 1
            self.array[i], self.array[minIndex] = self.array[
                minIndex], self.array[i]
            self.array[i]['barColor'] = 'red'
        print('Array sorted using selection sort!')
        print('There were:')
        print(self.num_passes, 'passes')
        print(self.num_comps, 'comparisons')
        print(self.num_swaps, 'swaps')
    

    def sort(self):
        #Reset counters
        self.num_passes = 0
        self.num_comps = 0
        self.num_swaps = 0
      
        if self.algorithm == 'Bubble Sort':
            self.bubble_sort()
        if self.algorithm == 'Insertion Sort':
            self.insertion_sort()
        if self.algorithm == 'Selection Sort':
            self.selection_sort()
