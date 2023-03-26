import tkinter as tk
import pandas as pd
import random
import numpy as np

class GraphApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up main window
        self.title("Graph App")

        # Set up variables
        self.mode = tk.StringVar()
        self.mode.set("Normal")
        self.graph1_value = tk.StringVar()
        self.graph2_value = tk.StringVar()
        self.graph3_value = tk.StringVar()
        self.graph4_value = tk.StringVar()

        # Set up widgets
        self.time_step = tk.Label(self,text="Time step 0")
        self.step = 0

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.mode_label = tk.Label(self, text="Mode:")
        self.mode_radio_normal = tk.Radiobutton(self, text="Normal", variable=self.mode, value="Normal", command=self.update_mode)
        self.mode_radio_warning = tk.Radiobutton(self, text="Warning", variable=self.mode, value="Warning", command=self.update_mode)
        self.graph1_label = tk.Label(self, text="Graph Y1")
        self.graph2_label = tk.Label(self, text="Graph Y2")
        self.graph3_label = tk.Label(self, text="Graph Y3")
        self.graph4_label = tk.Label(self, text="Graph Y4")
        self.graph1_canvas = tk.Canvas(self, width=500, height=200, bg="white")
        self.graph2_canvas = tk.Canvas(self, width=500, height=200, bg="white")
        self.graph3_canvas = tk.Canvas(self, width=500, height=200, bg="white")
        self.graph4_canvas = tk.Canvas(self, width=500, height=200, bg="white")
        self.graph1_value_label = tk.Label(self, textvariable=self.graph1_value)
        self.graph2_value_label = tk.Label(self, textvariable=self.graph2_value)
        self.graph3_value_label = tk.Label(self, textvariable=self.graph3_value)
        self.graph4_value_label = tk.Label(self, textvariable=self.graph4_value)

        #Main Data (tracking of Y1, Y2, Y3,Y4 values)
        self.Y1 = tk.Label(self, text="Y1 current value :")
        self.Y2 = tk.Label(self, text="Y2 current value :")
        self.Y3 = tk.Label(self, text="Y3 current value :")
        self.Y4 = tk.Label(self, text="Y4 current value :")

        self.type_of_situation = tk.Label(self, text="Type of situation")
        self.description_of_situation = tk.Label(self, text="Description of situation")
        self.level_of_danger = tk.Label(self, text="Level of danger")
        self.level = tk.Label(self, text="Type of situation")

        # Set up layout
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        self.mode_label.grid(row=1, column=0, padx=10, pady=10)
        self.mode_radio_normal.grid(row=1, column=1, padx=10, pady=10)
        self.mode_radio_warning.grid(row=1, column=2, padx=10, pady=10)
        self.time_step.grid(row=2,column=0, padx=10, pady=10)

        self.graph1_label.grid(row=3, column=2, padx=10, pady=10)
        self.graph1_canvas.grid(row=4, column=2, padx=10, pady=10)
        self.graph1_value_label.grid(row=5, column=2, padx=10, pady=10)

        self.graph2_label.grid(row=3, column=3, padx=10, pady=10)
        self.graph2_canvas.grid(row=4, column=3, padx=10, pady=10)
        self.graph2_value_label.grid(row=5, column=3, padx=10, pady=10)

        self.graph3_label.grid(row=6, column=2, padx=10, pady=10)
        self.graph3_canvas.grid(row=7, column=2, padx=10, pady=10)
        self.graph3_value_label.grid(row=8, column=2, padx=10, pady=10)

        self.graph4_label.grid(row=6, column=3, padx=10, pady=10)
        self.graph4_canvas.grid(row=7, column=3, padx=10, pady=10)
        self.graph4_value_label.grid(row=8, column=3, padx=10, pady=10)

        self.type_of_situation.grid(row=3, column=0, padx=10, pady=10)        
        self.description_of_situation.grid(row=4, column=0, padx=10, pady=10)        
        self.level_of_danger.grid(row=5, column=0, padx=10, pady=10)        
        self.level.grid(row=6, column=0, padx=10, pady=10)   
        self.Y1.grid(row=3, column=1, padx=10, pady=10)
        self.Y2.grid(row=4, column=1, padx=10, pady=10)
        self.Y3.grid(row=5, column=1, padx=10, pady=10)
        self.Y4.grid(row=6, column=1, padx=10, pady=10)

    def update_mode(self):
        pass

    # Additive/multiplicative methond of prediciton
    def predict(self):
        pass

    def predict_random(self):
        noise = np.random.uniform(-0.1, 0.1, size=(len(self.Func), 5))
        self.Func_predicted = self.Func + self.Func * noise


    def reset_ui(self):
        self.time_step = tk.Label(self,text="Time step 0")
        self.step = 0
        self.Y1 = tk.Label(self, text="Y1 current value :")
        self.Y2 = tk.Label(self, text="Y2 current value :")
        self.Y3 = tk.Label(self, text="Y3 current value :")
        self.Y4 = tk.Label(self, text="Y4 current value :")
        self.Y1.grid(row=3, column=1, padx=10, pady=10)
        self.Y2.grid(row=4, column=1, padx=10, pady=10)
        self.Y3.grid(row=5, column=1, padx=10, pady=10)
        self.Y4.grid(row=6, column=1, padx=10, pady=10)
        
        self.time_step.grid(row=2,column=0, padx=10, pady=10)
    def start(self):
        self.reset_ui()
        
        if self.mode.get() == 'Warning':
            self.F1 = pd.read_csv('./Final_Pump_Warn/argF1_Warn.txt',header=None,sep='  ')
            self.F2 = pd.read_csv('./Final_Pump_Warn/argF2_Warn.txt',header=None,sep='  ')
            self.F3 = pd.read_csv('./Final_Pump_Warn/argF3_Warn.txt',header=None,sep='  ')
            self.F4 = pd.read_csv('./Final_Pump_Warn/argF4_Warn.txt',header=None,sep='  ')
            self.Func = pd.read_csv('./Final_Pump_Warn/Func_Warn.txt',header=None,sep='  ')
        
        elif self.mode.get() == 'Normal':
            self.F1 = pd.read_csv('./Final_Pump_Norm/argF1_Norm.txt',header=None,sep='  ')
            self.F2 = pd.read_csv('./Final_Pump_Norm/argF2_Norm.txt',header=None,sep='  ')
            self.F3 = pd.read_csv('./Final_Pump_Norm/argF3_Norm.txt',header=None,sep='  ')
            self.F4 = pd.read_csv('./Final_Pump_Norm/argF4_Norm.txt',header=None,sep='  ')
            self.Func = pd.read_csv('./Final_Pump_Norm/Func_Norm.txt',header=None,sep='  ')
        self.predict_random()

        # Set up initial values for graphs
        self.graph1_values = self.Func.iloc[0:1, 1].tolist()
        self.graph2_values = self.Func.iloc[0:1, 2].tolist()
        self.graph3_values = self.Func.iloc[0:1, 3].tolist()
        self.graph4_values = self.Func.iloc[0:1, 4].tolist()
        self.graph1_x = [0]
        self.graph2_x = [0]
        self.graph3_x = [0]
        self.graph4_x = [0]

        self.graph1_values_pred = self.Func_predicted.iloc[0:1, 1].tolist()
        self.graph2_values_pred = self.Func_predicted.iloc[0:1, 2].tolist()
        self.graph3_values_pred = self.Func_predicted.iloc[0:1, 3].tolist()
        self.graph4_values_pred = self.Func_predicted.iloc[0:1, 4].tolist()
        # Draw initial graphs
        self.draw_graph(self.graph1_canvas, self.graph1_x, self.graph1_values,self.graph1_values_pred,self.Y1)
        self.draw_graph(self.graph2_canvas, self.graph2_x, self.graph2_values,self.graph2_values_pred,self.Y2)
        self.draw_graph(self.graph3_canvas, self.graph3_x, self.graph3_values,self.graph3_values_pred,self.Y3)
        self.draw_graph(self.graph4_canvas, self.graph4_x, self.graph4_values,self.graph4_values_pred,self.Y4)

        # Schedule function to update graphs every 200 miliseconds 
        self.after(200, self.update_graphs, 1)

    def update_graphs(self, index):
        self.step += 1
        self.time_step.config( text = f' Time step = {self.step}')

        
        # Get next row of data
        row = self.Func.iloc[index:index+1]
        row_pred = self.Func_predicted.iloc[index:index+1]

        # Append new values to graph data
        self.graph1_x.append(self.graph1_x[-1] + 1)
        self.graph2_x.append(self.graph2_x[-1] + 1)
        self.graph3_x.append(self.graph3_x[-1] + 1)
        self.graph4_x.append(self.graph4_x[-1] + 1)
        self.graph1_values.append(row.iloc[0, 1])
        self.graph2_values.append(row.iloc[0, 2])
        self.graph3_values.append(row.iloc[0, 3])
        self.graph4_values.append(row.iloc[0, 4])

        self.graph1_values_pred.append(row_pred.iloc[0, 1])
        self.graph2_values_pred.append(row_pred.iloc[0, 2])
        self.graph3_values_pred.append(row_pred.iloc[0, 3])
        self.graph4_values_pred.append(row_pred.iloc[0, 4])

        # Redraw graphs
        self.draw_graph(self.graph1_canvas, self.graph1_x, self.graph1_values,self.graph1_values_pred,self.Y1)
        self.draw_graph(self.graph2_canvas, self.graph2_x, self.graph2_values,self.graph2_values_pred,self.Y2)
        self.draw_graph(self.graph3_canvas, self.graph3_x, self.graph3_values,self.graph3_values_pred,self.Y3)
        self.draw_graph(self.graph4_canvas, self.graph4_x, self.graph4_values,self.graph4_values_pred,self.Y4)

        # Schedule function to update graphs again in one second
        if (index + 1) % len(self.Func) != 0:
            self.after(200, self.update_graphs, (index + 1) % len(self.Func))

    def draw_graph(self, canvas, x_data, y_data,y_data_pred,Y_text):
        # Clear canvas
        canvas.delete("all")

        # Define the coordinates of the X-axis line
        x1, y1 = 0, canvas.winfo_height()
        x2, y2 = canvas.winfo_width(), canvas.winfo_height()

        # Draw the X-axis line
        canvas.create_line(x1, y1, x2, y2, fill='red',width=4)
        ticks_range = 30
        ticks = x2//ticks_range
        # Draw the tick marks and labels
        for i in range(1, ticks):
            x = x1 + i * ticks_range
            canvas.create_line(x, y1, x, y1 - 5)
            canvas.create_text(x, y1 - 10, text=str(i * ticks_range), fill="black", font=("Arial", 5))
            

        # Draw y-axis
        # canvas.create_line(50,
        print(len(y_data)==len(y_data_pred))


        # Draw initial values
        prev_x_point, prev_y_point = 0,y2
        for x_point,y_point in zip(x_data,y_data):
            y_point = y2 - y_point
            canvas.create_line(prev_x_point,prev_y_point,x_point,y_point,fill="green", width=2)
            prev_x_point = x_point
            prev_y_point = y_point
        #Draw predicted values
        
        prev_x_point, prev_y_point = 0,y2
        for x_point,y_point in zip(x_data,y_data_pred):
            y_point = y2 - y_point
            canvas.create_line(prev_x_point,prev_y_point,x_point,y_point,fill="yellow", width=2)
            prev_x_point = x_point
            prev_y_point = y_point
        text = Y_text['text'].split(':')[0]
        Y_text.config(text=f'{text}: {np.round(y_data_pred[-1],3)}')
if __name__ == "__main__":
    app = GraphApp()
    app.mainloop()
