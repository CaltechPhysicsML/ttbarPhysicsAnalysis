import numpy as np
import cPickle
import pydotplus
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_blobs

import chain_aggregate

def main():
    
    dt_features = ['numJets', 'maxjetpt', 'minjetpt', 'medium', 'numLeptons', 'maxlpt', 'MET', 'MT', 'HT', 'DPHI_metlep', 'DPHI_metjet', 'DR_lepjet']
    
    #dt_list = chain_aggregate.aggregate_main()
    
    output = open('output.txt', 'rb')
    dt_list = cPickle.load(output)
    
    
    dtlistlen = len(dt_list)
    
    
    print "Checking keys .........."
    
    for i in range(dtlistlen):
        curr_dict = dt_list[i]
        
        #print curr_dict.keys()
        
        tester = len(curr_dict['numJets'])
        
        print "test value: " + str(tester)
        
        for key in curr_dict:
            #print "key: " + str(key)
            
            if len(curr_dict[key]) != tester:
                print "ERROR // length of key: " + str(len(curr_dict[key]))
                
        
    print "Merging keys .........."
    
    # merge all dictionaries into 1
    main_dict = {k: v + dt_list[1][k] + dt_list[2][k] for k, v in dt_list[0].iteritems()}
    
    tester = len(main_dict['medium'])
    for key in main_dict:
        #print "key: " + str(key)
        
        if len(main_dict[key]) != tester:
            print "// ERROR // length of key: " + str(len(main_dict[key]))
    
    print main_dict.keys()
    
    
    print "Setting X and Y matrices .........."
    
    # set X and Y matrices
    X = np.array([main_dict.get(key) for key in dt_features])
    X = X.T
    
    Y = np.array([0] * len(dt_list[0]['numJets']) + [1] * len(dt_list[1]['numJets']) + [2] * len(dt_list[2]['numJets']))
    Y = Y.T
    
    
    
    #X, Y = make_blobs(n_samples = 10000, n_features=10, centers = 100, random_state = 0)
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)
    
    print "Training decision tree ..........."
        
    # do decision tree stuff now
    #clf = tree.DecisionTreeClassifier()
    #clf = RandomForestClassifier()
    clf = GradientBoostingClassifier()
    clf = clf.fit(x_train, y_train)
    
    preds = clf.predict(x_test)
    
    #scores = cross_val_score(clf, X, Y)
    #print scores.mean()
    
    #scores = score(clf, x_test, y_test)
    #print clf.score(x_test, y_test)
    print accuracy_score(preds, y_test) * 100
    
    #preds = clf.predict(X)
    #print "predicted: " + str(preds)
    
    #print "y_test: " + str(y_test)
    #print ""
    #print sum(i != 0 for i in preds)
    print float(sum(preds == y_test))/float(len(preds))  

    #data = tree.export_graphviz(clf, out_file = None)
    #print "1"
    #graph = pydotplus.graph_from_dot_data(data)
    #print "2"
    #graph.write_pdf("test.pdf")
    #print "3"

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
