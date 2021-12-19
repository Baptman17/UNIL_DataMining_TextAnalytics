from DecisionTree_without_dc import DecisionTreeThread_without_dc
from LogisticRegression_without_dc import LogisticRegressionThread_without_dc
from RandomForest_without_dc import RandomForestThread_without_dc
from kNN_without_dc import kNNThread_without_dc
from util import get_training_data
from LogisticRegression import LogisticRegressionThread
from kNN import kNNThread
from DecisionTree import DecisionTreeThread
from RandomForest import RandomForestThread
from MLP import MLPThread
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from mdutils.mdutils import MdUtils
import threading
from EvaluationMetrics import EvaluationMetrics
import time

class ReadmeGenerator:
    def __init__(self, lr0: EvaluationMetrics = EvaluationMetrics(0,0,0,0), knn0: EvaluationMetrics = EvaluationMetrics(0,0,0,0), dt0: EvaluationMetrics = EvaluationMetrics(0,0,0,0), rf0: EvaluationMetrics = EvaluationMetrics(0,0,0,0), lr: EvaluationMetrics = EvaluationMetrics(0,0,0,0), knn: EvaluationMetrics = EvaluationMetrics(0,0,0,0), dt: EvaluationMetrics = EvaluationMetrics(0,0,0,0), rf: EvaluationMetrics = EvaluationMetrics(0,0,0,0), mlp: EvaluationMetrics = EvaluationMetrics(0,0,0,0)):
        self.__lr0 = lr0
        self.__knn0 = knn0
        self.__dt0 = dt0
        self.__rf0 = rf0
        self.__lr = lr
        self.__knn = knn
        self.__dt = dt
        self.__rf = rf
        self.__mlp = mlp
        self.__mdFile = MdUtils(file_name="../README")

    def generate_redame(self):
        self.__mdFile.new_header(level=1, title="UNIL_DataMining_TextAnalytics")
        self.__mdFile.new_header(level=2, title="Result without Data Cleaning")
        data = ["/","Logistic regression", "kNN", "Decision Tree", "Random Forests"]
        data.extend(["Precision", self.__lr0.getPrecision(), self.__knn0.getPrecision(),self.__dt0.getPrecision(),self.__rf0.getPrecision()])
        data.extend(["Recall", self.__lr0.getRecall(),self.__knn0.getRecall(),self.__dt0.getRecall(),self.__rf0.getRecall()])
        data.extend(["F1-score", self.__lr0.getF1(),self.__knn0.getF1(),self.__dt0.getF1(),self.__rf0.getF1()])
        data.extend(["Accuracy", self.__lr0.getAccuracy(),self.__knn0.getAccuracy(),self.__dt0.getAccuracy(),self.__rf0.getAccuracy()])
        self.__mdFile.new_table(columns=5, rows=5, text=data)
        self.__mdFile.new_header(level=2, title="Result with Data Cleaning")
        data = ["/","Logistic regression", "kNN", "Decision Tree", "Random Forests", "MLP"]
        data.extend(["Precision", self.__lr.getPrecision(), self.__knn.getPrecision(),self.__dt.getPrecision(),self.__rf.getPrecision(),self.__mlp.getPrecision()])
        data.extend(["Recall", self.__lr.getRecall(),self.__knn.getRecall(),self.__dt.getRecall(),self.__rf.getRecall(),self.__mlp.getRecall()])
        data.extend(["F1-score", self.__lr.getF1(),self.__knn.getF1(),self.__dt.getF1(),self.__rf.getF1(),self.__mlp.getF1()])
        data.extend(["Accuracy", self.__lr.getAccuracy(),self.__knn.getAccuracy(),self.__dt.getAccuracy(),self.__rf.getAccuracy(),self.__mlp.getAccuracy()])
        self.__mdFile.new_table(columns=6, rows=5, text=data)
        
        self.__mdFile.create_md_file()


if __name__ == '__main__':

    #without data cleaning

    start_time = time.time()
    lrThread = LogisticRegressionThread_without_dc()
    lrThread.start()

    kNNThread2 = kNNThread_without_dc()
    kNNThread2.start()

    dtThread = DecisionTreeThread_without_dc()
    dtThread.start()

    rfThread = RandomForestThread_without_dc()
    rfThread.start()

    lr_metrics0 = lrThread.join()
    kNN_metrics0 = kNNThread2.join()
    dt_metrics0 = dtThread.join()
    rf_metrics0 = rfThread.join()

    print(f"[Main]\t:\tTotal execution time : {time.time() - start_time}")

    #with data cleaning

    start_time = time.time()
    lrThread = LogisticRegressionThread()
    lrThread.start()

    kNNThread2 = kNNThread()
    kNNThread2.start()

    dtThread = DecisionTreeThread()
    dtThread.start()

    rfThread = RandomForestThread()
    rfThread.start()

    # It takes about 6 hours to run the MLP classificator
    # Last metrics found were 0.4827, 0.4854, 0.4837 and 0.4854
    # mlpThread = MLPThread()
    # mlpThread.start()

    lr_metrics = lrThread.join()
    kNN_metrics = kNNThread2.join()
    dt_metrics = dtThread.join()
    rf_metrics = rfThread.join()
    # mlp_metrics = mlpThread.join()
    mlp_metrics = EvaluationMetrics(0.4827, 0.4854, 0.4837, 0.4854)

    rg = ReadmeGenerator(lr_metrics0, kNN_metrics0, dt_metrics0, rf_metrics0, lr_metrics, kNN_metrics, dt_metrics, rf_metrics, mlp_metrics)
    rg.generate_redame()
    print(f"[Main]\t:\tTotal execution time : {time.time() - start_time}")



