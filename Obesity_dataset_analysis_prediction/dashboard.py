# app/dashboard.py
import streamlit as st
import pandas as pd
#import plotly.express as px
from data_load_clean_transform import load_clean_dataset
from config import Kaggle_repo, Kaggle_file, DATA_PROCESSED_PATH
#from src.visualization import plot_distribution, plot_time_series

# --- Configuration de la page ---
st.set_page_config(
    page_title="Obesity Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Titre et description ---
st.title("📊 Dashboard d'Analyse des données d'obésité")
st.markdown("<h2 style='color: #1E88E5;'>Flavie Kolb</h2>", unsafe_allow_html=True)

# Sidebar pour la navigation
with st.sidebar:
    st.header("Navigation")
    section = st.radio(
        "Aller à :",
        ["1. Présentation des données", "2. Analyses des données", "3. Prédictions"],
        index=0  # Par défaut, la première section est sélectionnée
    )

# --- Chargement des données ---
@st.cache_data
def load_data():
    return load_clean_dataset(path_cleaned=DATA_PROCESSED_PATH, Kaggle_repo=Kaggle_repo, Kaggle_file=Kaggle_file)

data = load_data()

# Contenu principal en fonction de la section sélectionnée
if section == "1. Présentation des données":
    st.header("1. Présentation des données")
    st.write("Apperçu du dataset :")
    
    st.dataframe(data)
    
    st.write("Description des variables :")
  
    st.markdown("""
    | **Nom / Name**                  | **Type**   | **Description (Français)**                                                                                     | **Description (English)**                                                                                     | **Notes**                                                                 |
    |---------------------------------|------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
    | **Gender**                      | string     | Genre de la personne (`Male` ou `Female`).                                                                     | Gender of the person (`Male` or `Female`).                                                                     | Standardisé en majuscules / Standardized in uppercase.                     |
    | **Age**                         | int        | Âge de la personne en années.                                                                               | Age of the person in years.                                                                                   | Valeurs plausibles : 14–61 ans / Plausible values: 14–61 years.              |
    | **Height**                      | float      | Taille de la personne en mètres.                                                                            | Height of the person in meters.                                                                              | Arrondi à 2 décimales / Rounded to 2 decimal places.                        |
    | **Weight**                      | float      | Poids de la personne en kilogrammes.                                                                        | Weight of the person in kilograms.                                                                           | Arrondi à 1 décimale / Rounded to 1 decimal place.                         |
    | **family_history_with_overweight** | string  | Antécédents familiaux d'obésité ou de surpoids (`yes` ou `no`).                                              | Family history of obesity or overweight (`yes` or `no`).                                                      |                                                                           |
    | **FAVC**                        | string     | Consommation fréquente d'aliments riches en calories (`yes` ou `no`).                                        | Frequent consumption of high-calorie food (`yes` or `no`).                                                     |                                                                           |
    | **FCVC**                        | float      | Fréquence de consommation de légumes (échelle de 1 à 3).                                                    | Frequency of vegetable consumption (scale from 1 to 3).                                                       | 1 = Rarement, 2 = Parfois, 3 = Toujours / 1 = Rarely, 2 = Sometimes, 3 = Always. |
    | **NCP**                         | float      | Nombre de repas principaux par jour.                                                                        | Number of main meals per day.                                                                                 |                                                                           |
    | **CAEC**                        | string     | Fréquence de consommation d'aliments entre les repas (`Never`, `Sometimes`, `Frequently`, `Always`).         | Frequency of eating between meals (`Never`, `Sometimes`, `Frequently`, `Always`).                            |                                                                           |
    | **SMOKE**                       | string     | La personne fume-t-elle (`yes` ou `no`) ?                                                                    | Does the person smoke (`yes` or `no`)?                                                                        |                                                                           |
    | **CH2O**                        | float      | Consommation quotidienne d'eau (échelle de 1 à 3).                                                           | Daily water intake (scale from 1 to 3).                                                                      | 1 = Peu, 2 = Moyenne, 3 = Beaucoup / 1 = Low, 2 = Medium, 3 = High.           |
    | **SCC**                         | string     | La personne surveille-t-elle son apport calorique (`yes` ou `no`) ?                                          | Does the person monitor their calorie intake (`yes` or `no`)?                                                  |                                                                           |
    | **FAF**                         | float      | Fréquence d'activité physique (échelle de 0 à 3).                                                            | Frequency of physical activity (scale from 0 to 3).                                                          | 0 = Jamais, 1 = Parfois, 2 = Souvent, 3 = Toujours / 0 = Never, 1 = Sometimes, 2 = Often, 3 = Always. |
    | **TUE**                         | float      | Temps passé sur les appareils technologiques (échelle de 0 à 3).                                            | Time spent using technology devices (scale from 0 to 3).                                                     | 0 = Jamais, 1 = Parfois, 2 = Souvent, 3 = Toujours / 0 = Never, 1 = Sometimes, 2 = Often, 3 = Always. |
    | **CALC**                        | string     | Fréquence de consommation d'alcool (`Never`, `Sometimes`, `Frequently`, `Always`).                          | Frequency of alcohol consumption (`Never`, `Sometimes`, `Frequently`, `Always`).                            |                                                                           |
    | **MTRANS**                      | string     | Moyen de transport principal (`Automobile`, `Bike`, `Motorbike`, `Public Transportation`, `Walking`).       | Main mode of transportation (`Automobile`, `Bike`, `Motorbike`, `Public Transportation`, `Walking`).         |                                                                           |
    | **NObeyesdad**                  | string     | Niveau d'obésité (`Insufficient Weight`, `Normal Weight`, `Overweight Level I`, `Overweight Level II`, `Obesity Type I`, `Obesity Type II`, `Obesity Type III`). | Obesity level (`Insufficient Weight`, `Normal Weight`, `Overweight Level I`, `Overweight Level II`, `Obesity Type I`, `Obesity Type II`, `Obesity Type III`). | Catégorie cible pour l'analyse / Target category for analysis.                     |
    """)

elif section == "2. Analyses des données":
    st.header("2. Analyses des données")
    st.write("Contenu de la section 2...")
    # Ajoute ici ton code pour la section 2
    # Création des onglets
    tab1, tab2 = st.tabs(["Analyse univariée ", "Analyse Mutlivariée"])
    
        # Contenu de l'onglet 1
    with tab1:
        st.header("Analyse des Données")
        st.write("Voici un exemple de tableau de données :")

        st.subheader("Graphique de la colonne 1")
        #fig = px.line(data, x=data.index, y='colonne1', title='Évolution de la colonne 1')
        st.plotly_chart(fig, use_container_width=True)
    
    # Contenu de l'onglet 2
    with tab2:
        st.header("Visualisations")
        st.write("Voici un graphique interactif :")
        #fig2 = px.bar(data, x=data.index, y='colonne2', title='Valeurs de la colonne 2')
        st.plotly_chart(fig2, use_container_width=True)

elif section == "3. Prédictions":
    st.header("3. Prédictions")
    st.write("Contenu de la section 3...")
    # Ajoute ici ton code pour la section 3

