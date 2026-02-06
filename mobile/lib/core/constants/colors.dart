// lib/core/constants/colors.dart
import 'package:flutter/material.dart';

class AppColors {
  // Palette principale - Bleu doux pour bébé
  static const Color primary = Color(0xFF6EC5E9);
  static const Color primaryLight = Color(0xFFA5D8F3);
  static const Color primaryDark = Color(0xFF4A90E2);
  
  // Palette secondaire - Rose doux pour bébé
  static const Color secondary = Color(0xFFFFB7D5);
  static const Color secondaryLight = Color(0xFFFFE4EE);
  static const Color secondaryDark = Color(0xFFFF8FB9);
  
  // Neutres
  static const Color background = Color(0xFFF8FAFF);
  static const Color surface = Color(0xFFFFFFFF);
  static const Color card = Color(0xFFF5F9FF);
  
  // Texte
  static const Color textPrimary = Color(0xFF2C3E50);
  static const Color textSecondary = Color(0xFF7F8C8D);
  static const Color textHint = Color(0xFFBDC3C7);
  
  // Accents
  static const Color success = Color(0xFF5CD85A);
  static const Color error = Color(0xFFFF6B6B);
  static const Color warning = Color(0xFFFFD166);
  static const Color info = Color(0xFF4ECDC4);
  
  // Dégradés
  static const Gradient primaryGradient = LinearGradient(
    colors: [Color(0xFF6EC5E9), Color(0xFF4A90E2)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );
  
  static const Gradient secondaryGradient = LinearGradient(
    colors: [Color(0xFFFFB7D5), Color(0xFFFF8FB9)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );
}
