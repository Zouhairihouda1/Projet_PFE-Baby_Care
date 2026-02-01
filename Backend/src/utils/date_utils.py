"""
Date Utilities
Fonctions utilitaires pour la manipulation de dates
Spécifiquement pour le calcul d'âge des bébés
"""

from datetime import date, datetime, timedelta
from typing import Dict, Optional, Tuple
from dateutil.relativedelta import relativedelta


def calculate_age(birth_date: date, reference_date: Optional[date] = None) -> Dict[str, int]:
    """
    Calcule l'âge d'un bébé en jours, semaines, mois et années
    
    Args:
        birth_date: Date de naissance
        reference_date: Date de référence (par défaut: aujourd'hui)
    
    Returns:
        dict: {
            "days": int,      # Nombre de jours
            "weeks": int,     # Nombre de semaines
            "months": int,    # Nombre de mois
            "years": int      # Nombre d'années
        }
    
    Examples:
        >>> calculate_age(date(2025, 12, 1))
        {"days": 62, "weeks": 8, "months": 2, "years": 0}
    """
    if reference_date is None:
        reference_date = date.today()
    
    # Validation
    if birth_date > reference_date:
        raise ValueError("Birth date cannot be after reference date")
    
    # Calculer la différence
    delta = reference_date - birth_date
    
    # Jours
    days = delta.days
    
    # Semaines
    weeks = days // 7
    
    # Mois (méthode précise avec relativedelta)
    rd = relativedelta(reference_date, birth_date)
    months = rd.years * 12 + rd.months
    
    # Années
    years = rd.years
    
    return {
        "days": max(0, days),
        "weeks": max(0, weeks),
        "months": max(0, months),
        "years": max(0, years)
    }


def calculate_age_detailed(birth_date: date, reference_date: Optional[date] = None) -> Dict[str, int]:
    """
    Calcule l'âge de manière détaillée (années, mois, jours séparés)
    
    Args:
        birth_date: Date de naissance
        reference_date: Date de référence (par défaut: aujourd'hui)
    
    Returns:
        dict: {
            "years": int,      # Années complètes
            "months": int,     # Mois résiduels (0-11)
            "days": int,       # Jours résiduels (0-30)
            "total_days": int  # Total en jours
        }
    
    Examples:
        >>> calculate_age_detailed(date(2025, 10, 15))
        {"years": 0, "months": 3, "days": 17, "total_days": 108}
    """
    if reference_date is None:
        reference_date = date.today()
    
    if birth_date > reference_date:
        raise ValueError("Birth date cannot be after reference date")
    
    rd = relativedelta(reference_date, birth_date)
    delta = reference_date - birth_date
    
    return {
        "years": rd.years,
        "months": rd.months,
        "days": rd.days,
        "total_days": delta.days
    }


def get_age_label(birth_date: date, reference_date: Optional[date] = None) -> str:
    """
    Retourne un label textuel de l'âge adapté
    
    Args:
        birth_date: Date de naissance
        reference_date: Date de référence
    
    Returns:
        str: Label de l'âge (ex: "2 mois", "1 an et 3 mois", "15 jours")
    
    Examples:
        >>> get_age_label(date(2026, 1, 25))
        "7 jours"
        >>> get_age_label(date(2024, 6, 1))
        "1 an et 8 mois"
    """
    age = calculate_age_detailed(birth_date, reference_date)
    
    # Moins d'1 mois: afficher en jours
    if age["years"] == 0 and age["months"] == 0:
        if age["days"] == 0:
            return "Aujourd'hui"
        elif age["days"] == 1:
            return "1 jour"
        else:
            return f"{age['days']} jours"
    
    # Moins d'1 an: afficher en mois
    if age["years"] == 0:
        if age["months"] == 1:
            label = "1 mois"
        else:
            label = f"{age['months']} mois"
        
        # Ajouter les jours si significatifs
        if age["days"] > 0:
            label += f" et {age['days']} jour{'s' if age['days'] > 1 else ''}"
        
        return label
    
    # Plus d'1 an: afficher en années et mois
    if age["years"] == 1:
        label = "1 an"
    else:
        label = f"{age['years']} ans"
    
    if age["months"] > 0:
        if age["months"] == 1:
            label += " et 1 mois"
        else:
            label += f" et {age['months']} mois"
    
    return label


def get_age_group(birth_date: date, reference_date: Optional[date] = None) -> str:
    """
    Détermine le groupe d'âge du bébé
    
    Args:
        birth_date: Date de naissance
        reference_date: Date de référence
    
    Returns:
        str: Groupe d'âge (newborn, infant, toddler, preschooler)
    
    Age groups:
        - newborn: 0-28 jours
        - infant: 1-12 mois
        - toddler: 1-3 ans
        - preschooler: 3-5 ans
        - child: 5+ ans
    """
    age = calculate_age(birth_date, reference_date)
    
    if age["days"] <= 28:
        return "newborn"
    elif age["months"] < 12:
        return "infant"
    elif age["years"] < 3:
        return "toddler"
    elif age["years"] < 5:
        return "preschooler"
    else:
        return "child"


def is_birthday(birth_date: date, reference_date: Optional[date] = None) -> bool:
    """
    Vérifie si c'est l'anniversaire du bébé
    
    Args:
        birth_date: Date de naissance
        reference_date: Date à vérifier
    
    Returns:
        bool: True si c'est l'anniversaire
    """
    if reference_date is None:
        reference_date = date.today()
    
    return (birth_date.month == reference_date.month and 
            birth_date.day == reference_date.day)


def get_next_birthday(birth_date: date, reference_date: Optional[date] = None) -> Tuple[date, int]:
    """
    Calcule la date du prochain anniversaire
    
    Args:
        birth_date: Date de naissance
        reference_date: Date de référence
    
    Returns:
        tuple: (date_anniversaire, jours_restants)
    
    Examples:
        >>> get_next_birthday(date(2025, 12, 1))
        (date(2026, 12, 1), 303)
    """
    if reference_date is None:
        reference_date = date.today()
    
    # Calculer le prochain anniversaire
    next_birthday = date(reference_date.year, birth_date.month, birth_date.day)
    
    # Si l'anniversaire est déjà passé cette année, prendre l'année prochaine
    if next_birthday <= reference_date:
        next_birthday = date(reference_date.year + 1, birth_date.month, birth_date.day)
    
    # Calculer les jours restants
    days_until = (next_birthday - reference_date).days
    
    return next_birthday, days_until


def get_gestational_age(birth_date: date, gestational_weeks: int = 40,
                       reference_date: Optional[date] = None) -> Dict[str, int]:
    """
    Calcule l'âge gestationnel corrigé (pour prématurés)
    
    Args:
        birth_date: Date de naissance réelle
        gestational_weeks: Nombre de semaines de gestation à la naissance (par défaut 40)
        reference_date: Date de référence
    
    Returns:
        dict: {
            "chronological_age": {"weeks": int, "days": int},
            "corrected_age": {"weeks": int, "days": int},
            "correction_weeks": int
        }
    
    Note:
        Important pour les bébés prématurés (< 37 semaines)
        L'âge corrigé est utilisé pour évaluer le développement
    """
    if reference_date is None:
        reference_date = date.today()
    
    # Âge chronologique
    delta = reference_date - birth_date
    chrono_weeks = delta.days // 7
    chrono_days = delta.days % 7
    
    # Correction pour prématurité
    correction_weeks = 40 - gestational_weeks
    corrected_total_weeks = chrono_weeks - correction_weeks
    
    return {
        "chronological_age": {
            "weeks": chrono_weeks,
            "days": chrono_days
        },
        "corrected_age": {
            "weeks": max(0, corrected_total_weeks),
            "days": chrono_days
        },
        "correction_weeks": correction_weeks
    }


def format_date_for_display(date_obj: date, format_type: str = "long") -> str:
    """
    Formate une date pour l'affichage
    
    Args:
        date_obj: Date à formater
        format_type: Type de format (short, medium, long)
    
    Returns:
        str: Date formatée
    
    Examples:
        >>> format_date_for_display(date(2025, 12, 1), "long")
        "1er décembre 2025"
        >>> format_date_for_display(date(2025, 12, 1), "short")
        "01/12/2025"
    """
    if format_type == "short":
        return date_obj.strftime("%d/%m/%Y")
    elif format_type == "medium":
        return date_obj.strftime("%d %b %Y")
    else:  # long
        # Mapping mois français
        months_fr = [
            "", "janvier", "février", "mars", "avril", "mai", "juin",
            "juillet", "août", "septembre", "octobre", "novembre", "décembre"
        ]
        
        day = date_obj.day
        if day == 1:
            day_str = "1er"
        else:
            day_str = str(day)
        
        return f"{day_str} {months_fr[date_obj.month]} {date_obj.year}"


def parse_date_string(date_string: str) -> Optional[date]:
    """
    Parse une chaîne de date dans différents formats
    
    Args:
        date_string: Chaîne représentant une date
    
    Returns:
        date ou None si parsing échoue
    
    Supported formats:
        - YYYY-MM-DD (ISO)
        - DD/MM/YYYY
        - DD-MM-YYYY
    """
    formats = [
        "%Y-%m-%d",     # 2025-12-01
        "%d/%m/%Y",     # 01/12/2025
        "%d-%m-%Y",     # 01-12-2025
        "%Y/%m/%d",     # 2025/12/01
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    
    return None


# Constantes utiles
DAYS_PER_WEEK = 7
DAYS_PER_MONTH_AVG = 30.44  # Moyenne
DAYS_PER_YEAR = 365.25  # Moyenne (incluant années bissextiles)
WEEKS_PER_MONTH_AVG = 4.35
MONTHS_PER_YEAR = 12
