#!/usr/bin/env puppet
#!/usr/local/lib/python3.8/dist-packages
#install flask from pip3
package {'flask':
ensure   => '2.1.0',
provider => 'pip3',
}
