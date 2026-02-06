// lib/core/services/auth_service.dart
class AuthService {
  AuthService();
  
  Future<Map<String, dynamic>?> getUser() async {
    // Pour tester, retournez des données factices
    return {
      'name': 'Test User',
      'email': 'test@example.com',
    };
  }
  
  Future<void> logout() async {
    print('User logged out');
  }
}