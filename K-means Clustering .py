# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:12:41 2020

@author: Grant
"""

import random

training_data = [[0, 1, 0], [1, 1, 0], [2, 2, 0], [2, 1, 0], [1, 2, 0], [5, 5, 0], [5, 6, 0], [6, 6, 0], [6, 7, 0]]

number_of_clusters = 2

centres = []
for i in range(number_of_clusters):
    temp = []
    temp.append(random.randint(0, 10))
    temp.append(random.randint(0, 10))
    centres.append(temp)

print(centres)

n = 10
count = 0
while count < 10:
    for point in training_data:
        temp_centres = []
        for i in range(len(centres)):
            temp = []
            distance = ((centres[i][0] - point[0])**2 + (centres[i][1] - point[1])**2)**(1/2)
            temp.append(i)
            temp.append(distance)
            temp_centres.append(temp)
        temp_centres.sort(key=lambda x: x[1])
        #print(temp_centres)
        
        point[2] = temp_centres[0][0]
    
    for j in range(len(centres)):
        summation_x = 0
        count_x = 0
        summation_y = 0
        count_y = 0
        for k in training_data:
            if k[2] == j:
                summation_x += k[0]
                count_x += 1
                summation_y += k[1]
                count_y += 1
        centres[i][0] = summation_x / count_x
        centres[i][1] = summation_y / count_y
    
    print(training_data)
    count += 1
print(training_data)