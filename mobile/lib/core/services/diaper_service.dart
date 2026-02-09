/// Diaper Service
/// Service pour communiquer avec l'API backend des changements de couches

import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/diaper.dart';
import '../config/api_config.dart';
import '../services/auth_service.dart';

class DiaperService {
  final String baseUrl = ApiConfig.baseUrl;
  final AuthService _authService = AuthService();

  /// Headers avec authentification
  Future<Map<String, String>> get _headers async {
    final token = await _authService.getToken();
    return {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token',
    };
  }

  /// Créer un changement de couche
  Future<Diaper> createDiaperChange(DiaperCreateRequest request) async {
    final response = await http.post(
      Uri.parse('$baseUrl/diapers/'),
      headers: await _headers,
      body: jsonEncode(request.toJson()),
    );

    if (response.statusCode == 201) {
      return Diaper.fromJson(jsonDecode(response.body));
    } else if (response.statusCode == 400) {
      final error = jsonDecode(response.body);
      throw Exception(error['detail'] ?? 'Erreur de validation');
    } else if (response.statusCode == 401) {
      throw Exception('Non authentifié');
    } else {
      throw Exception('Erreur lors de l\'enregistrement du changement');
    }
  }

  /// Récupérer tous les changements d'un bébé
  Future<List<Diaper>> getBabyDiaperChanges(
    int babyId, {
    int skip = 0,
    int limit = 50,
  }) async {
    final response = await http.get(
      Uri.parse('$baseUrl/diapers/baby/$babyId?skip=$skip&limit=$limit'),
      headers: await _headers,
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final items = data['items'] as List;
      return items.map((json) => Diaper.fromJson(json)).toList();
    } else if (response.statusCode == 404) {
      throw Exception('Bébé non trouvé');
    } else {
      throw Exception('Erreur lors de la récupération des changements');
    }
  }

  /// Récupérer un changement spécifique
  Future<Diaper> getDiaperById(int diaperId) async {
    final response = await http.get(
      Uri.parse('$baseUrl/diapers/$diaperId'),
      headers: await _headers,
    );

    if (response.statusCode == 200) {
      return Diaper.fromJson(jsonDecode(response.body));
    } else if (response.statusCode == 404) {
      throw Exception('Changement non trouvé');
    } else {
      throw Exception('Erreur lors de la récupération');
    }
  }

  /// Mettre à jour un changement
  Future<Diaper> updateDiaperChange(
    int diaperId,
    DiaperUpdateRequest request,
  ) async {
    final response = await http.put(
      Uri.parse('$baseUrl/diapers/$diaperId'),
      headers: await _headers,
      body: jsonEncode(request.toJson()),
    );

    if (response.statusCode == 200) {
      return Diaper.fromJson(jsonDecode(response.body));
    } else if (response.statusCode == 404) {
      throw Exception('Changement non trouvé');
    } else {
      throw Exception('Erreur lors de la mise à jour');
    }
  }

  /// Supprimer un changement
  Future<void> deleteDiaperChange(int diaperId, {bool permanent = false}) async {
    final response = await http.delete(
      Uri.parse('$baseUrl/diapers/$diaperId?permanent=$permanent'),
      headers: await _headers,
    );

    if (response.statusCode != 204) {
      throw Exception('Erreur lors de la suppression');
    }
  }

  /// Récupérer les statistiques
  Future<DiaperStats> getStatistics(int babyId, {int days = 30}) async {
    final response = await http.get(
      Uri.parse('$baseUrl/diapers/baby/$babyId/statistics?days=$days'),
      headers: await _headers,
    );

    if (response.statusCode == 200) {
      return DiaperStats.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Erreur lors de la récupération des statistiques');
    }
  }

  /// Récupérer les changements d'aujourd'hui
  Future<List<Diaper>> getTodayChanges(int babyId) async {
    final now = DateTime.now();
    final startOfDay = DateTime(now.year, now.month, now.day);
    final endOfDay = startOfDay.add(const Duration(days: 1));

    // Récupérer tous les changements et filtrer côté client
    final allChanges = await getBabyDiaperChanges(babyId, limit: 100);
    
    return allChanges.where((diaper) {
      return diaper.changedAt.isAfter(startOfDay) &&
             diaper.changedAt.isBefore(endOfDay);
    }).toList();
  }
}
