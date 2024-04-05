markers-replace:
	find . ! -name 'Makefile' ! -path './bin/*' ! -path './obj/*'  -type f | xargs perl -pi -e 's/{ms_port}/8080/g;'
	find . ! -name 'Makefile' ! -path '*.git' ! -path './bin/*' ! -path './obj/*'  -type f | xargs perl -pi -e 's/{ms_name}/msmachinelarning/g;'
	find . ! -name 'Makefile' ! -path '*.git' ! -path './bin/*' ! -path './obj/*'  -type f | xargs perl -pi -e 's/{ms_route}/machinelarning/g;'
 