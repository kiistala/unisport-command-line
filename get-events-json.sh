BASEURL="https://api.unisport.fi/v1/fi/events"
TODAY=$(date --rfc-3339=date)
PLUS7=$(date --date="7 days" --rfc-3339=date)
URL="$BASEURL?minDate=$TODAY&maxDate=$PLUS7&sportHierarchies=$1"

curl -s $URL
