import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd


def plot_distribution(df, colonne):
    nb_valeurs_uniques = df[colonne].nunique()

    if nb_valeurs_uniques < 8:
        # Pie chart
        counts = df[colonne].value_counts().reset_index()
        counts.columns = [colonne, "count"]

        fig = px.pie(
            counts,
            names=colonne,
            values="count",
            title=f"Répartition de {colonne}"
        )
    else:
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=("Histogramme", "Boxplot")
        )

        # Histogramme
        fig.add_trace(
            go.Histogram(x=df[colonne], name="Histogramme"),
            row=1, col=1
        )
        
        # Boxplot
        fig.add_trace(
            go.Box(x=df[colonne], name="Boxplot"),
            row=1, col=2
        )

        fig.update_layout(
            title=f"Distribution de {colonne}",
            showlegend=False
        )
    fig.update_layout(template="plotly_dark")

    return fig

def plot_x_y(df, x, y, color_hue=None):
    
    # détection des types
    is_x_num = pd.api.types.is_numeric_dtype(df[x])
    is_y_num = pd.api.types.is_numeric_dtype(df[y])

    # Numérique vs numérique :→ scatter
    if is_x_num and is_y_num:
        fig = px.scatter(
            df,
            x=x,
            y=y,
            color='NObeyesdad',
            title=f"{y} en fonction de {x}"
        )

    # Catégoriel vs numérique : boxplot
    elif not is_x_num and is_y_num:
        fig = px.box(
            df,
            x=x,
            y=y,
            color=x,
            color_discrete_sequence=px.colors.qualitative.Bold,
            title=f"{y} selon {x}"
        )

    elif is_x_num and not is_y_num:
        fig = px.box(
            df,
            x=y,
            y=x,
            color=y,
            color_discrete_sequence=px.colors.qualitative.Bold,
            title=f"{x} selon {y}"
        )

    # catégoriel vs catégoriel : bar chart
    else:
        counts = df.groupby([x, y]).size().reset_index(name="count")

        fig = px.bar(
            counts,
            x=x,
            y="count",
            color=y,
            barmode="group",
            title=f"Relation entre {x} et {y}"
        )

    fig.update_layout(template="plotly_dark")

    return fig

def plot_correlation_matrix(df):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numeric_df.corr()
    
    fig = px.imshow(
        corr_matrix,
        title="Matrice de corrélation",
        color_continuous_scale='RdBu_r',
        aspect="auto"
    )
    
    fig.update_layout(template="plotly_dark")
    
    return fig