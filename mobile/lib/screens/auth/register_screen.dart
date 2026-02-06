import 'package:flutter/material.dart';

class RegisterScreen extends StatelessWidget {
  const RegisterScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF0A3D62), // BLEU MARINE
      
      appBar: AppBar(
        backgroundColor: Color(0xFF0A3D62),
        title: Text('Créer un compte', style: TextStyle(color: Colors.white)),
        leading: IconButton(
          icon: Icon(Icons.arrow_back, color: Colors.white),
          onPressed: () => Navigator.pop(context),
        ),
      ),
      
      body: Container(
        color: Color(0xFF0A3D62),
        child: Center(
          child: Container(
            width: 400,
            margin: EdgeInsets.all(20),
            padding: EdgeInsets.all(30),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(20),
              boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 10)],
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                // Logo
                Container(
                  width: 100,
                  height: 100,
                  decoration: BoxDecoration(
                    color: Color(0xFF0A3D62),
                    borderRadius: BorderRadius.circular(50),
                  ),
                  child: Icon(Icons.child_care, color: Colors.white, size: 50),
                ),
                
                SizedBox(height: 20),
                
                Text(
                  'Inscription',
                  style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF0A3D62),
                  ),
                ),
                
                SizedBox(height: 30),
                
                // Formulaire simple
                TextField(
                  decoration: InputDecoration(
                    labelText: 'Nom complet',
                    border: OutlineInputBorder(),
                  ),
                ),
                
                SizedBox(height: 15),
                
                TextField(
                  decoration: InputDecoration(
                    labelText: 'Email',
                    border: OutlineInputBorder(),
                  ),
                ),
                
                SizedBox(height: 15),
                
                TextField(
                  obscureText: true,
                  decoration: InputDecoration(
                    labelText: 'Mot de passe',
                    border: OutlineInputBorder(),
                  ),
                ),
                
                SizedBox(height: 30),
                
                // Bouton
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () {
                      Navigator.pushReplacementNamed(context, '/home');
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Color(0xFF0A3D62),
                      padding: EdgeInsets.all(16),
                    ),
                    child: Text(
                      'Créer mon compte',
                      style: TextStyle(fontSize: 16, color: Colors.white),
                    ),
                  ),
                ),
                
                SizedBox(height: 20),
                
                TextButton(
                  onPressed: () => Navigator.pop(context),
                  child: Text(
                    'Déjà un compte ? Se connecter',
                    style: TextStyle(color: Color(0xFF0A3D62)),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
