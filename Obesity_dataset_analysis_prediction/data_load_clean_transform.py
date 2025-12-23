
import pandas as pd
import os

import kagglehub

def load_dataset(kaggle_repo: str, kaggle_file: str) -> pd.DataFrame:
  """Load dataset from a .csv file path.

  Args:
      kaggle_repo (str): Kaggle repository identifier
      kaggle_file (str): CSV filename in the dataset
  Returns:
      pd.DataFrame: Loaded dataset
  """

  try:
    path = kagglehub.dataset_download(kaggle_repo)
    print(path)
    df = pd.read_csv(os.path.join(path, kaggle_file))
    lignes, colonnes = df.shape
    print(f"Dataset chargée avec succès. Taille du dataset : {lignes} lignes, {colonnes} colonnes") 
    return df
  
  except Exception as e:
    print("Error reading CSV file:", e)
    return None

def clean_transform_data(df: pd.DataFrame) -> pd.DataFrame:
  """Clean and transform the dataset.

  Args:
      df (pd.DataFrame): The dataset to clean and transform.
      drop_duplicates (bool): Whether to drop duplicate rows.
      drop_na (bool): Whether to drop rows with missing values.

  Returns:
      pd.DataFrame: _description_
  """

  df = df.drop_duplicates()  # Remove duplicate rows

  df = df.dropna()  # Remove missing values    
    
  # Convert categorical columns to category dtype
  categorical_columns = df.select_dtypes(include=['object']).columns
  for col in categorical_columns:
    df[col] = df[col].astype('category')
        
  return df

def load_clean_dataset(path_cleaned: str, Kaggle_repo: str, Kaggle_file: str) -> pd.DataFrame:
  """Charger et nettoyer le dataset d'obésité depuis le dossier local ou depuis Kaggle.

  Returns:
      pd.DataFrame: Dataset nettoyé
  """
  try: 
    df_cleaned = pd.read_csv(path_cleaned)
    print("Dataset nettoyé chargé depuis le fichier.")
  except FileNotFoundError:
    print("Fichier nettoyé non trouvé. Chargement et nettoyage du dataset brut.")
    df = load_dataset(Kaggle_repo, Kaggle_file)
    df_cleaned = clean_transform_data(df)
    os.makedirs(os.path.dirname(path_cleaned), exist_ok=True)
    df_cleaned.to_csv(path_cleaned, index=False)
    print("Dataset nettoyé sauvegardé dans le dossier data.")
  print(df_cleaned.info())
  return df_cleaned      