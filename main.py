import pandas
import numpy as np


def main():
    # Load dataset
    url = "data_heart.csv"
    pre_dataset = pandas.read_csv(url)
    dataset = to_nominal(pre_dataset)
    row_count = dataset.shape[0]
    split_point = int(row_count * 1 / 10)
    ap = float(row_count * 1 / 10)
    extraf = round((ap - split_point) * 10)
    train_data, test_data = [0] * 11, [0] * 11
    start_point = 0
    # Creating 10-fold
    for x in range(1, 11):
        print("Fold ", x, " Results")
        if x != 10:
            end_point = start_point + split_point
        else:
            end_point = start_point + split_point + extraf

        test_data[x] = dataset[start_point:end_point]
        train_data[x] = dataset[~dataset.apply(tuple, 1).isin(test_data[x].apply(tuple, 1))]

        start_point += split_point
        rules = make_rules(train_data[x])
        print(" Selected Rules ")
        for k in rules.keys():
            print(k, rules[k])
            all_ft = rules[k]["features"].split(",")
            all_ft = list(filter(None, all_ft))  # remove empty
            all_v = rules[k]["values"].split(",")
            all_v = list(filter(None, all_v))  # remove empty
            sl_class = rules[k]["class"]
            p = test_data[x].copy()
            for ft in all_ft:
                val = all_v[all_ft.index(ft)]
                p = p[(p[ft] == val)]
            p_total = p.count()[0]
            p_correct = p[p["num"] == sl_class].count()[0]
            p_wrong = p_total - p_correct
            if p_correct == 0 or p_total == 0:
                accuracy = 0
            else:
                accuracy = p_correct / p_total
            print("Test Accuracy : ", accuracy, ", Correctly predicted : ", p_correct, ", Wrong prediction : ", p_wrong)
        print("****************************************************************************")

# function to get unique values
def unique(list1):
    x = np.array(list1)
    return np.unique(x)


# function to convert to nominal values
def to_nominal(dataset):
    # select numeric columns
    features = dataset.select_dtypes(exclude=["object"])
    for ft in features:
        avg = dataset[ft].mean()
        dataset.loc[dataset[ft] >= avg, ft] = "high"
        dataset.loc[(dataset[ft] != "high"), ft] = "low"

    return dataset


def loop_data(data, features, cs, selected_features, selected_values):
    maxf = 0

    for f in features:
        values = unique(data.loc[:, f])
        for v in values:
            if selected_features:
                p = data[(data[f] == v) & (data["num"] == cs)]
                pall = data[(data[f] == v)]
                for slf in selected_features:
                    p = p[p[slf] == selected_values[selected_features.index(slf)]]
                    pall = pall[(pall[slf] == selected_values[selected_features.index(slf)])]
                pair = p.count()
                total_pair = pall.count()
            else:
                pair = data[(data[f] == v) & (data["num"] == cs)].count()
                total_pair = data[(data[f] == v)].count()

            if int(pair[0]) == 0 or int(total_pair[0]) == 0:
                accuracy = 0
            else:
                accuracy = int(pair[0]) / int(total_pair[0])
            if accuracy > maxf:
                maxf = accuracy
                s_feature = f
                s_value = v
                if maxf == 1:
                    if selected_features:
                        return maxf, s_feature, s_value, p
                    else:
                        return maxf, s_feature, s_value, ""

    if maxf == 0:
        s_feature = ""
        s_value = ""
    return maxf, s_feature, s_value, ""


def make_rules(main_data):
    num_cols = len(main_data.columns) - 1
    rclass = main_data.iloc[:, num_cols]
    classes = unique(rclass)
    rules = {}
    counter = 1
    for cs in classes:
        data = main_data.copy()
        selected_features = []
        selected_values = []
        features = list(main_data.columns)
        features.remove("num")
        while data[data["num"] == cs].count()[0] != 0:

            maxf, s_feature, s_value, p = loop_data(data, features, cs, selected_features, selected_values)

            if maxf != 0:
                selected_features.append(s_feature)
                selected_values.append(s_value)
                # print("feature is ", selected_features, " value is ", selected_values)
                if maxf == 1:
                    # each feature/value is separated by ,
                    rules[counter] = {}
                    total_ft, total_vl = "", ""
                    for sf in selected_features:
                        total_ft += str(sf) + ","
                    for sv in selected_values:
                        total_vl += str(sv) + ","
                    rules[counter]['features'] = total_ft
                    rules[counter]['values'] = total_vl
                    if isinstance(p, pandas.DataFrame):
                        rules[counter]['support'] = p.count()[0]
                    else:
                        p_count = data[(data[selected_features[0]] == selected_values[0]) &
                                       (data["num"] == cs)].count()
                        rules[counter]['support'] = p_count[0]
                    rules[counter]['class'] = cs
                    counter += 1
                    if isinstance(p, pandas.DataFrame):
                        data = data[~data.apply(tuple, 1).isin(p.apply(tuple, 1))]
                    else:
                        p = data[(data[selected_features[0]] == selected_values[0]) & (data["num"] == cs)]
                        data = data[~data.apply(tuple, 1).isin(p.apply(tuple, 1))]
                    selected_features.clear()
                    selected_values.clear()
                    features = list(main_data.columns)
                    features.remove("num")
                else:
                    features.remove(s_feature)
            else:
                break

    return rules


main()
