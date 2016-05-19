IMAGE_FOLDER='images'
BASE_URL='https://netrunnerdb.com/bundles/netrunnerdbcards/images/cards/en'

mkdir -p ${IMAGE_FOLDER}

function download_range () {
  for ((num = $1; num <= $2; num++))
  do
    if [ ! -f ${IMAGE_FOLDER}/${num}.png ]
    then
      curl ${BASE_URL}/0${num}.png -o ${IMAGE_FOLDER}/${num}.png
    fi
  done
}

# core set
download_range 1001 1113

# genesis
download_range 2001 2120

# creation and control
download_range 3001 3055

# spin
download_range 4001 4120

# honar and profit
download_range 5001 5055

#
#

# order and chaos
download_range 7001 7055
