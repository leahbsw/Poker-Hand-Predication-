import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl

def show_hands(cards, hand):
    mpl.rcParams['font.family'] = 'Times New Roman'
    
    ordinal = ['hearts', 'spades', 'diamonds', 'clubs']
    numerical = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    
    title = ['Nothing in hand', 'One pair', 'Two pairs', 'Three of a kind','Straight', 'Flush', 
             'Full house', 'Four of a kind', 'Straight flush', 'Royal flush']
    
    number_of_cards = int(len(list(cards))/2) 
    
    pic_names = []
    for i in range(number_of_cards):
        pic_names.append('Cards_pics/{}_of_{}.png'.format(numerical[cards[2*i+1]-1], ordinal[cards[2*i]-1]))
        
    # create figure
    fig = plt.figure(figsize=(20, 5))
    plt.suptitle(title[hand], fontsize=25)

    # setting values to rows and column variables
    rows = 1
    columns = 5
    
    for i in range(number_of_cards):

        # reading images
        Image = cv2.imread(pic_names[i])
        # Adds a subplot at the 1st position
        fig.add_subplot(rows, columns, i+1)

        # showing image
        plt.imshow(Image[...,::-1])
        plt.axis('off')
#         plt.title("First")

    plt.show()