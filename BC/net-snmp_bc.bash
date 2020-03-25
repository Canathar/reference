#!/bin/bash
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Copyright (C) Harris Corporation 2012 - 2019
# Harris Proprietary Information
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FILE:              net-snmp_bc.bash
#
# DESCRIPTION:       This script processes a Backward Compatibility SNMP request (GET, GET NEXT, SET) through
#                    command line parameters and generates the response to stdout
#
# SOFTWARE HISTORY:
#
#  Date     US/DE    Name        Description
#  -------  -------  ----------  ------------------------------------------------------------------------------------------------
#  20FEB19  US22895  jlaccone    Prototype SNMP version reporting Mechanism
#**********************************************************************************************************************************
# NOTES:
#
#   This script is configured to run from snmpd.conf
#
#   To Generate Binary Build Data
#   -----------------------------
#     cat build_data.xml | xxd -p -c 8192 > build_data.dat && echo "" >> build_data.dat
#     md5sum -b build_data.dat > build_data.dat.md5
#
#
#   To Verify Binary Build Data
#   ---------------------------
#     md5sum -c build_data.dat.md5
#
#
#   To Decode Binary Build Data
#   ---------------------------
#     cat build_data.dat | xxd -r -p > build_data.xml
#
#**********************************************************************************************************************************
# Diagnostic Flag
DEBUG=false

# Sourcing Flag
SOURCE=false

# Automation Flag
JENKINS=false

# Script Operational Server Flags
IS_SIPCONF=false
IS_SIPPROXY=false



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                     ===== Build File Data =====                                               ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
#----- Binary Files -----
BUILD_FILE_BIN_PATH="/home/zabbix/datafiles/bc"

BUILD_FILE_BIN_MD5_NAME="build_data.dat.md5"
BUILD_FILE_BIN_NAME="build_data.dat"

BUILD_FILE_BIN_FULLNAME="${BUILD_FILE_BIN_PATH}/${BUILD_FILE_BIN_NAME}"
BUILD_FILE_BIN_MD5_FULLNAME="${BUILD_FILE_BIN_PATH}/${BUILD_FILE_BIN_MD5_NAME}"


#----- Text Files -----
BUILD_FILE_TXT_PATH="/tmp"

BUILD_FILE_TXT_NAME="build_data.xml"

BUILD_FILE_TXT_FULLNAME="${BUILD_FILE_TXT_PATH}/${BUILD_FILE_TXT_NAME}"



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                     ===== Script Strings =====                                                ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- Script Debug Strings -----
STRING_DEBUG_MAIN_HEADER="Debug Information"


# ----- Script Info Strings -----
STRING_INFO_BUILD_FILE="Build File -"
STRING_INFO_BUILD_FILE_BIN_MD5="Build MD5 File -"

STRING_INFO_RELEASE_VERSIONS="   --- Obtaining Release Version Data ---   "
STRING_INFO_CURRENT_RELEASE_VERSION="Build data current release version -"
STRING_INFO_PREVIOUS_RELEASE_VERSION="Build data previous release verison -"


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       Current Protocol Versions For Local Manager Interface                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
STRING_INFO_CURRENT_LM_INTERFACE_VERSIONS="   --- Obtaining Local Manager Current Version Data ---   "

STRING_INFO_CURRENT_SNMP_VERSION=" device build data, current VCS21 SNMP Parser version -"
STRING_INFO_CURRENT_XMLCONFIG_VERSION=" device build data, current XML Config version -"


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                            Current Protocol Versions For SIP Interface                                        ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
STRING_INFO_CURRENT_SIP_INTERFACE_VERSIONS="   --- Obtaining SIP Interface Current Version Data ---   "

STRING_INFO_CURRENT_SIP_VERSION=" device build data, current SIP version -"
STRING_INFO_CURRENT_RTSP_VERSION=" device build data, current RTSP version -"
STRING_INFO_CURRENT_RTP_VERSION=" device build data, current RTP version -"


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       Previous Protocol Versions For Local Manager Interface                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
STRING_INFO_PREVIOUS_LM_INTERFACE_VERSIONS="   --- Obtaining Local Manager Previous Version Data ---   "

STRING_INFO_PREVIOUS_SNMP_VERSION=" device build data, previous VCS21 SNMP Parser version -"
STRING_INFO_PREVIOUS_XMLCONFIG_VERSION=" device build data, previous XML Config version -"


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                            Previous Protocol Versions For SIP Interface                                       ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
STRING_INFO_PREVIOUS_SIP_INTERFACE_VERSIONS="   --- Obtaining SIP Interface Previous Version Data ---   "

STRING_INFO_PREVIOUS_SIP_VERSION=" device build data, previous SIP version -"
STRING_INFO_PREVIOUS_RTSP_VERSION=" device build data, previous RTSP version -"
STRING_INFO_PREVIOUS_RTP_VERSION=" device build data, previous RTP version -"



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                  ===== Build File Xpath =====                                                 ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- Release Versions Build File Xpath -----
CURRENT_RELEASE_VERSION_ENTRY_XPATH='//build/release-versions/current/text()'
PREVIOUS_RELEASE_VERSION_ENTRY_XPATH='//build/release-versions/previous/text()'


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       Current Protocol Versions For Local Manager Interface                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- SIP Conference Server - Build File Xpath -----
CONF_CURRENT_SNMP_VERSION_ENTRY_XPATH='//build/emb/sipconf/current/lm-interface-versions/vcs21-snmp-parser/text()'
CONF_CURRENT_XMLCONFIG_VERSION_ENTRY_XPATH='//build/emb/sipconf/current/lm-interface-versions/xml-config/text()'

# ----- SIP Proxy Server - Build File Xpath -----
PROXY_CURRENT_SNMP_VERSION_ENTRY_XPATH='//build/emb/sipproxy/current/lm-interface-versions/vcs21-snmp-parser/text()'
PROXY_CURRENT_XMLCONFIG_VERSION_ENTRY_XPATH='//build/emb/sipproxy/current/lm-interface-versions/xml-config/text()'


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                            Current Protocol Versions For SIP Interface                                        ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- SIP Conference Server - Build File Xpath -----
CONF_CURRENT_SIP_VERSION_ENTRY_XPATH='//build/emb/sipconf/current/sip-interface-versions/sip/text()'
CONF_CURRENT_RTSP_VERSION_ENTRY_XPATH='//build/emb/sipconf/current/sip-interface-versions/rtsp/text()'
CONF_CURRENT_RTP_VERSION_ENTRY_XPATH='//build/emb/sipconf/current/sip-interface-versions/rtp/text()'

# ----- SIP Proxy Server - Build File Xpath -----
PROXY_CURRENT_SIP_VERSION_ENTRY_XPATH='//build/emb/sipproxy/current/sip-interface-versions/sip/text()'


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       Previous Protocol Versions For Local Manager Interface                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- SIP Conference Server - Build File Xpath -----
CONF_PREVIOUS_SNMP_VERSION_ENTRY_XPATH='//build/emb/sipconf/previous/lm-interface-versions/vcs21-snmp-parser/text()'
CONF_PREVIOUS_XMLCONFIG_VERSION_ENTRY_XPATH='//build/emb/sipconf/previous/lm-interface-versions/xml-config/text()'

# ----- SIP Proxy Server - Build File Xpath -----
PROXY_PREVIOUS_SNMP_VERSION_ENTRY_XPATH='//build/emb/rmg/previous/lm-interface-versions/vcs21-snmp-parser/text()'
PROXY_PREVIOUS_XMLCONFIG_VERSION_ENTRY_XPATH='//build/emb/sipproxy/previous/lm-interface-versions/xml-config/text()'


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                            Previous Protocol Versions For SIP Interface                                       ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- SIP Conference Server - Build File Xpath -----
CONF_PREVIOUS_SIP_VERSION_ENTRY_XPATH='//build/emb/sipconf/previous/sip-interface-versions/sip/text()'
CONF_PREVIOUS_RTSP_VERSION_ENTRY_XPATH='//build/emb/sipconf/previous/sip-interface-versions/rtsp/text()'
CONF_PREVIOUS_RTP_VERSION_ENTRY_XPATH='//build/emb/sipconf/previous/sip-interface-versions/rtp/text()'

# ----- SIP Proxy Server - Build File Xpath -----
PROXY_PREVIOUS_SIP_VERSION_ENTRY_XPATH='//build/emb/sipproxy/previous/sip-interface-versions/sip/text()'



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                    ===== MIB Object Id's =====                                                ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- SIP Conf Backward Compatibility Base OID: backwardCompatibility OBJECT IDENTIFIER ::= { sipproxyObjects 3 } -----
#----- Use the MIB to lookup the value instead of hard-coding the following: .1.3.6.1.4.1.290.6.7.9.1.3 -----
OID_SIP_CONF_BC_BASE=$(snmptranslate -m +HARRIS-MIB:ION-MIB:ION-SIPCONF -On ION-SIPCONF::backwardCompatibility)

# ----- SIP Proxy Backward Compatibility Base OID: backwardCompatibility OBJECT IDENTIFIER ::= { sipproxyObjects 3 } -----
#----- Use the MIB to lookup the value instead of hard-coding the following: .1.3.6.1.4.1.290.6.7.11.1.1 -----
OID_SIP_PROXY_BC_BASE=$(snmptranslate -m +HARRIS-MIB:ION-MIB:ION-SIPPROXY -On ION-SIPPROXY::backwardCompatibility)



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                    ===== MIB Object Types =====                                               ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# Define the Release Versions
TYPE_CURRENT_RELEASE_VERSION="string"
TYPE_PREVIOUS_RELEASE_VERSION="string"

# Define the current LM Interface Versions
TYPE_CURRENT_SNMP_VERSION="string"
TYPE_CURRENT_XMLCONFIG_VERSION="string"

# Define the current SIP Interface Versions
TYPE_CURRENT_SIP_VERSION="string"
TYPE_CURRENT_RTSP_VERSION="string"
TYPE_CURRENT_RTP_VERSION="string"

# Define the previous LM Interface Versions
TYPE_PREVIOUS_SNMP_VERSION="string"
TYPE_PREVIOUS_XMLCONFIG_VERSION="string"

# Define the previous SIP Interface Versions
TYPE_PREVIOUS_SIP_VERSION="string"
TYPE_PREVIOUS_RTSP_VERSION="string"
TYPE_PREVIOUS_RTP_VERSION="string"



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                    ===== MIB Object Values =====                                              ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# Define the Release Versions
CURRENT_RELEASE_VERSION_VALUE=""
PREVIOUS_RELEASE_VERSION_VALUE=""

# Define the current LM Interface Versions
CURRENT_SNMP_VERSION_VALUE=""
CURRENT_XMLCONFIG_VERSION_VALUE=""

# Define the current SIP Interface Versions
CURRENT_SIP_VERSION_VALUE=""
CURRENT_RTSP_VERSION_VALUE=""
CURRENT_RTP_VERSION_VALUE=""

# Define the previous LM Interface Versions
PREVIOUS_SNMP_VERSION_VALUE=""
PREVIOUS_XMLCONFIG_VERSION_VALUE=""

# Define the previous SIP Interface Versions
PREVIOUS_SIP_VERSION_VALUE=""
PREVIOUS_RTSP_VERSION_VALUE=""
PREVIOUS_RTP_VERSION_VALUE=""



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                                                               ║
# ║                                                    ===== Request Variables =====                                              ║
# ║                                                                                                                               ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
# ----- Type of Request Flags -----
REQUEST_GET=false
REQUEST_GET_NEXT=false
REQUEST_SET=false

#----- Object Id associated with request
OID_GET=""
OID_GET_NEXT=""
OID_SET=""

# ----- Associated object variable type -----
TYPE_INTEGER=false
TYPE_GAUGE=false
TYPE_COUNTER=false
TYPE_TIMETICKS=false
TYPE_IPADDRESS=false
TYPE_OBJECTID=false
TYPE_STRING=false

# ----- Associated object value -----
VALUE_INTEGER=""
VALUE_GAUGE=""
VALUE_COUNTER=""
VALUE_TIMETICKS=""
VALUE_IPADDRESS=""
VALUE_OBJECTID=""
VALUE_STRING=""



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     decodeBuildData                                                                                                       ║
# ║                                                                                                                               ║
# ║ @brief  Function to decode binary build data file into plain text and obtain version information                              ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
decodeBuildData()
{
   # Verify that the build file has not been modified
   if [[ "${DEBUG}" == true ]]; then printInfo "Verifying Binary Build File With md5 -" "${BUILD_FILE_BIN_MD5_FULLNAME}"; fi
   cd "${BUILD_FILE_BIN_PATH}"
   md5sum -c "${BUILD_FILE_BIN_MD5_FULLNAME}" > /dev/null
   if [[ $? != 0 ]]; then

      printError "Build File Does Not Verify! - " "${BUILD_FILE_BIN_FULLNAME}"
      exit 2

   fi

   # Determine if the build file exists
   if [ ! -e "${BUILD_FILE_TXT_FULLNAME}" ]; then

      if [[ "${DEBUG}" == true ]]; then printInfo "Creating Text Based Build File -" "${BUILD_FILE_TXT_FULLNAME}"; fi
      if [[ "${DEBUG}" == true ]]; then echo; fi

      # Decode the binary file into UTF-8 XML
      cat "${BUILD_FILE_BIN_FULLNAME}" | xxd -r -p > "${BUILD_FILE_TXT_FULLNAME}"

   else

      if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_BUILD_FILE}" "${BUILD_FILE_TXT_FULLNAME}"; fi
      if [[ "${DEBUG}" == true ]]; then echo; fi

   fi

   # Release Versions From Build File
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_RELEASE_VERSIONS}"; fi

   CURRENT_RELEASE_VERSION_VALUE=`xmllint --xpath ${CURRENT_RELEASE_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_RELEASE_VERSION}" "${CURRENT_RELEASE_VERSION_VALUE}"; fi

   PREVIOUS_RELEASE_VERSION_VALUE=`xmllint --xpath ${PREVIOUS_RELEASE_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_RELEASE_VERSION}" "${PREVIOUS_RELEASE_VERSION_VALUE}"; fi

   if [[ "${DEBUG}" == true ]]; then echo; fi


   # ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   # ║                                       Current Protocol Versions For Local Manager Interface                                ║
   # ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_LM_INTERFACE_VERSIONS}"; fi

   if [[ "${IS_SIPCONF}" ==  "true" ]]
   then

      # ----- SIP Conference -----
      CURRENT_SNMP_VERSION_VALUE=`xmllint --xpath ${CONF_CURRENT_SNMP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_CURRENT_SNMP_VERSION}" "${CURRENT_SNMP_VERSION_VALUE}"; fi

      CURRENT_XMLCONFIG_VERSION_VALUE=`xmllint --xpath ${CONF_CURRENT_XMLCONFIG_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_CURRENT_XMLCONFIG_VERSION}" "${CURRENT_XMLCONFIG_VERSION_VALUE}"; fi

   elif [[ "${IS_SIPPROXY}" ==  "true" ]]
   then

      # ----- SIP Proxy -----
      CURRENT_SNMP_VERSION_VALUE=`xmllint --xpath ${PROXY_CURRENT_SNMP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy ${STRING_INFO_CURRENT_SNMP_VERSION}" "${CURRENT_SNMP_VERSION_VALUE}"; fi

      CURRENT_XMLCONFIG_VERSION_VALUE=`xmllint --xpath ${PROXY_CURRENT_XMLCONFIG_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy ${STRING_INFO_CURRENT_XMLCONFIG_VERSION}" "${CURRENT_XMLCONFIG_VERSION_VALUE}"; fi

   else

      if [[ "${DEBUG}" == true ]]; then echo; fi

   fi

   if [[ "${DEBUG}" == true ]]; then echo; fi



   # ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   # ║                                            Current Protocol Versions For SIP Interface                                     ║
   # ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_SIP_INTERFACE_VERSIONS}"; fi

   if [[ "${IS_SIPCONF}" ==  "true" ]]
   then

      # ----- SIP Conference -----
      CURRENT_SIP_VERSION_VALUE=`xmllint --xpath ${CONF_CURRENT_SIP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_CURRENT_SIP_VERSION}" "${CURRENT_SIP_VERSION_VALUE}"; fi

      CURRENT_RTSP_VERSION_VALUE=`xmllint --xpath ${CONF_CURRENT_RTSP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_CURRENT_RTSP_VERSION}" "${CURRENT_RTSP_VERSION_VALUE}"; fi

      CURRENT_RTP_VERSION_VALUE=`xmllint --xpath ${CONF_CURRENT_RTP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_CURRENT_RTP_VERSION}" "${CURRENT_RTP_VERSION_VALUE}"; fi

   elif [[ "${IS_SIPPROXY}" ==  "true" ]]
   then

      # ----- SIP Proxy -----
      CURRENT_SIP_VERSION_VALUE=`xmllint --xpath ${PROXY_CURRENT_SIP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy ${STRING_INFO_CURRENT_SIP_VERSION}" "${CURRENT_SIP_VERSION_VALUE}"; fi

   else

      if [[ "${DEBUG}" == true ]]; then echo; fi

   fi

   if [[ "${DEBUG}" == true ]]; then echo; fi



   # ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   # ║                                       Previous Protocol Versions For Local Manager Interface                               ║
   # ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_LM_INTERFACE_VERSIONS}"; fi

   if [[ "${IS_SIPCONF}" ==  "true" ]]
   then

      # ----- SIP Conference -----
      PREVIOUS_SNMP_VERSION_VALUE=`xmllint --xpath ${CONF_PREVIOUS_SNMP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_PREVIOUS_SNMP_VERSION}" "${PREVIOUS_SNMP_VERSION_VALUE}"; fi

      PREVIOUS_XMLCONFIG_VERSION_VALUE=`xmllint --xpath ${CONF_PREVIOUS_XMLCONFIG_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_PREVIOUS_XMLCONFIG_VERSION}" "${PREVIOUS_XMLCONFIG_VERSION_VALUE}"; fi

   elif [[ "${IS_SIPPROXY}" ==  "true" ]]
   then

      # ----- SIP Proxy -----
      PREVIOUS_SNMP_VERSION_VALUE=`xmllint --xpath ${PROXY_PREVIOUS_SNMP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy ${STRING_INFO_PREVIOUS_SNMP_VERSION}" "${PREVIOUS_SNMP_VERSION_VALUE}"; fi

      PREVIOUS_XMLCONFIG_VERSION_VALUE=`xmllint --xpath ${PROXY_PREVIOUS_XMLCONFIG_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy ${STRING_INFO_PREVIOUS_XMLCONFIG_VERSION}" "${PREVIOUS_XMLCONFIG_VERSION_VALUE}"; fi

   else

      if [[ "${DEBUG}" == true ]]; then echo; fi

   fi

   if [[ "${DEBUG}" == true ]]; then echo; fi



   # ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   # ║                                            Previous Protocol Versions For SIP Interface                                    ║
   # ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
   if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_SIP_INTERFACE_VERSIONS}"; fi

   if [[ "${IS_SIPCONF}" ==  "true" ]]
   then

      # ----- SIP Conference -----
      PREVIOUS_SIP_VERSION_VALUE=`xmllint --xpath ${CONF_PREVIOUS_SIP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_PREVIOUS_SIP_VERSION}" "${PREVIOUS_SIP_VERSION_VALUE}"; fi

      PREVIOUS_RTSP_VERSION_VALUE=`xmllint --xpath ${CONF_PREVIOUS_RTSP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_PREVIOUS_RTSP_VERSION}" "${PREVIOUS_RTSP_VERSION_VALUE}"; fi

      PREVIOUS_RTP_VERSION_VALUE=`xmllint --xpath ${CONF_PREVIOUS_RTP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Conf ${STRING_INFO_PREVIOUS_RTP_VERSION}" "${PREVIOUS_RTP_VERSION_VALUE}"; fi

   elif [[ "${IS_SIPPROXY}" ==  "true" ]]
   then

      # ----- SIP Proxy -----
      PREVIOUS_SIP_VERSION_VALUE=`xmllint --xpath ${PROXY_PREVIOUS_SIP_VERSION_ENTRY_XPATH} ${BUILD_FILE_TXT_FULLNAME}`
      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy ${STRING_INFO_PREVIOUS_SIP_VERSION}" "${PREVIOUS_SIP_VERSION_VALUE}"; fi

   else

      if [[ "${DEBUG}" == true ]]; then echo; fi

   fi

   if [[ "${DEBUG}" == true ]]; then echo; fi



}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     defineServerOIDs                                                                                                      ║
# ║                                                                                                                               ║
# ║ @brief  Function to set MIB object ids based on operational server type                                                       ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
defineServerOIDs()
{
   if [[ "${IS_SIPCONF}" ==  "true" ]]
   then

      OID_BC_BASE="${OID_SIP_CONF_BC_BASE}"

      # backwardCompatibility             { sipconfObjects 1 }
      # ------------------------------------------------------
         # currentReleaseVersion             { backwardCompatibility 1 }
         # previousReleaseVersion            { backwardCompatibility 2 }
         OID_CURRENT_RELEASE_VERSION="${OID_SIP_CONF_BC_BASE}.1"
         OID_PREVIOUS_RELEASE_VERSION="${OID_SIP_CONF_BC_BASE}.2"


         # currentInterfaceVersions          { backwardCompatibility 3 }
         # -------------------------------------------------------------

            # currentLMInterfaceVersions        { currentInterfaceVersions 1 }
            # ----------------------------------------------------------------
               # currentVcs21SnmpParserVersion     { currentLMInterfaceVersions 1 }
               # currentXmlConfigVersion           { currentLMInterfaceVersions 2 }
               OID_CURRENT_VCS21_SNMP_PARSER_VERSION="${OID_SIP_CONF_BC_BASE}.3.1.1"
               OID_CURRENT_XMLCONFIG_VERSION="${OID_SIP_CONF_BC_BASE}.3.1.2"

            # currentSIPInterfaceVersions       { currentInterfaceVersions 2 }
            # ----------------------------------------------------------------
               # currentSipVersion                 { currentSIPInterfaceVersions 1 }
               # currentRtspVersion                { currentSIPInterfaceVersions 2 }
               # currentRtpVersion                 { currentSIPInterfaceVersions 3 }
               OID_CURRENT_SIP_VERSION="${OID_SIP_CONF_BC_BASE}.3.2.1"
               OID_CURRENT_RTSP_VERSION="${OID_SIP_CONF_BC_BASE}.3.2.2"
               OID_CURRENT_RTP_VERSION="${OID_SIP_CONF_BC_BASE}.3.2.3"


         # previousInterfaceVersions         { backwardCompatibility 4 }
         # -------------------------------------------------------------

            # previousLMInterfaceVersions       { previousInterfaceVersions 1 }
            # -----------------------------------------------------------------
               # previousVcs21SnmpParserVersion    { previousLMInterfaceVersions 1 }
               # previousXmlConfigVersion          { previousLMInterfaceVersions 2 }
               OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION="${OID_SIP_CONF_BC_BASE}.4.1.1"
               OID_PREVIOUS_XMLCONFIG_VERSION="${OID_SIP_CONF_BC_BASE}.4.1.2"

            # previousSIPInterfaceVersions      { previousInterfaceVersions 2 }
            # -----------------------------------------------------------------
               # previousSipVersion                { previousSIPInterfaceVersions 1 }
               # previousRtspVersion               { previousSIPInterfaceVersions 2 }
               # previousRtpVersion                { previousSIPInterfaceVersions 3 }
               OID_PREVIOUS_SIP_VERSION="${OID_SIP_CONF_BC_BASE}.4.2.1"
               OID_PREVIOUS_RTSP_VERSION="${OID_SIP_CONF_BC_BASE}.4.2.2"
               OID_PREVIOUS_RTP_VERSION="${OID_SIP_CONF_BC_BASE}.4.2.3"

   elif [[ "${IS_SIPPROXY}" ==  "true" ]]
   then

      OID_BC_BASE="${OID_SIP_PROXY_BC_BASE}"

      # backwardCompatibility             { sipproxyObjects 3 }
      # ------------------------------------------------------
         # currentReleaseVersion             { backwardCompatibility 1 }
         # previousReleaseVersion            { backwardCompatibility 2 }
         OID_CURRENT_RELEASE_VERSION="${OID_SIP_PROXY_BC_BASE}.1"
         OID_PREVIOUS_RELEASE_VERSION="${OID_SIP_PROXY_BC_BASE}.2"


         # currentInterfaceVersions          { backwardCompatibility 3 }
         # -------------------------------------------------------------

            # currentLMInterfaceVersions        { currentInterfaceVersions 1 }
            # ----------------------------------------------------------------
               # currentVcs21SnmpParserVersion     { currentLMInterfaceVersions 1 }
               # currentXmlConfigVersion           { currentLMInterfaceVersions 2 }
               OID_CURRENT_VCS21_SNMP_PARSER_VERSION="${OID_SIP_PROXY_BC_BASE}.3.1.1"
               OID_CURRENT_XMLCONFIG_VERSION="${OID_SIP_PROXY_BC_BASE}.3.1.2"

            # currentSIPInterfaceVersions       { currentInterfaceVersions 2 }
            # ----------------------------------------------------------------
               # currentSipVersion                 { currentSIPInterfaceVersions 1 }
               OID_CURRENT_SIP_VERSION="${OID_SIP_PROXY_BC_BASE}.3.2.1"


         # previousInterfaceVersions         { backwardCompatibility 4 }
         # -------------------------------------------------------------

            # previousLMInterfaceVersions       { previousInterfaceVersions 1 }
            # -----------------------------------------------------------------
               # previousVcs21SnmpParserVersion    { previousLMInterfaceVersions 1 }
               # previousXmlConfigVersion          { previousLMInterfaceVersions 2 }
               OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION="${OID_SIP_PROXY_BC_BASE}.4.1.1"
               OID_PREVIOUS_XMLCONFIG_VERSION="${OID_SIP_PROXY_BC_BASE}.4.1.2"

            # previousSIPInterfaceVersions      { previousInterfaceVersions 2 }
            # -----------------------------------------------------------------
               # previousSipVersion                { previousSIPInterfaceVersions 1 }
               OID_PREVIOUS_SIP_VERSION="${OID_SIP_PROXY_BC_BASE}.4.2.1"

   else

      if [[ "${DEBUG}" == true ]]; then printInfo "Default OIDs Detected"; fi

   fi

}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     determineServerType                                                                                                   ║
# ║                                                                                                                               ║
# ║ @brief  Function to set operational server based on hostname                                                                  ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
determineServerType()
{
   # Capture the server hostname
   SERVER_HOSTNAME=$(hostname)
   if [[ "${DEBUG}" == true ]]; then printInfo "Server Hostname -" "${SERVER_HOSTNAME}"; fi

   # Determine which server type we are running on
   if [[ ${SERVER_HOSTNAME} =~ ^(.*sipconf.*)$ ]]
   then

      if [[ "${DEBUG}" == true ]]; then printInfo "Conference Server Detected"; fi
      IS_SIPCONF=true

   elif [[ ${SERVER_HOSTNAME} =~ ^(.*sipproxy.*)$ ]]
   then

      if [[ "${DEBUG}" == true ]]; then printInfo "Proxy Server Detected"; fi
      IS_SIPPROXY=true

   else

      # Default to SIP Proxy at this point, there may be additional servers in the future
      if [[ "${DEBUG}" == true ]]; then printInfo "Default Server Detected"; fi
      IS_SIPPROXY=true

   fi

}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     displayDebug                                                                                                          ║
# ║                                                                                                                               ║
# ║ @brief  Function to display the status of the internal variables                                                              ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
displayDebug()
{
   # All tab characters that begin the line will be ignored in the output
   #    https://en.wikipedia.org/wiki/Here_document#Unix_shells
   cat <<-EOF

	==============================================================================
	                            $(printDebugVariable "${STRING_DEBUG_MAIN_HEADER}")
	==============================================================================

	   ------------------------------------------------------------------------
	                            $(printDebugVariable "Script Variables")
	   ------------------------------------------------------------------------

	   Script Version                      : $(printInfoVariable "${version}")
	   Shortopts                           : $(printInfoVariable "${shortopts}")
	   Longopts                            : $(printInfoVariable "${longopts}")

	   ------------------------------------------------------------------------
	                            $(printDebugVariable "MIB OID Variables")
	   ------------------------------------------------------------------------
	      These variables contain the OIDs from the MIB

	   Backward Compatibility Base OID     : $(printInfoVariable "${OID_SIP_PROXY_BC_BASE}")

	   Current Release Version OID         : $(printInfoVariable "${OID_CURRENT_RELEASE_VERSION}")
	   Previous Release Version OID        : $(printInfoVariable "${OID_PREVIOUS_RELEASE_VERSION}")

	   ------------------------------------------------------------------------
	                         $(printDebugVariable "Request OID Variables")
	   ------------------------------------------------------------------------
	      These variables contain the id for the object to process

	   Get Request OID                     : $(printInfoVariable "${OID_GET}")
	   Get Next Request OID                : $(printInfoVariable "${OID_GET_NEXT}")
	   Set Request OID                     : $(printInfoVariable "${OID_SET}")

	   ------------------------------------------------------------------------
	                            $(printDebugVariable "Request Variables")
	   ------------------------------------------------------------------------
	      These variables contain the flags denoting the type of request
	      to process

	   Get Request                         : $(printInfoVariable "${REQUEST_GET}")
	   Get Next Request                    : $(printInfoVariable "${REQUEST_GET_NEXT}")
	   Set Request                         : $(printInfoVariable "${REQUEST_SET}")

	   ------------------------------------------------------------------------
	                            $(printDebugVariable "XPATH Variables")
	   ------------------------------------------------------------------------
	      These variables are used to obtain the version information from
	      the XML build file


	   Cur Release Xpath                   : $(printInfoVariable "${CURRENT_RELEASE_VERSION_ENTRY_XPATH}")
	   Pre Release Xpath                   : $(printInfoVariable "${PREVIOUS_RELEASE_VERSION_ENTRY_XPATH}")

	==============================================================================

	EOF

}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printError                                                                                                            ║
# ║                                                                                                                               ║
# ║ @brief  Function to add delimiters and error color tags to a variable for terminal printing                                   ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printError()
{
   echo -e $(printErrVariable "===== ERROR:") $(printErrVariable "${1}") $(printErrVariable "${2}") $(printErrVariable "=====")
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printInfo                                                                                                             ║
# ║                                                                                                                               ║
# ║ @brief  Function to add delimiters and info color tags to a variable for terminal printing                                    ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printInfo()
{
   echo -e $(printInfoVariable "===== INFO:") $(printInfoVariable "${1}") $(printInfoVariable "${2}") $(printInfoVariable "=====")
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printDebugVariable                                                                                                    ║
# ║                                                                                                                               ║
# ║ @brief  Function to add debug color tags to a variable for terminal printing                                                  ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printDebugVariable()
{
   printf '\033[33m'"$@"'\033[0m'
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printErrVariable                                                                                                      ║
# ║                                                                                                                               ║
# ║ @brief  Function to add error color tags to a variable for terminal printing                                                  ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printErrVariable()
{
   if [[ "${JENKINS}" == true ]]
   then

      printf "$@"

   else

      printf '\033[31m'"$@"'\033[0m'

   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     printInfoVariable                                                                                                     ║
# ║                                                                                                                               ║
# ║ @brief  Function to add info color tags to a variable for terminal printing                                                   ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
printInfoVariable()
{
   if [[ "${JENKINS}" == true ]]
   then

      printf "$@"

   else

      printf '\033[92m'"$@"'\033[0m'

   fi
}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     processGetRequest                                                                                                     ║
# ║                                                                                                                               ║
# ║ @brief  Function to process an SNMP Get Request                                                                               ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
processGetRequest()
{
   if [[ "${DEBUG}" == true ]]; then printInfo "Processing SNMP GET Request"; fi

   case "$1" in

      "${OID_CURRENT_RELEASE_VERSION}"|"${OID_CURRENT_RELEASE_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_RELEASE_VERSION}" "${CURRENT_RELEASE_VERSION_VALUE}"; fi
         echo "${OID_CURRENT_RELEASE_VERSION}"
         echo "${TYPE_CURRENT_RELEASE_VERSION}"
         echo "${CURRENT_RELEASE_VERSION_VALUE}"
         ;;

      "${OID_PREVIOUS_RELEASE_VERSION}"|"${OID_PREVIOUS_RELEASE_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_RELEASE_VERSION}" "${PREVIOUS_RELEASE_VERSION_VALUE}"; fi
         echo "${OID_PREVIOUS_RELEASE_VERSION}"
         echo "${TYPE_PREVIOUS_RELEASE_VERSION}"
         echo "${PREVIOUS_RELEASE_VERSION_VALUE}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                    Current Protocol Versions For Local Manager Interface                                ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_CURRENT_VCS21_SNMP_PARSER_VERSION}"|"${OID_CURRENT_VCS21_SNMP_PARSER_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_SNMP_VERSION}" "${CURRENT_SNMP_VERSION_VALUE}"; fi
         echo "${OID_CURRENT_VCS21_SNMP_PARSER_VERSION}"
         echo "${TYPE_CURRENT_SNMP_VERSION}"
         echo "${CURRENT_SNMP_VERSION_VALUE}"
         ;;

      "${OID_CURRENT_XMLCONFIG_VERSION}"|"${OID_CURRENT_XMLCONFIG_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_XMLCONFIG_VERSION}" "${CURRENT_XMLCONFIG_VERSION_VALUE}"; fi
         echo "${OID_CURRENT_XMLCONFIG_VERSION}"
         echo "${TYPE_CURRENT_XMLCONFIG_VERSION}"
         echo "${CURRENT_XMLCONFIG_VERSION_VALUE}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                         Current Protocol Versions For SIP Interface                                     ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_CURRENT_SIP_VERSION}"|"${OID_CURRENT_SIP_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_SIP_VERSION}" "${CURRENT_SIP_VERSION_VALUE}"; fi
         echo "${OID_CURRENT_SIP_VERSION}"
         echo "${TYPE_CURRENT_SIP_VERSION}"
         echo "${CURRENT_SIP_VERSION_VALUE}"
         ;;

      "${OID_CURRENT_RTSP_VERSION}"|"${OID_CURRENT_RTSP_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_RTSP_VERSION}" "${CURRENT_RTSP_VERSION_VALUE}"; fi
         echo "${OID_CURRENT_RTSP_VERSION}"
         echo "${TYPE_CURRENT_RTSP_VERSION}"
         echo "${CURRENT_RTSP_VERSION_VALUE}"
         ;;

      "${OID_CURRENT_RTP_VERSION}"|"${OID_CURRENT_RTP_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_CURRENT_RTP_VERSION}" "${CURRENT_RTP_VERSION_VALUE}"; fi
         echo "${OID_CURRENT_RTP_VERSION}"
         echo "${TYPE_CURRENT_RTP_VERSION}"
         echo "${CURRENT_RTP_VERSION_VALUE}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                   Previous Protocol Versions For Local Manager Interface                                ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION}"|"${OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_SNMP_VERSION}" "${PREVIOUS_SNMP_VERSION_VALUE}"; fi
         echo "${OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION}"
         echo "${TYPE_PREVIOUS_SNMP_VERSION}"
         echo "${PREVIOUS_SNMP_VERSION_VALUE}"
         ;;

      "${OID_PREVIOUS_XMLCONFIG_VERSION}"|"${OID_PREVIOUS_XMLCONFIG_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_XMLCONFIG_VERSION}" "${PREVIOUS_XMLCONFIG_VERSION_VALUE}"; fi
         echo "${OID_PREVIOUS_XMLCONFIG_VERSION}"
         echo "${TYPE_PREVIOUS_XMLCONFIG_VERSION}"
         echo "${PREVIOUS_XMLCONFIG_VERSION_VALUE}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                         Previous Protocol Versions For SIP Interface                                    ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_PREVIOUS_SIP_VERSION}"|"${OID_PREVIOUS_SIP_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_SIP_VERSION}" "${PREVIOUS_SIP_VERSION_VALUE}"; fi
         echo "${OID_PREVIOUS_SIP_VERSION}"
         echo "${TYPE_PREVIOUS_SIP_VERSION}"
         echo "${PREVIOUS_SIP_VERSION_VALUE}"
         ;;

      "${OID_PREVIOUS_RTSP_VERSION}"|"${OID_PREVIOUS_RTSP_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_RTSP_VERSION}" "${PREVIOUS_RTSP_VERSION_VALUE}"; fi
         echo "${OID_PREVIOUS_RTSP_VERSION}"
         echo "${TYPE_PREVIOUS_RTSP_VERSION}"
         echo "${PREVIOUS_RTSP_VERSION_VALUE}"
         ;;

      "${OID_PREVIOUS_RTP_VERSION}"|"${OID_PREVIOUS_RTP_VERSION}.0")

         if [[ "${DEBUG}" == true ]]; then printInfo "${STRING_INFO_PREVIOUS_RTP_VERSION}" "${PREVIOUS_RTP_VERSION_VALUE}"; fi
         echo "${OID_PREVIOUS_RTP_VERSION}"
         echo "${TYPE_PREVIOUS_RTP_VERSION}"
         echo "${PREVIOUS_RTP_VERSION_VALUE}"
         ;;


      *)
         if [[ "${DEBUG}" == true ]]; then printInfo "OID Not Found"; fi
         ;;

   esac

}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     processGetNextRequest                                                                                                 ║
# ║                                                                                                                               ║
# ║ @brief  Function to process an SNMP Get Request                                                                               ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
processGetNextRequest()
{
   if [[ "${DEBUG}" == true ]]; then printInfo "Processing SNMP GETNEXT Request"; fi

   case "$1" in

      "${OID_BC_BASE}")

         processGetRequest "${OID_CURRENT_RELEASE_VERSION}"
         ;;

      "${OID_CURRENT_RELEASE_VERSION}")

         processGetRequest "${OID_PREVIOUS_RELEASE_VERSION}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                    Current Protocol Versions For Local Manager Interface                                ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_PREVIOUS_RELEASE_VERSION}")

         processGetRequest "${OID_CURRENT_VCS21_SNMP_PARSER_VERSION}"
         ;;

      "${OID_CURRENT_VCS21_SNMP_PARSER_VERSION}")

         processGetRequest "${OID_CURRENT_XMLCONFIG_VERSION}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                         Current Protocol Versions For SIP Interface                                     ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_CURRENT_XMLCONFIG_VERSION}")

         processGetRequest "${OID_CURRENT_SIP_VERSION}"
         ;;

       "${OID_CURRENT_SIP_VERSION}")

         processGetRequest "${OID_CURRENT_RTSP_VERSION}"
         ;;

      "${OID_CURRENT_RTSP_VERSION}")

         processGetRequest "${OID_CURRENT_RTP_VERSION}"
         ;;

      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                   Previous Protocol Versions For Local Manager Interface                                ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_CURRENT_RTP_VERSION}")

         processGetRequest "${OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION}"
         ;;

      "${OID_PREVIOUS_VCS21_SNMP_PARSER_VERSION}")

         processGetRequest "${OID_PREVIOUS_XMLCONFIG_VERSION}"
         ;;


      # ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
      # ║                                         Previous Protocol Versions For SIP Interface                                    ║
      # ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
      "${OID_PREVIOUS_XMLCONFIG_VERSION}")

         processGetRequest "${OID_PREVIOUS_SIP_VERSION}"
         ;;

      "${OID_PREVIOUS_SIP_VERSION}")

         processGetRequest "${OID_PREVIOUS_RTSP_VERSION}"
         ;;

      "${OID_PREVIOUS_RTSP_VERSION}")

         processGetRequest "${OID_PREVIOUS_RTP_VERSION}"
         ;;


      *)
         if [[ "${DEBUG}" == true ]]; then printInfo "No More OIDs Found"; fi
         ;;

   esac

}


# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     Usage                                                                                                                 ║
# ║                                                                                                                               ║
# ║ @brief  Function that displays the operation of the script                                                                    ║
# ║                                                                                                                               ║
# ║ @return void                                                                                                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
usage()
{
   # All tab characters that begin the line will be ignored in the output
   #    https://en.wikipedia.org/wiki/Here_document#Unix_shells
   cat <<-EOF
	Usage: `basename "$0"` [OPTION(S)...]


	OPTIONS

	   ========== SNMP Agent Commands ==========

	   -g <oid>
	      Specifies a MIB object to query for a value

	   -n <oid>
	      Specifies the object id to query the next instance value

	   -s <oid> <type> <value>
	      Specifies the object id, type and value to modify


	   ========== Information Commands ==========

	   -h, --help
	      Display usage information (this text)



	NOTES

	   Utility to create a manifest file for the currently installed software (unzipped files) and compare
	   individual files to the currently installed software, using the created manifest.


	Examples:

	   # Build the running manifest file (specify file name ONLY, path will be managed internally)
	   `basename "$0"` -g ${OID_CURRENT_RELEASE_VERSION}

	   # Compare the map.bin with the currently installed software
	   `basename "$0"` -n ${OID_PREVIOUS_RELEASE_VERSION}


	EOF

   return
}



# ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ @fn     main                                                                                                                  ║
# ║                                                                                                                               ║
# ║ @brief  Function to be the main execution point for the script                                                                ║
# ║                                                                                                                               ║
# ║ @return Integer value representing the script execution status code                                                           ║
# ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
main()
{
   # Ensure the command line was called with parameters
   if [[ $# -eq 0 ]]
   then
      usage
      exit 1
   fi

   # ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   # ║                                             Command Line Processor Options                                                 ║
   # ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

   # Define the allowed command line options
   shortopts=":g:hn:s:0"
   longopts="integer:,gauge:,counter:,timeticks:,ipaddress:,objectid:,string:"
   longopts="${longopts},help"

   # Read the command line options
   OPTS=`getopt -o $shortopts  -l $longopts -- "$@"`
   if [[ $? != 0 ]]
   then
      usage
      exit 1
   fi

   # ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   # ║                                                 Command Line Processor                                                     ║
   # ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
   # Process the command line arguments
   eval set -- "$OPTS"

   # Process the configuration options first
   while true
   do

      case "$1" in

         # Configure the get request variable
         -g)

            case "$2" in

               "")
                  shift 2
                  ;;

                *)
                  OID_GET="$2"
                  shift 2
                  ;;
            esac

            REQUEST_GET=true
            ;;


         -n)
            case "$2" in
               "") shift 2 ;;
                *) OID_GET_NEXT="$2" ; shift 2 ;;
            esac
            REQUEST_GET_NEXT=true
            ;;


         -s)
            case "$2" in
               "") shift 2 ;;
                *) OID_SET="$2" ; shift 2 ;;
            esac
            REQUEST_SET=true
            ;;


         integer)
            case "$2" in
               "") shift 2 ;;
                *)
                   container_hostname="${2}"
                   shift 2
                   ;;
            esac ;;


         gauge)
            case "$2" in
               "") shift 2 ;;
                *)
                   container_name="${2}"
                   shift 2
                   ;;
            esac ;;


         counter)
            case "$2" in
               "") shift 2 ;;
                *)
                   container_mount="${2}"
                   shift 2
                   ;;
            esac ;;


         --) shift ; break ;;
          *) shift ;;
      esac
   done


   # Process the command line arguments to execute functions
   eval set -- "$OPTS"

   # Process the functions
   while true
   do

      case "$1" in

         # Skip the get request variable
         -g)

            shift 2
            ;;


         # Skip the get next request variable
         -n)

            shift 2
            ;;


         # Skip the set request variable
         -s)

            shift 2
            ;;


         # End of command line parameters marker
         --)

            shift
            break
            ;;


         # Display the usage
         -h|--help)

            usage
            exit 1
            ;;


         # Display the debug information
         -0)

            DEBUG=true
            displayDebug
            exit 1
            ;;


         # default
         *)

            usage
            exit 1
            ;;
      esac
   done

   # We may be running on the conference server, the proxy or some other server
   determineServerType

   # Now that we know the server we are on, build our oids
   defineServerOIDs

   # Decode/Obtain the versions from the build data
   decodeBuildData

   # Process the different types of requests
   if [[ "${REQUEST_GET}" ==  "true" ]]
   then

      processGetRequest "${OID_GET}"

   elif [[ "${REQUEST_GET_NEXT}" ==  "true" ]]
   then

      processGetNextRequest "${OID_GET_NEXT}"

   fi

}


# Initial script execution point. If this script is sourced from another script, the main function will not exexute
if [ "${BASH_SOURCE[0]}" -ef "$0" ]
then

   # Call the main function, pass it the command line parameters
   main "$@"

   if [[ "${DEBUG}" == true ]]; then printInfo "Leaving "`basename "$0"`; fi
   exit 0

fi
