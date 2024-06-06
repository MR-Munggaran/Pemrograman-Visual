import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def regression_plot(filename, xlabel, ylabel):
    df = pd.read_csv(filename)
    
    # Set the figure size for the plot
    plt.figure(figsize=(12, 6))
    
    # Use seaborn to create the regression plot
    sns.regplot(x=xlabel, y=ylabel, data=df)
    
    # Set the labels for the plot
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Show the plot
    plt.show()  # The parentheses are necessary to call the function

if __name__ == '__main__': 
    regression_plot('tempRainYearly.csv', 'temp', 'Rain')