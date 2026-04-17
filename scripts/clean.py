import pandas as pd


def load_raw(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.drop(columns=["Name", "Doctor", "Hospital", "Date of Admission", "Discharge Date", "Room Number"])
    df.columns = [col.strip() for col in df.columns]
    return df.reset_index(drop=True)


def save_cleaned(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)
