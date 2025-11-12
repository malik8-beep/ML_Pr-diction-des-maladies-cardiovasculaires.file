import streamlit as st

# --- Titre et description de l'application ---
st.title("Prédiction des maladies cardiovasculaires")
st.write("Bienvenue dans cette application de démonstration.")
st.markdown("---") # Ajout d'une ligne de séparation

# --- Démarrer le Formulaire ---
# Le 'key' (ex: "prediction_form") est obligatoire pour identifier le formulaire
with st.form(key='prediction_form'):
    st.header("Saisie des données du patient")

    # 1. Widgets de saisie pour les caractéristiques du patient
    
    # Utilisez st.number_input pour les nombres (âge, poids, etc.)
    age = st.number_input(
        'Âge (en années)', 
        min_value=18, 
        max_value=100, 
        value=50, 
        step=1
    )
    
    # Utilisez st.selectbox ou st.radio pour les catégories
    genre = st.selectbox(
        'Genre', 
        ('Femme', 'Homme')
    )
    
    cholesterol = st.radio(
        'Niveau de Cholestérol',
        ('Normal', 'Au-dessus de la normale', 'Beaucoup au-dessus de la normale')
    )
    
    # Utilisez un champ pour la tension artérielle (systolique et diastolique)
    col1, col2 = st.columns(2) # Crée deux colonnes pour aligner les champs

    with col1:
        pression_systolique = st.number_input(
            'Pression artérielle Systolique (mmHg)', 
            min_value=80, 
            max_value=200, 
            value=120, 
            step=5
        )
    with col2:
        pression_diastolique = st.number_input(
            'Pression artérielle Diastolique (mmHg)', 
            min_value=50, 
            max_value=120, 
            value=80, 
            step=5
        )
        
    # 2. Bouton de soumission du formulaire
    # IMPORTANT : Le bouton de soumission DOIT être le dernier élément du 'with st.form(...):'
    submit_button = st.form_submit_button(label='Faire la Prédiction')

# --- Traitement après soumission ---
if submit_button:
    st.success("Formulaire soumis avec succès!")
    
    # Ici, vous inséreriez votre logique de prédiction (votre modèle de Machine Learning)
    st.subheader("Résumé des données saisies :")
    st.write(f"Âge : **{age}** ans")
    st.write(f"Genre : **{genre}**")
    st.write(f"Cholestérol : **{cholesterol}**")
    st.write(f"Tension : **{pression_systolique} / {pression_diastolique}** mmHg")
    
    # Exemple de résultat (à remplacer par le résultat de votre modèle)
    st.warning("⚠️ **Résultat de la prédiction : Risque Élevé** (Ceci est un exemple, le modèle réel doit être intégré ici)")
