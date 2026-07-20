from src.train_model import main as train_main
from src.predict import main as predict_main
from src.evaluate import main as evaluate_main


def main():
    print("=" * 50)
    print("Training Model...")
    train_main()

    print("=" * 50)
    print("Generating Predictions...")
    predict_main()

    print("=" * 50)
    print("Evaluating Model...")
    evaluate_main()

    print("=" * 50)
    print("Pipeline Completed Successfully!")


if __name__ == "__main__":
    main()