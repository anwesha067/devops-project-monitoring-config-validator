class monitoring_validator {
  package { 'python3':
    ensure => installed,
  }

  service { 'validator':
    ensure => running,
  }
}