# !/bin/sh

# run this in the top level folder to delete all timing files
# with "FEEDBACK" in them
find . | grep "FEEDBACK" | xargs rm -f
