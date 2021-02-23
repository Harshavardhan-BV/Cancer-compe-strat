# !bin/bash

# A script to check for directories named archive and convert it to a tar.xz archive.
if test -f archive.tar.xz; then
  echo 'Archive exists appending'
  unxz archive.tar.xz
  find . -type d -name archive -exec tar --remove-files -rvf archive.tar {} +
  xz archive.tar
else
  echo 'Creating a new compressed archive'
  find . -type d -name archive -exec tar --remove-files -cvJf archive.tar.xz {} +
fi
