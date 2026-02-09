/// Diaper Change Model
/// Modèle pour les changements de couches
/// Correspond au backend DiaperResponseSchema

enum DiaperType {
  wet,
  dirty,
  both,
  clean;

  String get displayName {
    switch (this) {
      case DiaperType.wet:
        return 'Mouillée';
      case DiaperType.dirty:
        return 'Salie';
      case DiaperType.both:
        return 'Les deux';
      case DiaperType.clean:
        return 'Propre';
    }
  }

  String get emoji {
    switch (this) {
      case DiaperType.wet:
        return '💧';
      case DiaperType.dirty:
        return '💩';
      case DiaperType.both:
        return '💧💩';
      case DiaperType.clean:
        return '✨';
    }
  }
}

class TimeSinceChange {
  final int hours;
  final int minutes;
  final int totalMinutes;

  TimeSinceChange({
    required this.hours,
    required this.minutes,
    required this.totalMinutes,
  });

  factory TimeSinceChange.fromJson(Map<String, dynamic> json) {
    return TimeSinceChange(
      hours: json['hours'] as int,
      minutes: json['minutes'] as int,
      totalMinutes: json['total_minutes'] as int,
    );
  }

  Map<String, dynamic> toJson() {
    return {'hours': hours, 'minutes': minutes, 'total_minutes': totalMinutes};
  }

  String get displayText {
    if (hours == 0) {
      return 'Il y a $minutes min';
    } else if (hours == 1) {
      return 'Il y a 1h${minutes > 0 ? ' $minutes' : ''}';
    } else {
      return 'Il y a ${hours}h${minutes > 0 ? ' $minutes' : ''}';
    }
  }
}

class Diaper {
  final int id;
  final int babyId;
  final DateTime changedAt;
  final DiaperType diaperType;
  final String? notes;
  final bool rashDetected;
  final bool creamApplied;
  final TimeSinceChange timeSince;
  final DateTime createdAt;
  final DateTime updatedAt;

  Diaper({
    required this.id,
    required this.babyId,
    required this.changedAt,
    required this.diaperType,
    this.notes,
    required this.rashDetected,
    required this.creamApplied,
    required this.timeSince,
    required this.createdAt,
    required this.updatedAt,
  });

  factory Diaper.fromJson(Map<String, dynamic> json) {
    return Diaper(
      id: json['id'] as int,
      babyId: json['baby_id'] as int,
      changedAt: DateTime.parse(json['changed_at'] as String),
      diaperType: DiaperType.values.firstWhere(
        (e) => e.name == json['diaper_type'],
      ),
      notes: json['notes'] as String?,
      rashDetected: json['rash_detected'] as bool,
      creamApplied: json['cream_applied'] as bool,
      timeSince: TimeSinceChange.fromJson(
        json['time_since'] as Map<String, dynamic>,
      ),
      createdAt: DateTime.parse(json['created_at'] as String),
      updatedAt: DateTime.parse(json['updated_at'] as String),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'baby_id': babyId,
      'changed_at': changedAt.toIso8601String(),
      'diaper_type': diaperType.name,
      'notes': notes,
      'rash_detected': rashDetected,
      'cream_applied': creamApplied,
      'time_since': timeSince.toJson(),
      'created_at': createdAt.toIso8601String(),
      'updated_at': updatedAt.toIso8601String(),
    };
  }

  /// Copie avec modifications
  Diaper copyWith({
    int? id,
    int? babyId,
    DateTime? changedAt,
    DiaperType? diaperType,
    String? notes,
    bool? rashDetected,
    bool? creamApplied,
    TimeSinceChange? timeSince,
    DateTime? createdAt,
    DateTime? updatedAt,
  }) {
    return Diaper(
      id: id ?? this.id,
      babyId: babyId ?? this.babyId,
      changedAt: changedAt ?? this.changedAt,
      diaperType: diaperType ?? this.diaperType,
      notes: notes ?? this.notes,
      rashDetected: rashDetected ?? this.rashDetected,
      creamApplied: creamApplied ?? this.creamApplied,
      timeSince: timeSince ?? this.timeSince,
      createdAt: createdAt ?? this.createdAt,
      updatedAt: updatedAt ?? this.updatedAt,
    );
  }

  /// Vérifie si le changement nécessite une attention
  bool get needsAttention =>
      rashDetected || (notes != null && notes!.isNotEmpty);

  /// Format d'affichage de l'heure
  String get formattedTime {
    return '${changedAt.hour.toString().padLeft(2, '0')}:${changedAt.minute.toString().padLeft(2, '0')}';
  }
}

/// Request DTO pour créer un changement
class DiaperCreateRequest {
  final int babyId;
  final DateTime changedAt;
  final DiaperType diaperType;
  final String? notes;
  final bool rashDetected;
  final bool creamApplied;

  DiaperCreateRequest({
    required this.babyId,
    required this.changedAt,
    required this.diaperType,
    this.notes,
    this.rashDetected = false,
    this.creamApplied = false,
  });

  Map<String, dynamic> toJson() {
    return {
      'baby_id': babyId,
      'changed_at': changedAt.toIso8601String(),
      'diaper_type': diaperType.name,
      'notes': notes,
      'rash_detected': rashDetected,
      'cream_applied': creamApplied,
    };
  }
}

/// Request DTO pour mettre à jour un changement
class DiaperUpdateRequest {
  final DateTime? changedAt;
  final DiaperType? diaperType;
  final String? notes;
  final bool? rashDetected;
  final bool? creamApplied;

  DiaperUpdateRequest({
    this.changedAt,
    this.diaperType,
    this.notes,
    this.rashDetected,
    this.creamApplied,
  });

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = {};
    if (changedAt != null) data['changed_at'] = changedAt!.toIso8601String();
    if (diaperType != null) data['diaper_type'] = diaperType!.name;
    if (notes != null) data['notes'] = notes;
    if (rashDetected != null) data['rash_detected'] = rashDetected;
    if (creamApplied != null) data['cream_applied'] = creamApplied;
    return data;
  }
}

/// Statistiques des changements
class DiaperStats {
  final int totalChanges;
  final int changesToday;
  final Diaper? lastChange;
  final int wetCount;
  final int dirtyCount;
  final int bothCount;
  final int cleanCount;
  final int rashDetectedCount;
  final int? averageIntervalMinutes;

  DiaperStats({
    required this.totalChanges,
    required this.changesToday,
    this.lastChange,
    required this.wetCount,
    required this.dirtyCount,
    required this.bothCount,
    required this.cleanCount,
    required this.rashDetectedCount,
    this.averageIntervalMinutes,
  });

  factory DiaperStats.fromJson(Map<String, dynamic> json) {
    return DiaperStats(
      totalChanges: json['total_changes'] as int,
      changesToday: json['changes_today'] as int,
      lastChange: json['last_change'] != null
          ? Diaper.fromJson(json['last_change'] as Map<String, dynamic>)
          : null,
      wetCount: json['wet_count'] as int,
      dirtyCount: json['dirty_count'] as int,
      bothCount: json['both_count'] as int,
      cleanCount: json['clean_count'] as int,
      rashDetectedCount: json['rash_detected_count'] as int,
      averageIntervalMinutes: json['average_interval_minutes'] as int?,
    );
  }

  /// Intervalle moyen formaté
  String get averageIntervalFormatted {
    if (averageIntervalMinutes == null) return 'N/A';
    final hours = averageIntervalMinutes! ~/ 60;
    final minutes = averageIntervalMinutes! % 60;
    if (hours == 0) return '$minutes min';
    return '${hours}h ${minutes}min';
  }
}﻿
