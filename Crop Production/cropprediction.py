from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

mywindow = Tk()
mywindow.geometry("650x450")
mywindow.title("Crop Prediction - Python + Tkinter")
mywindow.resizable(False, False)
mywindow.config(background="#213141")

# Read the dataset
df = pd.read_csv('D:/Mayank/Project/APY.csv')

# Get unique crop names
crop_names = df['Crop'].unique()

main_title = Label(text="Crop Prediction", font=("Cambria", 14), bg="#56CD63", fg="black", width="500", height="2")
main_title.pack()


def send_data():
    import pandas as pd
    df=pd.read_csv('D:\Mayank\Project/APY.csv')
    print(df.head())

    #cleaning data
    crop_data=pd.get_dummies(data=df)
    print(crop_data.head())

    #rem null values
    print(crop_data.isnull().sum())
    crop_data.dropna(inplace=True)
    print(crop_data.isnull().sum())

    #prediction
    X=crop_data.drop(['Production'],axis=1)
    Y=crop_data['Production']

    from sklearn.model_selection import train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

    from sklearn.linear_model import LinearRegression
    mdl=LinearRegression()
    mdl.fit(X_train,Y_train)
    pred=mdl.predict(X_train)
    print(mdl.score(X_test,Y_test))
    print("")
    x= mdl.score(X_test,Y_test)

    
username_label = Label(text = "Show Prediction", bg = "#FFEEDD",width = "30", height = "2")
username_label.place(x = 220, y = 70)


submit_btn1 = Button(mywindow,text = "Predict", width = "20", height = "1", command =send_data, bg = "#00CD63")
submit_btn1.place(x = 250, y = 120)




def crop_prod1():
    crop_name = crop_var.get()
    dframe = df[df['Crop'] == crop_name]

    top_5states = dframe.groupby('State').sum()['Production'].nlargest()

    new_window = Toplevel(mywindow)
    new_window.geometry('580x400')
    new_window.title(f'Statewise Crop Production for {crop_name}')

    output_text = Text(new_window)
    output_text.pack()

    class PrintToTXT(object):
        def write(self, s):
            output_text.insert(END, s)

    sys.stdout = PrintToTXT()

    print('Top 5 states to get production are:')
    print(top_5states)

    plt.figure(figsize=(8, 4), dpi=100)
    sns.barplot(data=dframe, x='Production', y='State')
    plt.title(f'Statewise Crop Production for {crop_name}')
    plt.show()




crop_label = Label(mywindow, text="Select Crop", bg="#FFEEDD", width="30", height="2")
crop_label.place(x=50, y=300)

crop_var = StringVar(mywindow)
crop_dropdown = OptionMenu(mywindow, crop_var, *crop_names)
crop_dropdown.place(x=300, y=300)



submit_btn1 = Button(mywindow, text="Predict", width="20", height="1", command=send_data, bg="#00CD63")
submit_btn1.place(x=250, y=120)

submit_btn2 = Button(mywindow, text="Statewise Crop Production", width="30", height="2", command=crop_prod1,
                     bg="#00CD63")
submit_btn2.place(x=220, y=350)

mywindow.mainloop()
