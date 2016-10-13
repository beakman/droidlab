#!/bin/bash
#

echo "OML HOOK READY"

while read COMMAND ARGUMENTS; do
	# Continue if no command
	if [ -z "$COMMAND" ]; then
		continue
	fi

	case "${COMMAND}" in
		"DBCREATED")
			log "DB ${ARGUMENTS} created \n"
			;;
		"DBOPENED")
			log "DB ${ARGUMENTS} opened \n"
			;;
		"DBCLOSED")
			# When database is closed (the experiment has finished) we call the python script
			# and send the data to our Django App.
			case "${ARGUMENTS}" in
				# If we use SQLite backend
				file:*)
					DBNAME=${ARGUMENTS/file:/}
					log "[*] DBFILE= ${DBFILE} do something."
					;;
				# PostgreSQL backend
				postgresql://*)
					# Separate the components of the URI by gradually eating them off the TMP variable
					TMP="${ARGUMENTS/postgresql:\/\//}"
					USER=${TMP/@*/}
					TMP=${TMP/${USER}@/}
					HOST=${TMP/:*/}
					TMP=${TMP/${HOST}:/}
					PORT=${TMP/\/*/}
					TMP=${TMP/${PORT}\//}
					DBNAME=${TMP}
					log "[+] Usuario: ${USER}"
					log "[+] Host: ${HOST}"
					log "[+] Puerto: ${PORT}"
					log "[+] Base de datos: ${DBNAME}"
					;;
				*)
					log "DB ${ARGUMENTS} closed, but don't know how to handle it"
					;;
			esac
			;;
		"EXIT")
			log "Exiting"
			exit 0
			;;
		*)
			log "Unknown command"
			;;
	esac
done