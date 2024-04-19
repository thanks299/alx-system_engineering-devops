# Puppet manifest to install Flask from pip3

package { 'flask':
  add name => 'flask'
  ensure   => '2.1.0',
  provider => 'pip3',
}
