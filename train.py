from config import DATA_FILE
from data_loader import load_stock_data
from indicators import add_indicators
from labeler import create_labels
from trainer import train_model, save_model


def main():

    print("Loading Data...")

    df = load_stock_data(DATA_FILE)

    print("Calculating Indicators...")

    df = add_indicators(df)

    print("Generating Labels...")

    df = create_labels(df)

    print("Training Random Forest...")

    result = train_model(df)

    save_model(result["model"], result["scaler"])

    print("\n==============================")
    print("Training Complete")
    print("==============================")
    print(f"Accuracy : {result['accuracy']*100:.2f}%")
    print(result["report"])


if __name__ == "__main__":
    main()