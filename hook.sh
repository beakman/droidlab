#!/bin/bash
#

echo "OML HOOK READY"

LOGFILE=/root/oml2-server-hook.log
function log ()
{
        echo "$@" >&2
        echo "$@" >> ${LOGFILE}
}

SQLITE3=sqlite3
PGDUMP=pg_dump

while read COMMAND ARGUMENTS; do
        # One report line must be printed in each control path;
        # this first one puts out a timestamp and a dump of the received command, but no newline
        if [ -z "$COMMAND" ]; then
                continue
        fi
        log -n "`date`: '${COMMAND} ${ARGUMENTS}': "
        case "${COMMAND}" in
                "DBCREATED")
                        log "DB ${ARGUMENTS} created \n"
                        ;;
                "DBOPENED")
                        log "DB ${ARGUMENTS} opened \n"
                        ;;
                "DBCLOSED")
                        case "${ARGUMENTS}" in
                                file:*)
                                        DBNAME=${ARGUMENTS/file:/}
                                        DBFILE=${DBNAME}.`date +%Y-%m-%d_%H:%M:%S%z`.sqlite.sql
                                        log "SQLite3 DB ${DBNAME} closed, dumping as ${DBFILE} and pushing to iRODS \n"
                                        ${SQLITE3} ${DBNAME} .dump > ${DBFILE}
                                        log "[*] DBFILE= ${DBFILE} \n"
                                        ;;
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
                                        DBFILE=${DBNAME}.`date +%Y-%m-%d_%H:%M:%S%z`.pg.sql
                                        log "PostgreSQL DB ${DBNAME} closed, dumping as ${DBFILE} and pushing to iRODS"
                                        ${PGDUMP} -U ${USER} -h ${HOST} -p ${PORT} ${DBNAME} > ${DBFILE}
                                        log "[*] DBFILE= ${DBFILE} \n"
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