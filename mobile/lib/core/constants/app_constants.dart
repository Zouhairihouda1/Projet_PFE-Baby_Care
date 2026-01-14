class AppConstants {
  // App Info
  static const String appName = 'Baby Care';
  static const String appVersion = '1.0.0';
  
  // API
  static const String apiBaseUrl = 'http://localhost:8000/api/v1';
  static const int connectTimeout = 5000;
  static const int receiveTimeout = 5000;
  
  // Routes
  static const String loginRoute = '/';
  static const String registerRoute = '/register';
  static const String homeRoute = '/home';
  static const String babyListRoute = '/babies';
  static const String healthRoute = '/health';
  static const String dailyLogRoute = '/daily-log';
  
  // Storage Keys
  static const String tokenKey = 'auth_token';
  static const String userKey = 'user_data';
  static const String themeKey = 'app_theme';
  
  // Validation
  static const int minPasswordLength = 6;
  static const int maxPasswordLength = 50;
}
