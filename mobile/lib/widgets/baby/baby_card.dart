import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../../core/models/baby.dart';

class BabyCard extends StatelessWidget {
  final Baby baby;
  final VoidCallback onTap;
  
  const BabyCard({
    super.key,
    required this.baby,
    required this.onTap,
  });
  
  String _calculateAge(DateTime birthDate) {
    final now = DateTime.now();
    final difference = now.difference(birthDate);
    final months = difference.inDays ~/ 30;
    
    if (months == 0) {
      return '${difference.inDays} jours';
    } else if (months < 12) {
      return '$months mois';
    } else {
      final years = months ~/ 12;
      final remainingMonths = months % 12;
      return remainingMonths > 0 
          ? '$ans an $remainingMonths mois' 
          : '$ans ans';
    }
  }
  
  @override
  Widget build(BuildContext context) {
    final age = _calculateAge(baby.birthDate);
    final formattedDate = DateFormat('dd/MM/yyyy').format(baby.birthDate);
    
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              // Avatar bébé
              CircleAvatar(
                radius: 30,
                backgroundColor: baby.gender == 'male' 
                    ? Colors.blue[100] 
                    : Colors.pink[100],
                child: Icon(
                  baby.gender == 'male' ? Icons.boy : Icons.girl,
                  size: 30,
                  color: baby.gender == 'male' ? Colors.blue : Colors.pink,
                ),
              ),
              
              const SizedBox(width: 16),
              
              // Infos bébé
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      baby.name,
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      'Né(e) le $formattedDate',
                      style: TextStyle(
                        fontSize: 14,
                        color: Colors.grey[600],
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      'Âge: $age',
                      style: const TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),
              
              // Icône flèche
              const Icon(
                Icons.chevron_right,
                color: Colors.grey,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
