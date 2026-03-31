from data_handling import Dataset

if __name__ == "__main__":
    dataset = Dataset()
    #úloha 1
    stats = dataset.calculate_statistics()
    print(stats)
    #úloha 2
    X_train, X_test, y_train, y_test = dataset.split_data()

    methods = ['standard', 'normalize', 'robust']

    for method in methods:
        X_train_scaled, X_test_scaled = dataset.scale_data(X_train, X_test, scale_type=method)

        dataset.visualize_feature_distribution(feature_index=0, scaled_data=X_train_scaled, title_suffix=f"({method})")

    #Úloha 3
    stats = dataset.summarize_features()
    print(stats)
    print()

    #Úloha 4
    stats = dataset.summarize_features(['mean radius', 'mean area', 'mean concave points'])
    print(stats)
    print()