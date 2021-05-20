docker run -itd --rm \
    --volume="`pwd`":/project \
    --name="pymeshcntr" \
    pymesh /bin/bash