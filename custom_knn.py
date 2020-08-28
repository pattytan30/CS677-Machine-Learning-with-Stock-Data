import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

class Custom_knn:
    def __init__(self, k, p):
        # k is the number of neighbors 
        # p is the distance parameter
        self.k = k
        self.p = p
        
    def __str__(self):
        k = "The number of neighbors k value is" + str(self.k)
        p = "Distance parameter p is" + str(self.p)
        return k, p
    
    def fit(self, X, Labels):
        # import X train and Y train
        self.X = X
        self.Labels = Labels
        
    def predict(self, new_x):
        # import X test to predict Y
        y_predict = np.array([])
        for x_test in new_x:
            distances = np.array([])
            for x_train in self.X:
                distance = np.linalg.norm(x_test - x_train, ord=self.p)
                distances = np.append(distances, distance)
            k_sorted_distance_indice = np.argsort(distances)[:self.k]
            k_labels = [self.Labels[i] for i in k_sorted_distance_indice]
            pred_label = Counter(k_labels).most_common(1)[0][0] 
            y_predict = np.append(y_predict, pred_label)
        return y_predict
    
    def draw_decision_boundary(self, new_x):
        # import single new x and draw its neighbors
        distances = np.array([])
        for x_train in self.X:
            distance = np.linalg.norm(new_x - x_train, ord=self.p)
            distances = np.append(distances, distance)
        k_sorted_distance_indice = np.argsort(distances)[:self.k]
        x_trains = [self.X[i] for i in k_sorted_distance_indice]
        k_labels = [self.Labels[i] for i in k_sorted_distance_indice]
        pred_label = Counter(k_labels).most_common(1)[0][0]
        
        fig, ax = plt.subplots()
        ax.scatter(new_x[0], new_x[1], c=str(pred_label), s=70, marker='^')
        
        for i in range(self.k):
            ax.scatter(x_trains[i][0], x_trains[i][1], c=str(k_labels[i]), s=50)
            
        ax.set_xlabel("Mean Return")
        ax.set_ylabel("Volatility")
        ax.set_title("Decision Boundary")
        ax.grid(True)
        fig.tight_layout()
        plt.show()
    
