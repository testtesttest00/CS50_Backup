import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).
    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []

    months = [
        "Jan","Feb","Mar","Apr","May","June",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]
    visitor = {"New_Visitor" : 0, "Other" : 0, "Returning_Visitor" : 1}
    truth = ["FALSE", "TRUE"]

    column_converter = {
        "Administrative" : int,
        "Administrative_Duration" : float,
        "Informational" : int,
        "Informational_Duration" : float,
        "ProductRelated" : int,
        "ProductRelated_Duration" : float,
        "BounceRates" : float,
        "ExitRates" : float,
        "PageValues" : float,
        "SpecialDay" : float,
        "Month" : months.index,
        "OperatingSystems" : int,
        "Browser" : int,
        "Region" : int,
        "TrafficType" : int,
        "VisitorType" : lambda x : visitor[x],
        "Weekend" : truth.index,
        "Revenue" : truth.index
    }

    with open(filename, "r") as file:
        for row in csv.DictReader(file):
            evidence_list = [
                column_converter[col](row[col])
                for col in column_converter if col != "Revenue"
            ]
            evidence.append(evidence_list)
            labels.append(column_converter["Revenue"](row["Revenue"]))

            # alternative method
            #
            # administrative = row["Administrative"]
            # administrative_duration = row["Administrative_Duration"]
            # informational = row["Informational"]
            # informational_duration = row["Informational_Duration"]
            # productrelated = row["ProductRelated"]
            # productrelated_duration = row["ProductRelated_Duration"]
            # bouncerates = row["BounceRates"]
            # exitrates = row["ExitRates"]
            # pagevalues = row["PageValues"]
            # specialday = row["SpecialDay"]
            # month = months.index(row["Month"])
            # operatingsystems = row["OperatingSystems"]
            # browser = row["Browser"]
            # region = row["Region"]
            # traffictype = row["TrafficType"]
            # visitortype = visitor[row["VisitorType"]]
            # weekend = truth.index(row["Weekend"])
            # revenue = truth.index(row["Revenue"])
            # evidence_list = [
            #     int(administrative),
            #     float(administrative_duration),
            #     int(informational),
            #     float(informational_duration),
            #     int(productrelated),
            #     float(productrelated_duration),
            #     float(bouncerates),
            #     float(exitrates),
            #     float(pagevalues),
            #     float(specialday),
            #     month,
            #     int(operatingsystems),
            #     int(browser),
            #     int(region),
            #     int(traffictype),
            #     visitortype,
            #     weekend
            # ]
            # evidence.append(evidence_list)
            # labels.append(revenue)

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    K = 1
    model = KNeighborsClassifier(n_neighbors = K)
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensitivity = 0
    positives = 0
    specificity = 0
    negatives = 0
    for i in range(len(labels)):
        if labels[i] == 1:
            positives += 1
            if labels[i] == predictions[i]:
                sensitivity += 1
        else:
            negatives += 1
            if labels[i] == predictions[i]:
                specificity += 1
    sensitivity = sensitivity / positives
    specificity = specificity / negatives

    return sensitivity,specificity


if __name__ == "__main__":
    main()
